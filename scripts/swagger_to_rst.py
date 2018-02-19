'''Converts Swagger 1.2 defs for TACC Cloud services to ReStructured Text'''
from __future__ import absolute_import
from __future__ import print_function
from future import standard_library
standard_library.install_aliases()

import urllib.request, urllib.parse, urllib.error

import os
import jinja2
import json
import sys
import textwrap

from operator import itemgetter

HERE = os.path.dirname(os.path.abspath(__file__))
PWD = os.getcwd()

# Excludes at the Service and Operation level
#   Used to soft-deprecate APIs or Swagger defs that
#   are too broken to use
SVC_BLACKLIST = ('agavepy.clients', 'agavepy.transforms',
                 'agavepy.admin', 'agavepy.postits')
API_BLACKLIST = ('agavepy.apps.getJobSubmissionForm',
                 'agavepy.apps.listByOntologyTerm',
                 'agavepy.apps.listByTag')
SVC_WHITELIST = ('agavepy.files')

# Jina is told to treat all of HERE as a templates
# directory so this is essentially a placeholder
RESOURCES = ('resources.json.j2',
             'abaco_resources.json.j2',
             'admin_resources.json.j2')

# Sphinx stuff
DEST = 'docs'
# Swagger stuff
SPEC = 'openapi'
# Schemas
SCHEMA = 'schema'

# RST mappings
INDENT = ' ' * 4
HEADINGS = {'title': {'char': '#', 'overline': True},
            'subtitle': {'char': '*', 'overline': True},
            'section': {'char': '=', 'overline': False},
            'subsection': {'char': '-', 'overline': False},
            'subsubsection': {'char': '^', 'overline': False},
            'paragraph': {'char': '"', 'overline': False}}
FMTS = {'bold': {'char': '**', 'wrap': True},
        'italic': {'char': '*', 'wrap': True},
        'literal': {'char': '``', 'wrap': True},
        'indent': {'char': INDENT, 'wrap': False}}

# Deployment base URL (ReadTheDocs)
RTFD_BASE_URI = 'http://agavepy.readthedocs.io/en/latest/'


class ConfigGen(object):
    def __init__(self, template_str):
        self.template_str = template_str

    def compile(self, configs, env):
        template = env.get_template(self.template_str)
        return template.render(configs)


def mod_name(api_name):
    return '.'.join(['agavepy', api_name])


def submod_name(api_name, mod_name):
    return '.'.join([mod_name, api_name])


def api_name(path):
    '''modularize API pathname'''
    p = os.path.basename(path)
    return p


def rst_link(text, uri):
    '''Return text and URI href'''
    return "'" + text + "<" + uri + ">`_"


def rst_heading(text, level):
    ltxt = len(text)
    fmt = ''
    if HEADINGS[level]['overline']:
        fmt = HEADINGS[level]['char'] * ltxt
        fmt = fmt + '\n'
    fmt = fmt + text + '\n' + (HEADINGS[level]['char'] * ltxt)
    return fmt


def rst_block(text):
    return '    ' + text


def rst_bold(text):
    return '**' + text + '**'


def rst_italic(text):
    return '*' + text + '*'


def rst_source(code, level=1, lang='python', caption=None):
    '''Wrap a code block in rst form'''
    idt = '.. code-block:: ' + lang + '\n'
    if caption is not None:
        idt = idt + '   :caption: ' + caption + '\n'
    # make sure leading newline is here after set up code-block
    idt = idt + '\n'
    indent = '    ' * level
    for line in code.split('\n'):
        idt = idt + indent + line + '\n'
    idt = idt + '\n'
    return idt


def schemify(name, classmod):
    '''Transform a Swagger class model into JSON schema'''
    try:
        schema = {"$schema": "http://json-schema.org/draft-07/schema#",
                  "$id": None,
                  "title": None, "type": "object",
                  "properties": {}, "required": []}

        schema_file_name = name + '.json'
        schema['title'] = "AgavePy {} schema".format(name)
        schema['$id'] = "{}".format(os.path.join(
            RTFD_BASE_URI, schema_file_name))
        props_tmp = {}
        for p in classmod.items():
            if p[1].get('required', None):
                schema['required'].append(p[0])
            props_tmp[p[0]] = {'type': p[1].get('type', 'string'),
                               'description': p[1].get('description', '')}
            if p[1].get('enum', None) is not None:
                props_tmp[p[0]]['enum'] = p[1].get('enum')
        schema['properties'] = props_tmp.copy()
        jsp = json.dumps(schema, indent=2, sort_keys=True)
        jsf = open(os.path.join(PWD, SCHEMA, schema_file_name), 'w')
        jsf.write(jsp + '\n')
        jsf.close()

        return rst_source(code=jsp, level=1, lang='javascript')
    except KeyError:
        return ''


def load_resource(resource_file, api_server='https://api.tacc.cloud'):
    """Load a default resource file.

    :type api_server: str
    :rtype: dict
    """
    conf = ConfigGen(os.path.join('agavepy', resource_file))
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(PWD),
                             trim_blocks=True, lstrip_blocks=True)
    rsrcs = json.loads(conf.compile(
        {'api_server_base': urllib.parse.urlparse(api_server).netloc}, env))
    return rsrcs


def write_swagger_1_2(res, filename='openapi', form='json'):
    '''Write a validating swagger1.2 spec out to world-readable location'''
    assert form in ('json', 'yaml')

    # set up paths
    base_path = os.path.join(PWD, SPEC, '1.2')
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    apis_subdir = 'APIs'
    api_path = os.path.join(base_path, apis_subdir)
    if not os.path.exists(api_path):
        os.mkdir(api_path)

    # main swagger.json
    swag = {'apiVersion': res['apiVersion'],
            'apis': [],
            'info': res['info'],
            'produces': res['produces'],
            'swaggerVersion': res['swaggerVersion'],
            'url': res['url']}

    for api in res['apis']:
        idx = {'description': api['description'],
               'path': os.path.join(apis_subdir, api['name'] + '.json')}
        swag['apis'].append(idx)

    try:
        f = open(os.path.join(base_path, filename + '.' + form), 'w')
        f.write(json.dumps(swag, indent=2, sort_keys=True))
        f.close()
    except Exception as e:
        print(("Failure to write Index {}: {}".format(filename, e)))
        sys.exit(1)

    # individual api definitions
    # iterate thru apis
    #  - transform if needed the write to standalone apis/<name>.json
    for api in res['apis']:
        api_def = api.copy()
        api_filename = api_def['name'] + '.' + form
        # dict contains list of any keys to remove from definition
        # url is redundant and actively damaging
        for strip_key in ('url'):
            api_def.pop(strip_key, None)

        try:
            f = open(os.path.join(api_path, api_filename), 'w')
            f.write(json.dumps(api_def, indent=2, sort_keys=True))
            f.close()
        except Exception as e:
            print(("Failure to write API {}: {}".format(api_filename, e)))
            sys.exit(1)

    return True


def main():
    res = load_resource('resources.json.j2')
    write_swagger_1_2(res)

    for api in res.get('apis', []):

        api_name = mod_name(api.get('name'))
        #if api_name in WHITELIST and api_name not in BLACKLIST:
        if api_name not in SVC_BLACKLIST:

            print("{}/".format(api_name))

            f = open(os.path.join(PWD, DEST, api_name + '.rst'), 'w')
            # example: agavepy.apps
            f.write(rst_heading(api_name, 'subtitle') + '\n\n')
            f.write("Summary: {}".format(api.get('description')) + '\n\n')

            # class models
            # JSON objects expected by the API as 'body'
            # parameters
            classmods = {}
            # response mods
            respmods = {}

            for mk in api['api_declaration']['models'].keys():
                mod = api['api_declaration']['models'][mk]
                if 'Response' not in mk:
                    classmods[mk] = mod['properties'].copy()
                else:
                    respmods[mk] = mod['properties'].copy()

            for sub_api in api['api_declaration']['apis']:
                # Iterate through operations
                op_list = sorted(sub_api.get('operations'),
                                 key=itemgetter('nickname'),
                                 reverse=False)

                for op in op_list:
                #for op in sub_api.get('operations'):
                    # agavepy.apps.list
                    submod_name_path = submod_name(
                        op.get('nickname'), api_name)
                    if submod_name_path not in API_BLACKLIST:
                        print(" - {}".format(op.get('nickname')))

                        # assemble param list for func signature
                        arglist = []
                        kwarglist = []
                        # param list for formatted list
                        fmtlist = []

                        for param in op.get('parameters'):
                            jtype = param.get('type')
                            ptype = param.get('paramType')
                            pdesc = param.get('description')
                            pname = param.get('name')
                            fmtlist.append({'name': pname, 'jtype': jtype,
                                            'ptype': ptype, 'desc': pdesc})

                            if param['required']:
                                arglist.append(param['name'])
                            else:
                                # use to extract exemplar JSON where provided
                                default = param.get('defaultValue')
                                kwarglist.append(param['name'] + '=' + str(
                                    param.get('defaultValue', None)))

                        codeargs = sorted(arglist) + sorted(kwarglist)
                        fmtcodeargs = ', '.join(codeargs)

                        # operation name
                        f.write(rst_heading(op.get('nickname') + ': ' + op.get('summary'),
                                            'section') + '\n')

                        f.write('``' + (submod_name_path +
                                '(' + fmtcodeargs + ')') + '``\n\n')
                        #f.write(op.get('summary') + '\n\n')

                        f.write(rst_heading('Parameters:',
                                            'subsection') + '\n')
                        for fp in fmtlist:
                            # compute type
                            fmttype = fp['jtype']
                            fmtdesc = fp['desc']

                            if fp['ptype'] == 'body':
                                fmttype = 'JSON, ' + fp['jtype']

                            f.write('    * ' + rst_bold(fp['name']) +
                                    ': ' + fmtdesc + ' (' + fmttype + ')' +
                                    '\n')

                        f.write('\n\n')
                        # format JSON schema for request object
                        if fp['ptype'] == 'body':
                            if fp['jtype'] != 'string':
                                if fp['jtype'] in classmods:
                                    f.write(rst_bold(fp['jtype'] +
                                            ' schema') + '\n\n')
                                    js = schemify(fp['jtype'],
                                                  classmods[fp['jtype']])
                                    f.write(js)

                        f.write(rst_heading('Response:', 'subsection') + '\n')

                        resp_type = op.get('type')
                        resp_string = 'None'
                        resp_schema_type = None

                        if resp_type in respmods:
                            try:
                                resp_type_obj = respmods[resp_type]['result']['type']
                            except KeyError as e:
                                print("ResponseType: {}".format(resp_type))
                                print("Value: {} / Error: {}".format(
                                    respmods[resp_type], e))
                                pass
                            if resp_type_obj == 'array':
                                # get item $ref
                                resp_item = respmods[resp_type]['result']['items']['$ref']
                                resp_schema_type = resp_item
                                resp_string = "Array of {} objects".format(resp_item)
                            elif resp_type_obj in ('string', 'integer', 'int', 'boolean'):
                                resp_string = resp_type_obj.capitalize()
                            else:
                                # agavepy class object
                                resp_schema_type = resp_type_obj
                                resp_string = "A single {} object".format(resp_type_obj)

                        f.write('    * ' + rst_italic(resp_string) + '\n\n')

                        # print schema if response is single or array of agavepy class obj
                        if resp_schema_type is not None:
                            if resp_schema_type in classmods:
                                f.write(rst_bold(resp_schema_type +
                                        ' schema') + '\n\n')
                                js = schemify(resp_schema_type,
                                              classmods[resp_schema_type])
                                f.write(js)
            f.close()


if __name__ == '__main__':
    main()

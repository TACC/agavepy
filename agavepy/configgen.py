import jinja2
import json
import logging
import os

from future import standard_library
standard_library.install_aliases()  # noqa
from urllib.parse import urlparse, urlencode, urljoin, urlsplit  # noqa

HERE = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(
    os.environ.get('TAPISPY_LOG_LEVEL', logging.WARNING))

__all__ = ['ConfigGen', 'load_resource', 'updateDict']


class ConfigGen(object):
    def __init__(self, template_str):
        self.template_str = template_str

    def compile(self, configs, env):
        template = env.get_template(self.template_str)
        return template.render(configs)


def updateDict(base_dict, new_dict):
    for key, val in new_dict.items():
        if isinstance(val, dict):
            base_dict[key] = updateDict(base_dict.get(key, {}), val)
        elif isinstance(val, list):
            if key not in base_dict:
                base_dict[key] = []
            for list_dict in val:
                base_dict[key].append(list_dict)
        else:
            base_dict[key] = val
    return base_dict


def load_resource(api_server):
    """Load a default resource file.

    :type api_server: str
    :rtype: dict
    """
    logger.debug('load_resource({0})...'.format(api_server))
    rsrcs = {}
    rsrc_files = [
        "resources/misc.json.j2",
        "resources/api_clients.json.j2",
        "resources/api_apps.json.j2",
        "resources/api_files.json.j2",
        "resources/api_jobs.json.j2",
        "resources/api_meta.json.j2",
        "resources/api_monitors.json.j2",
        "resources/api_notifications.json.j2",
        "resources/api_postits.json.j2",
        "resources/api_profiles.json.j2",
        "resources/api_systems.json.j2",
        "resources/api_transforms.json.j2",
        "resources/api_actors.json.j2",
        "resources/api_admin.json.j2",
    ]
    for rsrc_file in rsrc_files:
        conf = ConfigGen(rsrc_file)
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(HERE),
                                 trim_blocks=True,
                                 lstrip_blocks=True)

        new_rsrcs = json.loads(
            conf.compile({"api_server_base": urlparse(api_server).netloc},
                         env))
        updateDict(rsrcs, new_rsrcs)

    logger.debug('load_resource finished')
    return rsrcs

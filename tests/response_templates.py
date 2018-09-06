import json
import pkg_resources


rsc_pkg = __name__


def response_template_to_json(template_name):
    rsc_path = "/".join(("sample_responses", template_name))
    return json.loads(pkg_resources.resource_string(rsc_pkg, rsc_path))

import json
import pkg_resources


rsc_pkg = __name__


def response_template_to_json(template_name):
    rsc_path = "/".join(("sample_responses", template_name))
    try: # Python 3.3 will return the contents as a bytes-like object.
        file_contents = pkg_resources.resource_string(rsc_pkg, rsc_path).decode("utf-8")
    except AttributeError:
        file_contents = pkg_resources.resource_string(rsc_pkg, rsc_path)
    return json.loads(file_contents)

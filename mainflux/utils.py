ThingPrefix = "Thing "
BearerPrefix = "Bearer "
# CTJSON represents JSON content type.
CTJSON = "application/json"

# CTJSONSenML represents JSON SenML content type.
CTJSONSenML = "application/senml+json"


def construct_header(token: str, content_type: str):
    headers = dict()
    if token != "":
        if not token.__contains__(ThingPrefix):
            token = BearerPrefix + token
        headers["Authorization"] = token
    if content_type != "":
        headers["Content-Type"] = content_type
    return headers

def handle_error(error_dict, status_code):
    if status_code in error_dict.keys():
        return error_dict[status_code]
    elif status_code in errors.keys():
        return errors[status_code]
    else:
        return "Unknown error"


errors = {
    400: "Failed due to malformed JSON.",
    401: "Missing or invalid access token provided.",
    403: "Missing or invalid access token provided.",
    404: "A non-existent entity request.",
    409: "Entity already exist.",
    415: "Missing or invalid content type.",
    422: "Database can't process request.",
    500: "Unexpected server-side error occurred.",
}

users = {
    "create": {
        409: "Failed due to using an existing identity.",
    },
    "login": {
        409: "Failed due to using an existing email address.",
    },
    "refresh_token": {
        404: "A non-existent entity request.",
    },
    "get": {
        400: "Failed due to malformed query parameters.",
    },
    "get_all": {
        400: "Failed due to malformed query parameters.",
    },
    "update": {
        404: "Failed due to non existing user.",
    },
    "update_user_identity": {
        401: "Missing or invalid access token provided.",
    },
    "update_user_tags": {
        401: "Missing or invalid access token provided.",
    },
    "update_user_owner": {
        401: "Missing or invalid access token provided.",
    },
    "enable": {
        404: "Failed due to non existing user."
    },
    "disable": {
        404: "Failed due to non existing user."
    },
    "reset_password_request": {
        400: "Failed due to malformed JSON."
    },
    "reset_password": {
        400: "Failed due to malformed JSON."
    },
    "authorise_user":{
        400: "Failed due to malformed JSON."
    }
}

things = {
    "create": {
        422: "Unprocessable Entity."
    },
    "create_bulk": {
    },
    "get": {
        400: "Failed due to malformed query parameters.",
        404: "Thing does not exist.",
    },
    "get_all": {
        404: "Thing does not exist.",
    },
    "get_by_channel": {
        400: "Failed due to malformed query parameters.",
    },
    "update": {
        404: "Thing does not exist.",
    },
    "update_thing_secret": {
        401: "Missing or invalid access token provided.",
    },
    "update_thing_tags": {
        401: "Missing or invalid access token provided.",
    },
    "update_thing_owner": {
        401: "Missing or invalid access token provided.",
    },
    "delete": {
        400: "Failed due to malformed thing's ID.",
    },
    "connect": {
        400: "A non-existent entity request."
    },
    "disconnect": {
        400: "Failed due to malformed query parameters.",
        404: "Channel or thing does not exist.",
    },
    "share_thing": {
        400: "A non-existent entity request."
    },
    "authorise_thing":{
        403: "False",
    },
}

channels = {
    "create": {
        409: "Failed due to using an existing identity."
    },
    "create_bulk": {
        401: "Missing or invalid access token provided."
    },
    "get": {
        401: "Missing or invalid access token provided."
    },
    "get_all": {
        400: "Failed due to malformed channel's ID.",
        404: "Channel does not exist.",
    },
    "get_by_thing": {
        400: "Failed due to malformed query parameters.",
        404: "Thing does not exist.",
    },
    "update": {
        404: "Channel does not exist."
    },
    "delete": {
        400: "Failed due to malformed channel's ID."
    },
    "identify_thing":{
        401: "Thing and channel are not connected, or thing with specified key doesn't exist."
    },
}

messages = {
    "send": {
        400: "Message discarded due to its malformed content.",
        403: "Message discarded due to missing or invalid credentials.",
        404: "Message discarded due to invalid channel id.",
        415: "Message discarded due to invalid or missing content type.",
    },
    "read": {
        400: "Failed due to malformed query parameters.",
    },
}

groups = {
    "create": {
        409: "Failed due to using an existing email address.",
    },
    "get": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
    "get_all": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
    "update": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
    "members": {
        409: "Failed due to using an existing email address.",
    },
    "memberships":{
        400: "Failed due to malformed query parameters."  
    },
    "parents": {
        400: "Failed due to malformed query parameters."
    },
    "children": {
        400: "Failed due to malformed query parameters."
    },
    "assign": {
        400: "Failed due to malformed JSON."
    }, 
    "unassign": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
    "disable": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
}

bootstrap = {
    "add": {
        401: "Missing or invalid access token provided.",
    },
    "view": {
        404: "Config does not exist.",
    },
    "whitelist": {
        204: "Config removed.",
        400: "Failed due to malformed config's ID.",
    },
    "update": {
        404: "Config does not exist.",
    },
    "bootstrap": {
        404: "Failed to retrieve corresponding config."
    },
    "remove": {
        400: "Failed due to malformed config ID."
    } 
}
certs = {
    "issue": {
        401: "Missing or invalid access token provided.",
    },
    "view_by_thing": {
        404: "Failed to retrieve corresponding certificate.",
    },
    "view_by_serial": {
        404: "Failed to retrieve corresponding certificate.",
    },
    "revoke": {
        404: "Failed to revoke corresponding certificate.",
    },
    "serials": {
        404: "Failed to retrieve corresponding certificates.",
    },
}

Module lib.api
==============

Classes
-------

`Api(url)`
:   

    ### Methods

    `create(self, user_token, duration_params)`
    :   Generates a new API key

    `get_key_details(self, user_token, key_id)`
    :   Gets API key details for the given key

    `revoke(self, user_token, key_id)`
    :   Revoke API key identified by the given ID.
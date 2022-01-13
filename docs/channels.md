Module lib.channels
===================

Classes
-------

`Channels(url)`
:   

    ### Methods

    `check_access_by_id(self, channel_id, thing_id)`
    :   Checks if thing has access to a channel

    `construct_query(self, params)`
    :

    `create(self, channel, token)`
    :   Creates channel entity in the database

    `create_bulk(self, channels, token)`
    :   Creates multiple channels in a bulk

    `delete(self, chanID, token)`
    :   Deletes a channel entity from database

    `get(self, chanID, token)`
    :   Gets a channel entity for a logged-in user

    `get_all(self, token, query_params=None)`
    :   Gets all channels from database

    `get_by_thing(self, thing_id, params, token)`
    :   Gets all channels to which a specific thing is connected to

    `update(self, channel_id, token, channel)`
    :   Updates channel entity
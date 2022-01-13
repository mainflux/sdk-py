Module lib.things
=================

Classes
-------

`Things(url)`
:   

    ### Methods

    `connect(self, channel_ids, thing_ids, token)`
    :   Connects thing and channel

    `construct_query(self, params)`
    :

    `create(self, thing, token)`
    :   Creates thing entity in the database

    `create_bulk(self, things, token)`
    :   Creates multiple things in a bulk

    `delete(self, thing_id, token)`
    :   Deletes a thing entity from database

    `disconnect(self, channel_ids, thing_ids, token)`
    :   Disconnect thing and channel

    `disconnect_things(self, channel_ids, thing_ids, token)`
    :   Disconnect things from channels specified by lists of IDs

    `get(self, thing_id, token)`
    :   Gets a thing entity for a logged-in user

    `get_all(self, token, query_params=None)`
    :   Gets all things from database

    `get_by_channel(self, channel_id, params, token)`
    :   Gets all things to which a specific thing is connected to

    `update(self, thing_id, token, thing)`
    :   Updates thing entity
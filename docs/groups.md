Module lib.groups
=================

Classes
-------

`Groups(url)`
:   

    ### Methods

    `assign(self, group_id, token, members)`
    :   Assign

    `construct_query(self, params)`
    :

    `create(self, group, token)`
    :   Creates group entity in the database

    `delete(self, group_id, token)`
    :   Deletes a group entity from database

    `get(self, group_id, token)`
    :   Gets a group entity

    `get_all(self, group_id, token, query_params=None)`
    :   Gets all groups from database

    `members(self, group_id, token)`
    :   Get list of members ID's from group

    `share_groups(self, token, user_group_id, thing_group_id)`
    :   Adds access rights on thing groups to the user group

    `unassign(self, group_id, token, members)`
    :   Assign

    `update(self, group_id, token, group)`
    :   Updates group entity
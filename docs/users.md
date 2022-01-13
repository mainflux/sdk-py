Module lib.users
================

Classes
-------

`Users(url)`
:   

    ### Methods

    `create(self, user)`
    :   Creates user entity in the database

    `get(self, user_id, token)`
    :   Gets a user entity for a logged-in user

    `get_all(self, token)`
    :   Gets all users from database

    `login(self, user)`
    :   Creates a user token

    `update(self, user, token)`
    :   Updates user entity

    `update_password(self, old_password, password, token)`
    :   Changes user password
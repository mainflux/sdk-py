import requests
import json

from mainflux import response
from mainflux import errors
from mainflux import utils


class Users:
    """Users API client.
    
    Users API is used for creating and managing users.
    It is used for creating new users, logging in, refreshing tokens,
    getting user information, updating user information, disabling 
    and enabling users.
    
    Attributes:
        URL: str - URL of the Users API
        USERS_ENDPOINT: str - Users API endpoint
    """
    USERS_ENDPOINT = "users"

    def __init__(self, url: str):
        self.URL = url
    """Initializes Users API client.
        
        params:
            url: str - URL of the Users API
        
        returns:
            Users: Users - Users API client
            
        raises:
            None
    """
    def create(self, user: dict, token: str = ""):
        """Creates a new user.
        
        Creates a new user with provided user information.
        If token is provided, it will be used to create a new user.

        params:
            user: dict - user information for example:
            {
                "name": "example",
                "credentials": {
                    "identity": "example@main.com",
                    "secret": "12345678"
                }
            }
            token: str - token used for creating a new user
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> user = {
            ...     "name": "example",
            ...     "credentials": {
            ...         "identity": "example@mail.com",
            ...         "secret": "12345678"
            ...     }
            ... }
            >>> mf_resp = mfsdk.users.create(user)
            >>> mf_resp            
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/users",
            json=user,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["create"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def login(self, user: dict):
        """Generates an access token when provided with proper credentials.
        
        Issues a new access and refresh token for a user for authenticating 
        into the system.
        
        params: 
            user: a dict with the user information and password for example: 
            {"credentials":{
                "identity": "user@mainflux.com",
                "secret": "12345678"
                }
            }
        returns: 
            mf_resp: response.Response - response object
        
        Usage:: 
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> credentials= {
            ...         "identity": "user@mainflux.com",
            ...         "secret": "12345678"
            ... }
            >>> mf_resp = mfsdk.users.login(credentials)
            >>> mf_resp                
        """
        mf_resp = response.Response()
        http_resp = requests.post(self.URL + "/users/tokens/issue", json=user)
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["login"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def refresh_token(self, refresh_token: str):
        """Refreshes Access and Refresh Token used for authenticating 
        into the system.
        
        Creates a new access token and refresh token for a user when 
        provided with a valid refresh token.
        
        params: 
            refresh_token: str - token used to refresh access. 
        
        returns: 
            mf_resp: response.Response - response object
        
        Usage:: 

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> mf_resp = mfsdk.users.refresh_token(refresh_token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/users/tokens/refresh",
            headers=utils.construct_header(refresh_token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["refresh_token"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get(self, user_id: str, token: str):
        """Gets a user information.
        
        Gets info on currently logged in user. Info is obtained 
        using authorization token and the user id.

        params:
            user_id: str - user information eg "886b4266-77d1-4258-abae-2931fb4f16de",
            token: str - token used for creating a new user
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> user_id = "886b4266-77d1-4258-abae-2931fb4f16de"
            >>> token = ""
            >>> mf_resp = mfsdk.users.get(user_id, token)
            >>> mf_resp            
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["get"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_all(self, query_params: dict, user_token: str):
        """Retrieves a list of users. 
        
        Gets a list of users from the database when provided with a user token and
        some parameters. 
        
        params: 
            user_token: str - token used for creating a new user
            query_params: dict - has a limit(int) which is the size of the subset
                to be expected and offset which is the number of items to skip during retrieval.
                For example:
                {
                    "offset" : 0, "limit" : 10
                }
                
        returns:
            mf_resp: response.Response - response object
        
        Usage::

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> query_params = {
            ...     "offset" : 0, "limit" : 10
            ...     }
            >>> mf_resp = mfsdk.users.get(query_params, user_token)
            >>> mf_resp        
        """
        http_resp = requests.get(
            self.URL + "/" + self.USERS_ENDPOINT,
            headers=utils.construct_header(user_token, utils.CTJSON),
            params=query_params,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["get_all"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, user: dict, user_token: str):
        """Updates information on currently logged in user. 
        
        Information such as name and metadata is updated using authorization user_token

        params:
            user: dict - user information for example:
            {
                "name": "example",
                "id": "886b4266-77d1-4258-abae-2931fb4f16de"
                "credentials": {
                    "identity": "example@main.com",
                    "secret": "12345678"
                },
                "metadata": {
                    "foo": "bar"
                }
            }
            token: str - token used for creating a new user
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> user = {
            ...     "name": "example",
            ...     "id": "886b4266-77d1-4258-abae-2931fb4f16de"
            ...     "metadata": {
            ...            "foo": "bar"
            ...        }
            ... }
            >>> mf_resp = mfsdk.users.update(user, token)
            >>> mf_resp            
        """
        http_resp = requests.patch(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user["id"],
            headers=utils.construct_header(user_token, utils.CTJSON),
            data=json.dumps(user),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["update"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_user_identity(self, user: dict, user_token: str):
        """Updates identity information on currently logged in user. 
        
        The user Identity is updated using authorization user_token

        params:
            user: dict - user information for example:
            
            {
                "name": "example",
                "id": "886b4266-77d1-4258-abae-2931fb4f16de"
                "credentials": {
                    "identity": "example@main.com",
                    "secret": "12345678"
                },
                "metadata": {
                    "foo": "bar"
                }
            }
            token: str - token used for creating a new user
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> user = {
            ...    "name": "example",
            ...    "id": "886b4266-77d1-4258-abae-2931fb4f16de"
            ...    "credentials": {
            ...        "identity": "example@main.com",
            ...        "secret": "12345678"
            ...    },
            ...    "metadata": {
            ...        "foo": "bar"
            ...     }
            ... }
            >>> mf_resp = mfsdk.users.update_user_identity(user, user_token)
            >>> mf_resp            
        """
        http_resp = requests.patch(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user["id"] + "/identity",
            headers=utils.construct_header(user_token, utils.CTJSON),
            data= json.dumps(user),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["update_user_identity"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_user_tags(self, user: dict, user_token: str):
        """Updates tags on currently logged in user. 
        
        Updates tags of the user with provided ID. Tags is updated using 
        authorization token and the new tags received in request.

        params:
            user: dict - user information for example:
            
            {
                "name": "example",
                "id": "886b4266-77d1-4258-abae-2931fb4f16de"
                "tags": [
                    "back",
                    "end"
                ]
                "metadata": {
                    "foo": "bar"
                }
            }
            token: str - token used for creating a new user
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> user = {
            ...     "name": "example",
            ...     "id": "886b4266-77d1-4258-abae-2931fb4f16de"
            ...     "tags": [
            ...        "back",
            ...        "end"
            ...     ]
            ... }
            >>> mf_resp = mfsdk.users.update_user_tags(user, user_token)
            >>> mf_resp            
        """
        http_resp = requests.patch(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user["id"] + "/tags",
            headers=utils.construct_header(user_token, utils.CTJSON),
            data=json.dumps(user),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["update_user_tags"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_user_owner(self, user: dict, user_token: str):
        """Updates owner on currently logged in user. 
        
        Updates owner for the user with provided ID. Owner is updated using 
        authorization token and a new owner identifier received in request.

        params:
            user: dict - user information for example:
            
            {
                "name": "example",
                "id": "886b4266-77d1-4258-abae-2931fb4f16de"
                "owner": "c52d-3b0d-43b9-8c3e-275c087d875af"
            }
            token: str - token used for creating a new user
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> user = {
            ...     "name": "example",
            ...     "id": "886b4266-77d1-4258-abae-2931fb4f16de",
            ...     "owner": "c52d-3b0d-43b9-8c3e-275c087d875af"
            ... }
            >>> mf_resp = mfsdk.users.update_user_owner(user, user_token)
            >>> mf_resp            
        """
        http_resp = requests.patch(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user["id"] + "/owner",
            headers=utils.construct_header(user_token, utils.CTJSON),
            data=json.dumps(user),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["update_user_owner"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_password(self, old_secret: str, new_secret: str, user_token: str):
        """Changes user password.
        
        Updates secret of currently logged in user. Secret is updated using 
        authorization token and the new received info. 

        params:
            old_secret: str - the logged in user's current secret.
            new_secret: str - the user's new secret.
            token: str - token used for creating a new user
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            ... old_secret = 12345678
            ... new_secret = 87654321
            >>> mf_resp = mfsdk.users.update(old_secret, new_secret, user_token)
            >>> mf_resp            
        """
        payload = {"old_secret": old_secret, "new_secret": new_secret}
        http_resp = requests.patch(
            self.URL + "/" + self.USERS_ENDPOINT + "/secret",
            headers=utils.construct_header(user_token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["update"], http_resp.status_code
            )
        else:
            mf_resp.value = "OK"
        return mf_resp

    def reset_password_request(self, email: str, url: str):
        """User Password reset request. 
        
        Generates a reset token and sends an email to the user
        with link for resetting password.
        
        params:
            referrer email: str - this is the host being sent by the browser.
                            The email must be valid preferably gmail and ensure that the email is 
                            already linked to a user as their identity in the database.
                            The email is part of the header.
            url: str - http://localhost/reset-request
            
        returns: 
            mf_resp: response.Response - response object
        
        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            ... email = admin@example.com
            ... url = stp@gmail.com
            >>> mf_resp = mfsdk.users.reset_password_request(email, url)
            >>> mf_resp
        """
        http_resp = requests.post(
            self.URL + "/password/reset-request",
            headers={"Referer": url},
            json={"email": email},
        )
        mf_resp = response.Response()
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["reset_password_request"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def reset_password(self, password: str, confirm_password: str, token: str):
        """Changes user password with the reset_request token
        
        When user gets reset token, after he submitted email to 
        /password/reset-request, posting a new password along to this 
        endpoint will change password.
        
        params: 
            passwor: str - the user's new password.
            confirm_password: str - a recurrence of the password to ensure it
            is the same.
            token: str - the reset token recieved from the reset_request email.
            
        returns: 
            mf_resp: "OK"
        
        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            ... password = 234567
            ... confirm_password = 234567
            >>> mf_resp = mfsdk.users.reset_password(password, confirm_password, token)
            >>> mf_resp
        """
        payload = {
            "password": password,
            "confirm_password": confirm_password,
            "token": token,
        }
        http_resp = requests.put(
            self.URL + "/password/reset",
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["reset_password"], http_resp.status_code
            )
        else:
            mf_resp.value = "OK"
        return mf_resp

    def enable(self, user_id: str, user_token: str):
        """Enables a disabled user account for a given user ID. 
        
        Takes in the disabled User's ID and a valid token and enables the user.

        params:
            user_id: str - the user's given ID.
            token: str - token used for enabling a user
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> user_id= "886b4266-77d1-4258-abae-2931fb4f16de"
            >>> mf_resp = mfsdk.users.enable(user_id, user_token)
            >>> mf_resp            
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user_id + "/enable",
            headers=utils.construct_header(user_token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["enable"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disable(self, user_id: str, user_token: str):
        """Disables an enabled user account for a given user ID. 

        params:
            user_id: str - the user's given ID.
            token: str - token used for enabling a user
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> user_id= "886b4266-77d1-4258-abae-2931fb4f16de"
            >>> mf_resp = mfsdk.users.disable(user_id, user_token)
            >>> mf_resp            
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user_id + "/disable",
            headers=utils.construct_header(user_token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["disable"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def authorise_user(self, access_request: dict, token: str):
        """Authorises user
        
        Creates policies for a user as a subject over a group which is the object. 
        It authorizes the User to perform some actions over the group. 

        params:
            access_request = {
            "subject": "<user_id>",
            "object": "<group_id>",
            "action": "<action>",
            "entity_type": "<entity_type>"
            }
            token: strOnly admin can use this endpoint. Therefore, you need 
                an authentication token for the admin. Also, only policies 
                defined on the system are allowed to add.
            
        returns:
            mf_resp: "True"

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> access_request = {
            ...     "subject": "<user_id>",
            ...     "object": "<group_id>",
            ...     "action": "<action>",
            ...     "entity_type": "<entity_type>"
            ...     }
            >>> mf_resp = mfsdk.users.authorise_user(access_request, token)
            >>> mf_resp            
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/authorize",
            headers=utils.construct_header(token, utils.CTJSON),
            json=access_request,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["authorise_user"], http_resp.status_code
            )
        else:
            mf_resp.value = "True"
        return mf_resp

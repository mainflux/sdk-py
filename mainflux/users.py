import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Users:
    USERS_ENDPOINT = "users"

    def __init__(self, url: str):
        self.URL = url

    def create(self, user: dict, token: str = ""):
        """Registers new user account given email and password. New account
        will be uniquely identified by its email address."""
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
        """Generates an access token when provided with proper credentials."""
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
        """Refreshes Access and Refresh Token used for authenticating into the system."""
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
        """Gets a user information"""
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
        """Retrieves a list of users"""
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
        """Updates info on currently logged in user. Info is updated using authorization user_token"""
        http_resp = requests.patch(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user["id"],
            headers=utils.construct_header(user_token, utils.CTJSON),
            data=user,
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
        """Updates Identity of the user"""
        http_resp = requests.patch(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user["id"] + "/identity",
            headers=utils.construct_header(user_token, utils.CTJSON),
            data=user,
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
        """Updating user tags in the database"""
        http_resp = requests.patch(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user["id"] + "/tags",
            headers=utils.construct_header(user_token, utils.CTJSON),
            data=user,
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
        """Updating user tags in the database"""
        http_resp = requests.patch(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user["id"] + "/owner",
            headers=utils.construct_header(user_token, utils.CTJSON),
            data=user,
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
        """Changes user password"""
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
        """User Password reset request"""
        http_resp = requests.post(
            self.URL + "/password/reset-request",
            headers= {"Referer": url},
            json= {"email": email} 
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
        """Changes user password with the reset_request token"""
        payload = {"password": password, "confirm_password": confirm_password, "token": token}
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
        """Enables a disabled user account for a given user ID."""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.USERS_ENDPOINT + "/" + user_id + "/enable",
            headers=utils.construct_header(user_token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["enable"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disable(self, user_id: str, user_token: str):
        """Disables an enabled user account for a given user ID."""
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

    def authorise_user(self,access_request: dict, token: str):
        """Authorises user"""
        mf_resp = response.Response()
        http_resp= requests.post(
            self.URL +"/authorize",
            headers=utils.construct_header(token, utils.CTJSON),
            json= access_request
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.users["authorise_user"], http_resp.status_code
            )
        else:
            mf_resp.value = "True"
        return mf_resp

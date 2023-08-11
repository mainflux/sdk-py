import requests
import json

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

    def get_all(self, query_params: dict, admin_token: str):
        """Retrieves a list of users"""
        http_resp = requests.get(
            self.URL + "/" + self.USERS_ENDPOINT,
            headers=utils.construct_header(admin_token, utils.CTJSON),
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
        """Updates info on currently logged in user. Info is updated using
        authorization user_token"""
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

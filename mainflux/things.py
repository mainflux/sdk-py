import requests
from mainflux import response
from mainflux import errors
from mainflux import utils


class Things:
    THINGS_ENDPOINT = "things"
    CONNECT_ENDPOINT = "connect"
    DISCONNECT_ENDPOINT = "disconnect"
    IDENTIFY_ENDPOINT= "identify"

    def __init__(self, url: str):
        self.URL = url

    def create(self, thing: dict, token: str):
        """Creates thing entity in the database"""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.THINGS_ENDPOINT,
            json=thing,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["create"], http_resp.status_code
            )
        else:
             mf_resp.value = http_resp.json()
        return mf_resp

    def create_bulk(self, things: list, token: str):
        """Creates multiple things in a bulk"""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.THINGS_ENDPOINT + "/bulk",
            json=things,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["create_bulk"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get(self, thing_id: str, token: str):
        """Gets a thing entity for a logged-in user"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.THINGS_ENDPOINT + "/" + thing_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["get"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_all(self, query_params: dict, token: str):
        """Gets all things from database"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.THINGS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["get_all"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_by_channel(self, channel_id: str, query_params: dict, token: str):
        """Gets all things to which a specific thing is connected to"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/channels/" + channel_id + "/" + self.THINGS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["get_by_channel"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, thing_id: str, thing: dict, token: str):
        """Updates thing entity"""
        http_resp = requests.patch(
            self.URL + "/" + self.THINGS_ENDPOINT + "/" + thing_id,
            json=thing,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["update"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
    
    def update_thing_secret(self, thing_id: str, thing: dict, token: str):
        """Updates thing secret"""
        http_resp = requests.patch(
            self.URL + "/" + self.THINGS_ENDPOINT + "/" + thing_id + "/secret",
            json=thing,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["update_thing_secret"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
    
    def update_thing_tags(self, thing_id: str, thing: dict, token: str):
        """Updates thing secret"""
        http_resp = requests.patch(
            self.URL + "/" + self.THINGS_ENDPOINT + "/" + thing_id + "/tags",
            json=thing,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["update_thing_tags"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
    
    def update_thing_owner(self, thing_id: str, thing: dict, token: str):
        """Updates thing secret"""
        http_resp = requests.patch(
            self.URL + "/" + self.THINGS_ENDPOINT + "/" + thing_id + "/owner",
            json=thing,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["update_thing_owner"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disable(self, thing_id: str, token: str):
        """Deletes a thing entity from database"""
        http_resp = requests.post(
            self.URL + "/" + self.THINGS_ENDPOINT + "/" + thing_id + "/disable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["delete"], http_resp.status_code
            )
        return mf_resp

    def connects(self, thing_ids: list, channel_ids: list, actions: list, token: str):
        """Connects thing and channel"""
        payload = {"subjects": thing_ids, "objects": channel_ids, "actions": actions}
        http_resp = requests.post(
            self.URL + "/connect",
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["connect"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disconnects(self, thing_ids: list, channel_ids: list, token: str):
        """Disconnect thing and channel"""
        payload = {"subjects": thing_ids, "objects": channel_ids}
        http_resp = requests.post(
            self.URL + "/disconnect",
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["disconnect"], http_resp.status_code
            )
        return mf_resp

    def connect(self, thing_id: str, channel_id: str, action: str, token: str):
        """Connects thing and channel"""
        payload= {"subject": thing_id, "object": channel_id, "action": action}
        http_resp = requests.post(
            self.URL + "/policies",
            headers=utils.construct_header(token, utils.CTJSON),
            json= payload, 
        )
        mf_resp = response.Response()
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["connect"], http_resp.status_code
            )
        else:
            mf_resp.value = "connected"
        return mf_resp

    def disconnect(self, thing_id: str, channel_id: str, token: str):
        """Disconnect thing and channel"""
        payload = {"subject": thing_id, "object": channel_id}
        http_resp = requests.post(
            self.URL + "/disconnect",
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["disconnect"], http_resp.status_code
            )
        return mf_resp
    
    def share_thing(self, user_id: str, channel_id: str, actions: list, token: str):
        """Share thing"""
        payload = {"object": channel_id, "subject": user_id, "actions": actions, "external": True}
        http_resp = requests.post(
            self.URL + "/policies",
            headers=utils.construct_header(token, utils.CTJSON),
            data=payload
        )
        mf_resp = response.Response()
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["share_thing"], http_resp.status_code
            )
        else:
            mf_resp.value = "OK"
        return mf_resp
    
    def authorise_thing(self,access_request: dict, token: str):
        """Authorises thing"""
        mf_resp = response.Response()
        http_resp= requests.post(
            self.URL +"/channels/object/access",
            headers=utils.construct_header(token, utils.CTJSON),
            json= access_request
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["authorise_thing"], http_resp.status_code
            )
        else:
            mf_resp.value = "True"
        return mf_resp
    
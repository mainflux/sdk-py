import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Things:
    things_endpoint = "things"
    connect_endpoint = "connect"
    disconnect_endpoint = "disconnect"
    identify_endpoint = "identify"

    def __init__(self, url: str):
        self.url = url

    def create(self, thing: dict, token: str):
        """Creates thing entity in the database"""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.things_endpoint,
            json=thing,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["create"], http_resp.status_code
            )
        else:
            location = http_resp.headers.get("location")
            mf_resp.value = location.split("/")[2]
        return mf_resp

    def create_bulk(self, things: list, token: str):
        """Creates multiple things in a bulk"""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.things_endpoint + "/bulk",
            json=things,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
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
            self.url + "/" + self.things_endpoint + "/" + thing_id,
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
            self.url + "/" + self.things_endpoint,
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
            self.url + "/channels/" + channel_id + "/" + self.things_endpoint,
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
        http_resp = requests.put(
            self.url + "/" + self.things_endpoint + "/" + thing_id,
            json=thing,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["update"], http_resp.status_code
            )
        return mf_resp

    def delete(self, thing_id: str, token: str):
        """Deletes a thing entity from database"""
        http_resp = requests.delete(
            self.url + "/" + self.things_endpoint + "/" + thing_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["delete"], http_resp.status_code
            )
        return mf_resp

    def connects(self, thing_ids: list, channel_ids: list, token: str):
        """Connects thing and channel"""
        payload = {"channel_ids": channel_ids, "thing_ids": thing_ids}
        http_resp = requests.post(
            self.url + "/" + self.connect_endpoint,
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
        payload = {"thing_ids": thing_ids, "channel_ids": channel_ids}
        http_resp = requests.delete(
            self.url + "/" + self.disconnect_endpoint,
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

    def connect(self, thing_id: str, channel_id: str, token: str):
        """Connects thing and channel"""
        http_resp = requests.put(
            self.url + "/channels/" + channel_id + "/things/" + thing_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["connect"], http_resp.status_code
            )
        else:
            mf_resp.value = "connected"
        return mf_resp

    def disconnect(self, thing_id: str, channel_id: str, token: str):
        """Disconnect thing and channel"""
        http_resp = requests.delete(
            self.url + "/channels/" + channel_id + "/things/" + thing_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["disconnect"], http_resp.status_code
            )
        return mf_resp

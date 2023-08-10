import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Channels:
    channels_endpoint = "channels"
    things_endpoint = "things"
    identify_endpoint = "identify"

    def __init__(self, url: str):
        self.url = url

    def create(self, channel: dict, token: str):
        """Creates channel entity in the database"""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.channels_endpoint,
            json=channel,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["create"], http_resp.status_code
            )
        else:
            location = http_resp.headers.get("location")
            mf_resp.value = location.split("/")[2]
        return mf_resp

    def create_bulk(self, channels: list, token: str):
        """Creates multiple channels in a bulk"""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.channels_endpoint + "/bulk",
            json=channels,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["create_bulk"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get(self, channel_id: str, token: str):
        """Gets a channel entity for a logged-in user"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.channels_endpoint + "/" + channel_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["get"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_all(self, query_params: dict, token: str):
        """Gets all channels from database"""
        url = self.url + "/" + self.channels_endpoint
        mf_resp = response.Response()
        http_resp = requests.get(
            url,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["get_all"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_by_thing(self, thing_id: str, query_params: dict, token: str):
        """Gets all channels to which a specific thing is connected to"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url
            + "/"
            + self.things_endpoint
            + "/"
            + thing_id
            + "/"
            + self.channels_endpoint,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["get_by_thing"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, channel_id: str, channel: dict, token: str):
        """Updates channel entity"""
        http_resp = requests.put(
            self.url + "/" + self.channels_endpoint + "/" + channel_id,
            json=channel,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["update"], http_resp.status_code
            )
        return mf_resp

    def delete(self, channel_id: str, token: str):
        """Deletes a channel entity from database"""
        http_resp = requests.delete(
            self.url + "/" + self.channels_endpoint + "/" + channel_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["delete"], http_resp.status_code
            )
        return mf_resp

    def identify_thing(self, thing_key: str):
        """Validates thing's key and returns it's ID if key is valid"""
        http_resp = requests.post(
            self.url + "/" + self.identify_endpoint, json={"token": thing_key}
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["get_by_thing"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

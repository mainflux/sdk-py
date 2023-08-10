import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Keys:
    keys_endpoint = "keys"

    def __init__(self, url: str):
        self.url = url

    def issue(self, duration: str, token: str):
        """Generates a new API key"""
        payload = {"type": 2, "duration": duration}
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.keys_endpoint,
            json=payload,
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

    def get_key_details(self, key_id: str, token: str):
        """Gets API key details for the given key"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.keys_endpoint + "/" + key_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["create"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def revoke(self, key_id: str, token: str):
        """Revoke API key identified by the given ID."""
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.url + "/" + self.keys_endpoint + "/" + key_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["delete"], http_resp.status_code
            )
        return mf_resp

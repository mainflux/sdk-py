import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Certs:
    certs_endpoint = "configs"

    def __init__(self, url: str):
        self.url = url

    def issue(
        self, thing_id: str, key_bits: int, key_type: str, valid: str,
            token: str
    ):

        payload = {
            "thing_id": thing_id,
            "key_bits": key_bits,
            "key_type": key_type,
            "ttl": valid,
        }
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.certs_endpoint,
            json=payload,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.certs["issue"], http_resp.status_code
            )
        else:
            location = http_resp.headers.get("location")
            mf_resp.value = location.split("/")[2]
        return mf_resp

    def view(self, thing_id: str, token: str):
        """Generates an access token when provided with proper credentials."""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.certs_endpoint + "/" + thing_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.certs["view"], http_resp.status_code
            )
        return mf_resp

    def revoke(self, thing_id: str, token: str):

        mf_resp = response.Response()
        http_resp = requests.delete(
            self.url + "/" + self.certs_endpoint + "/" + thing_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.certs["revoke"], http_resp.status_code
            )
        return mf_resp

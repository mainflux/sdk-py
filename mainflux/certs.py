import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Certs:
    certs_endpoint = "certs"

    def __init__(self, url: str):
        self.url = url

    def issue(self, thing_id: str, valid: str, token: str):

        payload = {
            "thing_id": thing_id,
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
            mf_resp.value = http_resp.json()
        return mf_resp

    def view_by_thing(self, thing_id: str, token: str):
        """Retrieves a list of certificates' serial IDs for a given thing ID."""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/serials" + "/" + thing_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.certs["view_by_thing"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
    
    def view_by_serial(self, cert_id: str, token: str):
        """Retrieves a certificate for a given cert ID."""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.certs_endpoint + "/" + cert_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        print(http_resp.url)
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.certs["view_by_serial"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
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
        else:
            mf_resp.value = "DELETED"
        return mf_resp

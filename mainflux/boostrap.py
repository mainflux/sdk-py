import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Bootstrap:
    configs_endpoint = "configs"
    bootstrap_endpoint = "bootstrap"
    whitelist_endpoint = "state"
    bootstrap_certs_endpoint = "configs/certs"

    def __init__(self, url: str):
        self.url = url

    def add(self, config: dict, token: str):
        """Adds new config to the list of config owned by user identified
        using the provided access token."""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.configs_endpoint,
            json=config,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.boostrap["add"], http_resp.status_code
            )
        else:
            location = http_resp.headers.get("location")
            mf_resp.value = location.split("/")[2]
        return mf_resp

    def whitelist(self, config: dict, token: str):
        """Updating state represents enabling/disabling Config,
        i.e.connecting and disconnecting corresponding Mainflux Thing to the
        list of Channels."""
        mf_resp = response.Response()
        if config["MFThing"] == "":
            mf_resp.error.status = 1
            mf_resp.error.message = "parameter not found in the query"
        http_resp = requests.put(
            self.url + "/" + self.whitelist_endpoint + "/" + config["MFThing"],
            json=config,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.boostrap["whitelist"], http_resp.status_code
            )
        return mf_resp

    def view(self, config_id: str, token: str):
        """Retrieves a configuration with given config id"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.configs_endpoint + "/" + config_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.boostrap["view"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, config: dict, token: str):
        """Update is performed by replacing the current resource data with
        values provided in a request payload. Note that the owner, ID,
        external ID, external key, Mainflux Thing ID and key cannot be
        changed."""
        mf_resp = response.Response()
        if config["MFThing"] == "":
            mf_resp.error.status = 1
            mf_resp.error.message = "parameter not found in the query"
        http_resp = requests.put(
            self.url + "/" + self.configs_endpoint + "/" + config["MFThing"],
            headers=utils.construct_header(token, utils.CTJSON),
            data=config,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.boostrap["update"], http_resp.status_code
            )
        return mf_resp

    def update_certs(
        self, config_id: str, client_cert: str, client_key: str, ca: str,
            token: str
    ):
        """Update is performed by replacing the current certificate data
        with values provided in a request payload."""
        payload = {"client_cert": client_cert,
                   "client_key": client_key, "ca_cert": ca}
        http_resp = requests.patch(
            self.url + "/" + self.bootstrap_certs_endpoint + "/" + config_id,
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.boostrap["update"], http_resp.status_code
            )
        return mf_resp

    def remove(self, config_id: str, token: str):
        """Removes a Config. In case of successful removal the service will
        ensure that the removed config is disconnected from all the
        Mainflux channels."""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.configs_endpoint + "/" + config_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.boostrap["remove"], http_resp.status_code
            )
        return mf_resp

    def bootstrap(self, external_id: str, external_key: str):
        """Retrieves a configuration with given external ID and external
        key."""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.bootstrap_endpoint + "/" + external_id,
            headers=utils.construct_header(external_key, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.boostrap["bootstrap"], http_resp.status_code
            )
        return mf_resp

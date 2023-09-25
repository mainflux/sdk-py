import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Bootstrap:
    """Bootstrap service API client.
    
    Bootstrap service is used to manage configurations for Mainflux Things. It provides 
    services such as updating, viewing, removing and adding new configurations.
    
    Attributes:
        url (str): Mainflux Bootstrap API URL.
        CONFIGS_ENDPOINT (str): Configurations API endpoint.
        BOOTSTRAP_ENDPOINT (str): Bootstrap API endpoint.
        WHITELIST_ENDPOINT (str): Whitelist API endpoint.
        BOOTSTRAP_CERTS_ENDPOINT (str): Bootstrap certificates API endpoint.
        
    """
    CONFIGS_ENDPOINT = "configs"
    BOOTSTRAP_ENDPOINT = "bootstrap"
    WHITELIST_ENDPOINT = "things/state"
    BOOTSTRAP_CERTS_ENDPOINT = "configs/certs"

    def __init__(self, url: str):
        """Initializes Bootstrap with the provided URL.
        
        params:
            url (str): Mainflux Bootstrap API URL.
            
        returns:
            Bootstrap: Bootstrap object.
            
        raises: 
            None
        """
        self.url = url

    def add(self, config: dict, token: str):
        """Adds new config to the list of config owned by user identified
        using the provided access token.
        
        Some of the key data needed include the external_key and external_id which must be
        specific to the thing provided with the thing_id.
        
        params:
            config (dict): Configuration data for example: 
                {  
                    "external_id": "123",
                    "external_key": "456",
                    "thing_id": "fdb1057c-2905-4f71-9a80-e0ce9191e667",
                    "name": "thing_name"
                }
            token (str): Authorization token.
            
        returns:
            mf_response : response.Response.
            
        Usage:
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(bootstrap_url="http://localhost:9013")
            >>> config = {
            ... "external_id": "123",
            ... "external_key": "456",
            ... "thing_id": "fdb1057c-2905-4f71-9a80-e0ce9191e667",
            ... "name": "thing_name"
            ... }
            >>> mf_resp = mfsdk.bootstrap.add(config, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/things" + "/" + self.CONFIGS_ENDPOINT,
            json=config,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.bootstrap["add"], http_resp.status_code
            )
        else:
            mf_resp.value = "Configuration added"
        return mf_resp

    def whitelist(self, config: dict, token: str):
        """Updating state represents enabling/disabling Config,
        i.e.connecting and disconnecting corresponding Mainflux Thing to the
        list of Channels.
        
        params:
            config (dict): Configuration data for example: 
                {  
                    "external_id": "123",
                    "external_key": "456",
                    "thing_id": "fdb1057c-2905-4f71-9a80-e0ce9191e667",
                    "name": "thing_name"
                }
            token (str): Authorization token.
            
        returns:
            mf_response : response.Response.
            
        Usage:
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(bootstrap_url="http://localhost:9013")
            >>> config = {
            ... "external_id": "123",
            ... "external_key": "456",
            ... "thing_id": "fdb1057c-2905-4f71-9a80-e0ce9191e667",
            ... "name": "thing_name"
            ... }
            >>> mf_resp = mfsdk.bootstrap.whitelist(config, token)
            >>> mf_resp        
        """
        mf_resp = response.Response()
        if config["thing_id"] == "":
            mf_resp.error.status = 1
            mf_resp.error.message = "parameter not found in the query"
        http_resp = requests.put(
            self.url + "/" + self.WHITELIST_ENDPOINT + "/" + config["thing_id"],
            json=config,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.bootstrap["whitelist"], http_resp.status_code
            )
        else:
            mf_resp.value = "Configuration Updated"
        return mf_resp

    def view(self, thing_id: str, token: str):
        """Retrieves a configuration with given config id
        
        Provides a configuration with given config id.
        
        params:
            thing_id (str): Thing ID.
            token (str): Authorization token.
            
        returns:
            mf_resp : response.Response - response object.
            
        Usage:
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(bootstrap_url="http://localhost:9013")
            >>> thing_id = "thing_id"
            >>> mf_resp = mfsdk.bootstrap.view(thing_id, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/things" + "/" + self.CONFIGS_ENDPOINT + "/" + thing_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.bootstrap["view"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, config: dict, token: str):
        """Update is performed by replacing the current resource data with
        values provided in a request payload. Note that the owner, ID,
        external ID, external key, Mainflux Thing ID and key cannot be
        changed.
        
        params:
            config (dict): Configuration data for example: 
                {  
                    "external_id": "123",
                    "external_key": "456",
                    "thing_id": "fdb1057c-2905-4f71-9a80-e0ce9191e667",
                    "name": "thing_name"
                }
            token (str): Authorization token.
            
        returns:

            mf_response : response.Response.
            
        Usage:
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(bootstrap_url="http://localhost:9013")
            >>> config = {
            ... "external_id": "123",
            ... "external_key": "456",
            ... "thing_id": "fdb1057c-2905-4f71-9a80-e0ce9191e667",
            ... "name": "thing_name"
            ... }
            >>> mf_resp = mfsdk.bootstrap.update(config, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        if config["thing_id"] == "":
            mf_resp.error.status = 1
            mf_resp.error.message = "parameter not found in the query"
        http_resp = requests.put(
            self.url + "/things/" + self.CONFIGS_ENDPOINT + "/" + config["thing_id"],
            headers=utils.construct_header(token, utils.CTJSON),
            json=config,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.bootstrap["update"], http_resp.status_code
            )
        else:
            mf_resp.value = "Configuration updated."
        return mf_resp

    def update_certs(
        self, config_id: str, client_cert: str, client_key: str, ca: str,
            token: str):
        """Update is performed by replacing the current certificate data
        with values provided in a request payload.
        
        params: 
            config_id (str): Configuration ID.
            client_cert (str): Client certificate.
            client_key (str): Client key.
            ca (str): CA certificate.
            token (str): Authorization token.
            
        returns:
            mf_response : response.Response.
            
        Usage:
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(bootstrap_url="http://localhost:9013")
            >>> config_id = "config_id"
            >>> client_cert = "client_cert"
            >>> client_key = "client_key"
            >>> ca = "ca"
            >>> mf_resp = mfsdk.bootstrap.update_certs(config_id, client_cert, client_key, ca, token)
            >>> mf_resp
        """
        payload = {"client_cert": client_cert,
                   "client_key": client_key, "ca_cert": ca}
        http_resp = requests.patch(
            self.url + "/" + self.BOOTSTRAP_CERTS_ENDPOINT + "/" + config_id,
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.bootstrap["update"], http_resp.status_code
            )
        return mf_resp

    def remove(self, config_id: str, token: str):
        """Removes a Config. In case of successful removal the service will
        ensure that the removed config is disconnected from all the
        Mainflux channels.
        
        params:
            config_id (str): Configuration ID.
            token (str): Authorization token.
            
        returns:
            mf_response : response.Response.
            
        Usage:
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(bootstrap_url="http://localhost:9013")
            >>> config_id = "config_id"
            >>> mf_resp = mfsdk.bootstrap.remove(config_id, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.url + "/things/" + self.CONFIGS_ENDPOINT + "/" + config_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.bootstrap["remove"], http_resp.status_code
            )
        else:
             mf_resp.value = "Configuration removed."
        return mf_resp

    def bootstrap(self, external_id: str, external_key: str):
        """Retrieves a configuration with given external ID and external
        key.
        
        params:
            external_id (str): External ID.
            external_key (str): External key.
            
        returns:
            mf_resp : response.Response - response object.
            
        Usage:

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(bootstrap_url="http://localhost:9013")
            >>> external_id = "external_id"
            >>> external_key = "external_key"
            >>> mf_resp = mfsdk.bootstrap.bootstrap(external_id, external_key)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/things/bootstrap" + "/" + external_id,
            headers=utils.construct_header(utils.ThingPrefix+external_key, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.bootstrap["bootstrap"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

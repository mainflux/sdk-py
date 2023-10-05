import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Channels:
    """Channels class provides the abstraction of the Mainflux Channels API.
    
    Channels are used to connect things and users. They are used to send messages to things and 
    receive messages from things. Channels API provides the following functionalities:
        - create channel
        - create multiple channels in a bulk
        - get channel
        - get all channels
        - get all channels to which a specific thing is connected to
        - update channel
        - delete channel
        - identify thing
        
    Attributes: 
        CHANNELS_ENDPOINT (str): Channels API endpoint
        THINGS_ENDPOINT (str): Things API endpoint
        IDENTIFY_ENDPOINT (str): Identify API endpoint
        
    """
    CHANNELS_ENDPOINT = "channels"
    THINGS_ENDPOINT = "things"
    IDENTIFY_ENDPOINT = "identify"

    def __init__(self, url: str):
        """Initializes Channels class with the provided url

            Args:
                url (str): Mainflux Channels API URL
                
            returns:
                Channels: Channels object initialized with the provided url.
                
            raises:
                None
        """
        self.url = url

    def create(self, channel: dict, token: str):
        """Creates channel entity in the database
        
        Creates a new channel in the database when provided with a valid token.
        
        params:
            channel (dict): Channel entity to be created for example:
                {
                    "name": "channel_name",
                    "metadata": {
                        "description": "channel_description"
                    }
                }
            token (str): User's token
            
        returns:
            Response: Response object containing the response from the server
            
        Usage:
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> channel = {
            ...    "name": "channel_name"
            ... }
            >>> mf_resp = mfsdk.channels.create(channel, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.CHANNELS_ENDPOINT,
            json=channel,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["create"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def create_bulk(self, channels: list, token: str):
        """Creates multiple channels in bulk
        
        Creates multiple new channels when provided with channels information
        and a valid token.
        
        params:
            channels: list- Channel entities to be created for example:
                [
                    {
                        "name": "channel_name",
                        "metadata": {
                            "description": "channel_description"
                        }
                    },
                    {
                        "name": "channel_name",
                        "metadata": {
                            "description": "channel_description"
                        }
                    }
                ]
                
            token (str): User's token
        
        returns:
            Response: Response object containing the response from the server
            
        Usage:
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> channels = [
            ...    {
            ...        "name": "channel_name"
            ...    },
            ...    {
            ...        "name": "channel_name"
            ...    }
            ... ]
            >>> mf_resp = mfsdk.channels.create_bulk(channels, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.CHANNELS_ENDPOINT + "/bulk",
            json=channels,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["create_bulk"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get(self, channel_id: str, token: str):
        """Gets a channel entity for a logged-in user
        
        Provides a channel entity when provided with a valid channel ID and token.
        
        params: 
            channel_id (str): Channel ID
            token (str): User's token
            
        returns:
            Response: Response object
            
        Usage:

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> channel_id = "channel_id"
            >>> mf_resp = mfsdk.channels.get(channel_id, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.CHANNELS_ENDPOINT + "/" + channel_id,
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
        """Gets all channels from database
        
        Gets all channels from database when provided with a valid token..
        
        params:
            query_params (dict): Query parameters for example:
                {
                    "offset": 0,
                    "limit": 10
                }
            token (str): User's token
            
        returns:
            mf_resp: response.Response -response object
            
        Usage:
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> query_params = {
            ...    "offset": 0,
            ...    "limit": 10
            ... }
            >>> mf_resp = mfsdk.channels.get_all(query_params, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.CHANNELS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
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
        """Gets all channels to which a specific thing is connected to.
        
        Provides a list of all the channels a thing is connected to when provided with a valid
        token and thing ID.
        
        params:
            thing_id (str): Thing ID
            query_params (dict): Query parameters for example:
                {
                    "offset": 0,
                    "limit": 10
                }
            token (str): User's token
            
        returns:
            mf_resp: response.Response -response object
            
        Usage:

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> thing_id = "thing_id"
            >>> query_params = {
            ...    "offset": 0,
            ...    "limit": 10
            ... }
            >>> mf_resp = mfsdk.channels.get_by_thing(thing_id, query_params, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.THINGS_ENDPOINT + "/" + thing_id + "/" + self.CHANNELS_ENDPOINT,
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
        """Updates channel entity
        
        Updates a channel entity when provided with a valid channel ID, channel entity and token.
        The information that can be updated are channel's name and metadata.
        
        params:
            channel_id (str): Channel ID
            channel (dict): Channel entity to be updated for example:
                {
                    "name": "channel_name",
                    "metadata": {
                        "description": "channel_description"
                    }
                }
            token (str): User's token
            
        returns:
            mf_resp: response.Response -response object
            
        Usage:

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> channel_id = "channel_id"
            >>> channel = {
            ...    "name": "channel_name"
            ... }
            >>> mf_resp = mfsdk.channels.update(channel_id, channel, token)
            >>> mf_resp
        """
        http_resp = requests.put(
            self.url + "/" + self.CHANNELS_ENDPOINT + "/" + channel_id,
            json=channel,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["update"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disable(self, channel_id: str, token: str):
        """Deletes a channel entity from database.
        
        Deletes a channel entity from database when provided with a valid channel ID and token.
        The channel is not deleted from the database but is marked as disabled.
        
        params:

            channel_id (str): Channel ID
            token (str): User's token
            
        returns:

            mf_resp: response.Response -response object
            
        Usage:
            
                >>> from mainflux import sdk
                >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
                >>> channel_id = "channel_id"
                >>> mf_resp = mfsdk.channels.disable(channel_id, token)
                >>> mf_resp
        """
        http_resp = requests.post(
            self.url + "/" + self.CHANNELS_ENDPOINT + "/" + channel_id + "/disable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["delete"], http_resp.status_code
            )
        return mf_resp

    def identify_thing(self, thing_key: str):
        """Validates thing's key and returns it's ID if key is valid
        
        Uses a thing_key or secret to validate a thing and provide its information.
        
        params:
            thing_key (str): Thing's key
            
        returns:
            mf_resp: response.Response -response object
            
        Usage:
        
            >>> from mainflux import sdk    
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> thing_key = "thing_key"
            >>> mf_resp = mfsdk.channels.identify_thing(thing_key)
            >>> mf_resp
        """
        http_resp = requests.post(
            self.url + "/" + self.IDENTIFY_ENDPOINT,
            headers=utils.construct_header(utils.ThingPrefix + thing_key, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["identify_thing"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

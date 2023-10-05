import requests
from mainflux import response
from mainflux import errors
from mainflux import utils


class Things:
    """Things API client.
    
    Things API is used for creating and managing things.
    It is used for creating new things, creating multiple things
    getting thing information, updating thing information, disabling 
    and enabling things ,and connecting and disconnecting things.
    
    Attributes:
        URL: str - URL of the Things API
        THINGS_ENDPOINT: str - Things API endpoint
    """
    THINGS_ENDPOINT = "things"

    def __init__(self, url: str):
        self.URL = url
    """Initializes Things API client.
        
        params:
            url: str - URL of the Things API
        
        returns:
            Thigs: Things - Things API client
            
        raises:
            None
    """
    def create(self, thing: dict, token: str):
        """Creates thing entity in the database.
                
        Creates a new thing with provided thing information.
        If token is provided, it will be used to create a new thing

        params:
            thing: dict - thing information for example:
            {
                "name": "thing1"
            }
            token: str - token used for creating a new thing
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing = {
            ...     "name": "thing1",
            ...  }
            >>> mf_resp = mfsdk.things.create(thing)
            >>> mf_resp            
        """
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
        """Creates multiple things in bulk.
                
        Creates multiple new things with provided things information.
        If a token is provided, it will be used to create the new things.

        params:
            things: list - a list of things with theri information for example:
                [
                    {"name": "thing2"}, 
                    {"name": "thing3"}, 
                    {"name": "thing4"}
                ]
            token: str - token used for creating the new things.
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> things = [
            ...     {"name": "thing2"}, 
            ...     {"name": "thing3"}, 
            ...     {"name": "thing4"}
            ... ]
            >>> mf_resp = mfsdk.things.create_bulk(things)
            >>> mf_resp            
        """
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
        """Gets a thing entity.
        
        Provides information about a thing with provided thing ID and token.
        Information about a thing is provided in a JSON format and includes the name
        its owner, secret,tags and status.
        
        params:
            thing_id: str - ID of the thing
            token: str - token used for getting thing information
        
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
                
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> mf_resp = mfsdk.things.get(thing_id)
            >>> mf_resp        
        """
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
        """Gets all things from database.
        
        Provides information about all things in a JSON format. It is controlled
        by a set of query parameters and a valid token.
        
        params:
            query_params: dict - query parameters for example:
                {
                    "offset": 0,
                    "limit": 10
                }
                where offset is the number of things to skip and limit is the maximum
            token: str - token used for getting all things information
        
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
                    
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> query_params = {
            ...     "offset": 0,
            ...     "limit": 10
            ... }
            >>> mf_resp = mfsdk.things.get_all(query_params)
            >>> mf_resp        
        """
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
        """Gets all things to which a specific thing is connected to.
        
        Provides a list of all things that are connected to a specific channel when
        given a channel ID and valid token.
        
        params:
            channel_id: str - ID of the channel
            query_params: dict - query parameters for example:
                {
                    "offset": 0,
                    "limit": 10
                }
                where offset is the number of things to skip and limit is the maximum
            token: str - token used for getting all things information
        
        returns:    
            mf_resp: response.Response - response object.
            
        Usage::
                        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> query_params = {
            ...     "offset": 0,
            ...     "limit": 10
            ... }
            >>> mf_resp = mfsdk.things.get_by_channel(channel_id, query_params)
            >>> mf_resp        
        """
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
        """Updates thing entity.
        
        Allows a logged in user to make changes and update a thing's
        information with provided thing ID and valid token. Information 
        such as the metadata and name can be updated. 
        
        params:
            thing_id: str - ID of the thing
            thing: dict - thing information for example:
                {
                    "name": "thing1"
                }
            token: str - token used for updating thing information 
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
                                
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> thing = {
            ...     "name": "thing2",
            ...  }
            >>> mf_resp = mfsdk.things.update(thing_id, thing)
            >>> mf_resp            
        """
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
        """Updates thing secret.
        
        Allows a logged in user to make changes and update a thing's
        information with provided thing ID and valid token. The thing's 
        secret can be updated.
        
        params:
            thing_id: str - ID of the thing
            thing: dict - thing information for example:
                {
                    "key": "thing1"
                }
            token: str - token used for updating thing information
            
        returns:
            mf_resp: response.Response - response object.
        
        Usage::

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> thing = {
            ...     "key": "thing2",
            ...  }
            >>> mf_resp = mfsdk.things.update_thing_secret(thing_id, thing)
            >>> mf_resp
        """
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
        """Updates thing tags.
        
        Allows a logged in user to make changes and update a thing's
        information with provided thing ID and valid token. The thing's
        tags can be updated.
        
        params:
            thing_id: str - ID of the thing
            thing: dict - thing information for example:
                {
                    "tags": ["tag1", "tag2"]
                }
            token: str - token used for updating thing information
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
        
            >>> from mainflux import sdk   
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> thing = {
            ...     "tags": ["tag1", "tag2"]
            ...  }
            >>> mf_resp = mfsdk.things.update_thing_tags(thing_id, thing)
            >>> mf_resp
        """
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
        """Updates thing owner.
        
        Allows a logged in user to make changes and update a thing's
            information with provided thing ID and valid token. The thing
            owner can be updated.
        
        params:
            thing_id: str - ID of the thing
            thing: dict - thing information for example:
                {
                    "owner": "user1"
                }
            token: str - token used for updating thing information
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> thing = {
            ...     "owner": "user1"
            ...  }
            >>> mf_resp = mfsdk.things.update_thing_owner(thing_id, thing)
            >>> mf_resp
        """
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
        """Deletes a thing entity from the database.
        
        Deletes a thing with provided thing ID and valid token.
        
        params:
            thing_id: str - ID of the thing
            token: str - token used for deleting thing
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
                        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> mf_resp = mfsdk.things.disable(thing_id)
            >>> mf_resp        
        """
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
        """Connects things and channels. 
        
        Connects multiple things and channels with provided thing IDs 
        as the subjects, channel IDs as the objects, actions that the 
        thing can partake in and a valid token.
        
        params:
            thing_ids: list - list of thing IDs
            channel_ids: list - list of channel IDs
            actions: list - list of actions for example: 
                ["m_write", "m_read"]
            token: str - token used for connecting things and channels
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]
            >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]
            >>> actions = ["m_write", "m_read"]
            >>> mf_resp = mfsdk.things.connects(thing_ids, channel_ids, actions)
            >>> mf_resp            
        """
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
        """Disconnect things and channels.
        
        Disconnects multiple things and channels with provided thing IDs 
        as the subjects, channel IDs as the objects and a valid token.
        
        params:
            thing_ids: list - list of thing IDs
            channel_ids: list - list of channel IDs
            token: str - token used for disconnecting things and channels
        
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]
            >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]
            >>> mf_resp = mfsdk.things.disconnects(thing_ids, channel_ids)
            >>> mf_resp
        """
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
        """Connects thing and channel.
        
        Connects a thing and channel with provided thing ID as the subject,
        channel ID as the object, action that the thing can partake in and a
        valid token.
        
        params:
            thing_id: str - ID of the thing
            channel_id: str - ID of the channel
            action: str - action for example: "m_write"
            token: str - token used for connecting thing and channel
            
        returns:
            mf_resp: "connected"
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> action = "m_write"
            >>> mf_resp = mfsdk.things.connect(thing_id, channel_id, action)
            >>> mf_resp
        """
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
        """Disconnects thing and channel.
        
        Disconnects a thing and channel with provided thing ID as the subject,  
        channel ID as the object and a valid token.
        
        params:
            thing_id: str - ID of the thing
            channel_id: str - ID of the channel
            token: str - token used for disconnecting thing and channel
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> mf_resp = mfsdk.things.disconnect(thing_id, channel_id)
            >>> mf_resp
        """
        payload = {"subject": thing_id, "object": channel_id}
        http_resp = requests.delete(
            self.URL + "/policies" + "/" + thing_id + "/" + channel_id,
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["disconnect"], http_resp.status_code
            )
        else:
            mf_resp.value = "Disconnected"
        return mf_resp
    
    def share_thing(self, user_id: str, channel_id: str, actions: list, token: str):
        """Shares thing.
        
        Allows a logged in user to create new policies for a thing over a channel
        provided with a user ID, channel ID, actions that the thing can partake in
        and a valid token.
        
        params:
            user_id: str - ID of the user
            channel_id: str - ID of the channel
            actions: list - list of actions for example: 
                ["m_write", "m_read"]
            token: str - token used for sharing thing
            
        returns:
            mf_resp: "OK"
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> user_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> actions = ["m_write", "m_read"]
            >>> mf_resp = mfsdk.things.share_thing(user_id, channel_id, actions)
            >>> mf_resp
        """
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
        """Authorises thing.
        
        Creates policies for a thing as a subject over a channel which is the object. 
        It authorizes the thing to perform some actions over the channel.
        
        params:
        
            access_request: dict - access request information for example:
                {
                    "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",
                    "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",
                    "actions": "m_write"
                    "entity_type": "group"
                }
            token: str - token used for authorising thing
            
        returns:
            mf_resp: "True"
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(things_url="http://localhost:9000")
            >>> access_request = {
            ...     "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",
            ...     "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",
            ...     "actions": "m_write"
            ...     "entity_type": "group"
            ... }
            >>> mf_resp = mfsdk.things.authorise_thing(access_request)
            >>> mf_resp
        """
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

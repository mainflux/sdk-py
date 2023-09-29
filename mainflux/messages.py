import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Messages:
    """Messages API client
    
    Messages API client enables interaction with Mainflux Messages API.
    It provides methods for sending and reading messages.
    
    Attributes:
        adapter_url: URL of the Mainflux Messages adapter
        reader_url: URL of the Mainflux Messages reader
    """
    def __init__(self, adapter_url: str, reader_url: str):
        self.adapter_url = adapter_url
        self.reader_url = reader_url
        """Initializes Messages API client with adapter and reader URLs
        
        params:
            adapter_url: URL of the Mainflux Messages adapter
            reader_url: URL of the Mainflux Messages reader
            
        returns:
            Messages API client object
            
        raises:
            None
        """
    def send(self, channel_id: str, msg: str, thing_key: str):
        """Sends message via HTTP protocol
        
        Sends message to a given channel via HTTP protocol. Message is sent
        through a writer add-on such as timescale. Message is sent to a
        http port specific to the writer add-on. The thing and channel must be
        created before sending the message and connected. 
        
        params:
            channel_id: ID of the channel to send message to
            msg: message to send to the channel that should be in bytes
            thing_key: secret of the thing sending the message
        
        returns:
            mf_resp: response object
            
        usage:

            >>> from mainflux import sdk
            >>> mfsdk = sdk.Sdk("http://localhost:9011")
            >>> channel_id = "2b86beba-83dd-4b39-8165-4dda4e6eb4ad"
            >>> msg = '[{"bn":"demo", "bu":"V", "n":"voltage", "u":"V", "v":5}]'
            >>> thing_key = "fc68b31b-d7fd-4879-b3a7-0baf4580c5b1"
            >>> mf_resp = mfsdk.messages.send(channel_id, msg, thing_key)
            >>> mf_resp
        """
        chan_name_parts = channel_id.split(".", 2)
        chan_id = chan_name_parts[0]
        subtopic = ""
        if len(chan_name_parts) == 2:
            subtopic = chan_name_parts[1].replace(".", "/", -1)
        mf_resp = response.Response()
        http_resp = requests.post(
            self.adapter_url + "/http/channels/" + chan_id + "/messages/" +
            subtopic,
            data=bytes(msg, 'utf-8'),
            headers=utils.construct_header(
                utils.ThingPrefix + thing_key, utils.CTJSON),
        )
        print(http_resp)
        if http_resp.status_code != 202:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.messages["send"], http_resp.status_code
            )
        return mf_resp

    def read(self, channel_id: str, token: str):
        """Reads messages from database for a given channel
        
        Reads message from a given channel via HTTP protocol. Message is read
        through a reader add-on such as timescale.
        
        params:
            channel_id: ID of the channel to read message from
            token: token of the user reading the message
        
        returns:
            mf_resp: response object
            
        usage:

            >>> from mainflux import sdk
            >>> mfsdk = sdk.Sdk("http://localhost:9011")
            >>> channel_id = "2b86beba-83dd-4b39-8165-4dda4e6eb4ad"
            >>> mf_resp = mfsdk.messages.read(channel_id, token)
            >>> mf_resp
        """
        chan_name_parts = channel_id.split(".", 2)
        chan_id = chan_name_parts[0]
        subtopic = ""
        if len(chan_name_parts) == 2:
            subtopic = chan_name_parts[1].replace(".", "/", -1)
        mf_resp = response.Response()
        http_resp = requests.get(
            self.reader_url + "/channels/" + chan_id + "/messages",
            headers=utils.construct_header(token, utils.CTJSON),
            params={"subtopic": subtopic},
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.messages["read"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

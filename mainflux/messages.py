import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Messages:
    def __init__(self, adapter_url: str, reader_url: str):
        self.adapter_url = adapter_url
        self.reader_url = reader_url

    def send(self, channel_id: str, msg: dict, thing_key: str):
        """Sends message via HTTP protocol"""
        chan_name_parts = channel_id.split(".", 2)
        chan_id = chan_name_parts[0]
        subtopic = ""
        if len(chan_name_parts) == 2:
            subtopic = chan_name_parts[0].replace(".", "/", -1)
        mf_resp = response.Response()
        http_resp = requests.post(
            self.adapter_url + "/http/channels/" + chan_id + "/messages/" +
            subtopic,
            json=msg,
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
        """Reads messages from database for a given channel"""
        chan_name_parts = channel_id.split(".", 2)
        chan_id = chan_name_parts[0]
        subtopic = ""
        if len(chan_name_parts) == 2:
            subtopic = chan_name_parts[0].replace(".", "/", -1)
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

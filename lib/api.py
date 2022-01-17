import requests

from lib import response
from lib import errors


class Keys:
    def __init__(self, url):
        self.url = url

    def create(self, user_token, duration_params):
        '''Generates a new API key'''
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/keys",
            json=duration_params,
            headers={"Authorization": user_token}
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["create"], http_resp.status_code)
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_key_details(self, user_token, key_id):
        '''Gets API key details for the given key'''
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/keys/" + key_id,
            headers={"Authorization": user_token}
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["create"], http_resp.status_code)
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def revoke(self, user_token, key_id):
        '''Revoke API key identified by the given ID.'''
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.url + "/keys/" + key_id,
            headers={"Authorization": user_token}
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.things["delete"], http_resp.status_code)
        return mf_resp

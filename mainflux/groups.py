import requests

from mainflux import response
from mainflux import errors
from mainflux import utils


class Groups:
    groups_endpoint = "groups"

    def __init__(self, url: str):
        self.url = url

    def create(self, group: dict, token: str):
        """Creates group entity in the database"""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.groups_endpoint,
            json=group,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["create"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get(self, group_id: str, token: str):
        """Gets a group entity"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.groups_endpoint + "/" + group_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["get"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_all(self, query_params: dict, token: str):
        """Gets all groups from database"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.groups_endpoint,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["get_all"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def parents(self, group_id: str, query_params: dict, token: str):
        """Gets parents for a specific group from database"""
        mf_resp = response.Response()

        http_resp = requests.get(
            self.url + "/" + self.groups_endpoint + "/" + group_id + "/parents",
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["parents"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def children(self, group_id: str, query_params: dict, token: str):
        """Gets children for a specific group from database"""
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.groups_endpoint + "/" + group_id + "/children",
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["get_all"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, group_id: str, group: dict, token: str):
        """Updates group entity"""
        http_resp = requests.put(
            self.url + "/" + self.groups_endpoint + "/" + group_id,
            data=group,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["update"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def members(self, group_id: str, query_params: dict, token: str):
        """Gets members associated with the group specified by id"""
        http_resp = requests.get(
            self.url + "/" + self.groups_endpoint + "/" + group_id + "/members",
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["members"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def memberships(self, member_id: str, query_params: dict, token: str):
        """Get list of members ID's from group"""
        http_resp = requests.get(
            self.url + "/users" + "/" + member_id + "/memberships",
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["memberships"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def assign(self, group_id: str, member_id: str, member_type: list, token: str):
        """Assign"""
        payload = {"object": group_id, "subject": member_id, "actions": member_type}
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/users/policies",
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["assign"], http_resp.status_code
            )
        return mf_resp

    def unassign(self, group_id: str, token: str, members_ids):
        """Unassign"""
        payload = {"Object": group_id, "Subject": members_ids}
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.url + "/users/policies" + "/" + members_ids + "/" + group_id,
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["unassign"], http_resp.status_code
            )
        return mf_resp

    def disable(self, group_id: str, user_token: str):
        """Disables a group entity from database"""
        http_resp = requests.post(
            self.url + "/" + self.groups_endpoint + "/" + group_id + "/disable",
            headers=utils.construct_header(user_token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["disable"], http_resp.status_code
            )
        return mf_resp

import requests
import json

from mainflux import response
from mainflux import errors
from mainflux import utils


class Groups:
    """Groups class provides the abstraction of the Mainflux groups service API.
    
    Groups class provides the following functionality: create, get, get_all, parents, 
    children, update, members, memberships, assign, unassign, disable.
    
    Attributes:
        URL: Mainflux groups service URL.
        GROUPS_ENDPOINT: Mainflux groups service API endpoint.   
    
    """
    GROUPS_ENDPOINT = "groups"

    def __init__(self, url: str):
        self.URL = url
        """Initializes Groups API client with the provided URL.
        
           params:
                url: Mainflux groups service URL.
                
            returns:
                Groups object.
                
            raises:
                None.        
        """
    def create(self, group: dict, token: str):
        """Creates a group entity in the database.
        
        Creates a group entity in the database using the provided group
        object and token.
        
        params:
            group: dict - group information for example:
            {
                "name": "groupName",
            }
            token: str - token used to create a new group.
            
        returns:
            mf_resp: response.Response - response object
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> group = {
            ...     "name": "groupName",
            ... }
            >>> mf_resp = mfsdk.groups.create(group)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.GROUPS_ENDPOINT,
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
        """Gets a group entity
        
        Provides information about a group entity using the provided group_id
        and a token.
        
        params: 
            group_id: str - group id
            token: str - token used to get a group. 
            
        returns:
            mf_resp: response.Response - response object
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> group_id = "group_id"
            >>> mf_resp = mfsdk.groups.get(group_id)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.GROUPS_ENDPOINT + "/" + group_id,
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
        """Gets all groups from database
        
        Gets all groups from database using the provided query_params and token.
        
        params:
            query_params: dict - query parameters for example:
            {
                "offset": 0,
                "limit": 10,
            }
            where offset is the number of items to skip before starting to collect 
            the result set and limit is the numbers of items to return.
            token: str - token used to get all groups.
            
        returns:
            mf_resp: response.Response - response object
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> query_params = {
            ...     "offset": 0,
            ...     "limit": 10,
            ... }
            >>> mf_resp = mfsdk.groups.get_all(query_params)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.GROUPS_ENDPOINT,
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
        """Gets parents for a specific group from database
        
        Provides information about parents for a specific group from database
        when provided with group_id, query_params and token.
        
        params: 
            group_id: str - group id of the child group in question.
            query_params: dict - query parameters for example:
            {
                "offset": 0,
                "limit": 10,
            }
            where offset is the number of items to skip before starting to collect 
            the result set and limit is the numbers of items to return.
            token: str - token used to get parents for a specific group.
            
        returns:
            mf_resp: response.Response - response object
            
        Usage::

            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> group_id = "group_id"
            >>> query_params = {
            ...     "offset": 0,
            ...     "limit": 10,
            ... }
            >>> mf_resp = mfsdk.groups.parents(group_id, query_params)
            >>> mf_resp
        """
        mf_resp = response.Response()

        http_resp = requests.get(
            self.URL + "/" + self.GROUPS_ENDPOINT + "/" + group_id + "/parents",
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
        """Gets children for a specific group from database
        
        Provides information about children for a specific group from database
        when provided with group_id, query_params and token.
        
        params:
            group_id: str - group id of the parent group in question.
            query_params: dict - query parameters for example:
            {
                "offset": 0,
                "limit": 10,
            }
            where offset is the number of items to skip before starting to collect 
            the result set and limit is the numbers of items to return.
            token: str - token used to get children for a specific group.
            
        returns:
            mf_resp: response.Response - response object
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> group_id = "group_id"
            >>> query_params = {
            ...     "offset": 0,
            ...     "limit": 10,
            ... }
            >>> mf_resp = mfsdk.groups.children(group_id, query_params)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.GROUPS_ENDPOINT + "/" + group_id + "/children",
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
        """Updates group entity
        
        Updates a group entity in the database using the provided group_id, 
        group object and token. It updates the group name and metadata.
        
        params:
            group_id: str - group id
            group: dict - group information for example:
            {
                "name": "groupName",
            }
            token: str - token used to update a group.
            
        returns:

            mf_resp: response.Response - response object
            
        Usage::
            
                >>> from mainflux import sdk
                >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
                >>> group_id = "group_id"
                >>> group = {
                ...     "name": "groupName",
                ... }
                >>> mf_resp = mfsdk.groups.update(group_id, group)
                >>> mf_resp
        """
        http_resp = requests.put(
            self.URL + "/" + self.GROUPS_ENDPOINT + "/" + group_id,
            data=json.dumps(group),
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
        """Gets members associated with the group specified by id
        
        Provides information about members associated with the group specified by id
        when provided with group_id, query_params and token.
        
        params: 
            group_id: str - group id
            query_params: dict - query parameters for example:
            {
                "offset": 0,
                "limit": 10,
            }
            where offset is the number of items to skip before starting to collect 
            the result set and limit is the numbers of items to return.
            token: str - token used to get members associated with the group specified by id.
            
        returns:
            mf_resp: response.Response - response object
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> group_id = "group_id"
            >>> query_params = {
            ...     "offset": 0,
            ...     "limit": 10,
            ... }
            >>> mf_resp = mfsdk.groups.members(group_id, query_params)
            >>> mf_resp       
        """
        http_resp = requests.get(
            self.URL + "/" + self.GROUPS_ENDPOINT + "/" + group_id + "/members",
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
        """Retrieves a list of groups the user is connected to
        
        Retrieves a list of groups the user is connected to when provided with
        the users id, query_params and token. 
        
        params: 
            member_id: str - user id
            query_params: dict - query parameters for example:
            {
                "offset": 0,
                "limit": 10,
            }
            where offset is the number of items to skip before starting to collect
            the result set and limit is the numbers of items to return.
            token: str - token used to retrieve a list of groups the user is connected to.
        
        returns:
            mf_resp: response.Response - response object
            
        Usage::
            
                >>> from mainflux import sdk
                >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
                >>> member_id = "member_id"
                >>> query_params = {
                ...     "offset": 0,
                ...     "limit": 10,
                ... }
                >>> mf_resp = mfsdk.groups.memberships(member_id, query_params)
                >>> mf_resp    
        """
        http_resp = requests.get(
            self.URL + "/users" + "/" + member_id + "/memberships",
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
        """Assign
        
        Assigns a member to a group when provided with group_id, member_id, 
        member_type which is their action and a token.
        
        params:
            group_id: str - group id
            member_id: str - member id
            member_type: list - actions the member can perform for example:
                        [
                            "m_read", "m_write", "m_admin" 
                        ]  
            token: str - token used to assign a member to a group.
        
        returns:
            mf_resp: "Policy created"
            
        Usage::
        
            >>> from mainflux import sdk
            >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
            >>> group_id = "group_id"
            >>> member_id = "member_id"
            >>> member_type = [
            ...     "m_read", "m_write", "m_admin"
            ... ]
            >>> mf_resp = mfsdk.groups.assign(group_id, member_id, member_type)
            >>> mf_resp
        """
        payload = {"object": group_id, "subject": member_id, "actions": member_type}
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/users/policies",
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["assign"], http_resp.status_code
            )
        else:
            mf_resp.value = "Policy created"
        return mf_resp

    def unassign(self, group_id: str, token: str, members_ids):
        """Unassign
        
        Deletes a user's policy from over a group when provided with group_id,
        token and members_ids.
        
        params:
            group_id: str - group id
            token: str - token used to delete a user's policy from over a group.
            members_ids: str - member id
            
        returns:
            mf_resp: response.Response - response object
            
        Usage::
                
                    >>> from mainflux import sdk
                    >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
                    >>> group_id = "group_id"
                    >>> members_ids = "members_ids"
                    >>> mf_resp = mfsdk.groups.unassign(group_id, members_ids)
                    >>> mf_resp
        """
        payload = {"Object": group_id, "Subject": members_ids}
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL + "/users/policies" + "/" + members_ids + "/" + group_id,
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
        """Disables a group entity from database
        
        Deletes a group from the database when provided with group_id and 
        user_token.
        
        params:
            group_id: str - group id
            user_token: str - token used to delete a group.
            
        returns:
            mf_resp: response.Response - response object
            
        Usage::
            
                >>> from mainflux import sdk
                >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")
                >>> group_id = "group_id"
                >>> mf_resp = mfsdk.groups.disable(group_id)
                >>> mf_resp
        """
        http_resp = requests.post(
            self.URL + "/" + self.GROUPS_ENDPOINT + "/" + group_id + "/disable",
            headers=utils.construct_header(user_token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.groups["disable"], http_resp.status_code
            )
        return mf_resp

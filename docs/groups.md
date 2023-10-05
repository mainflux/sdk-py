<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `groups`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Groups`
Groups class provides the abstraction of the Mainflux groups service API. 

Groups class provides the following functionality: create, get, get_all, parents,  children, update, members, memberships, assign, unassign, disable. 



**Attributes:**
 
 - <b>`URL`</b>:  Mainflux groups service URL. 
 - <b>`GROUPS_ENDPOINT`</b>:  Mainflux groups service API endpoint.    

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L388"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `assign`

```python
assign(group_id: str, member_id: str, member_type: list, token: str)
```

Assign 

Assigns a member to a group when provided with group_id, member_id,  member_type which is their action and a token. 

params:  group_id: str - group id  member_id: str - member id  member_type: list - actions the member can perform for example:  [  "m_read", "m_write", "m_admin"   ]    token: str - token used to assign a member to a group. 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
``` 

    >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> group_id = "group_id"     >>> member_id = "member_id"     >>> member_type = [     ...     "m_read", "m_write", "m_admin"     ... ]     >>> mf_resp = mfsdk.groups.assign(group_id, member_id, member_type)     >>> mf_resp 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L203"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `children`

```python
children(group_id: str, query_params: dict, token: str)
```

Gets children for a specific group from database 

Provides information about children for a specific group from database when provided with group_id, query_params and token. 

params:  group_id: str - group id of the parent group in question.  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10,  }  where offset is the number of items to skip before starting to collect   the result set and limit is the numbers of items to return.  token: str - token used to get children for a specific group.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
``` 

    >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> group_id = "group_id"     >>> query_params = {     ...     "offset": 0,     ...     "limit": 10,     ... }     >>> mf_resp = mfsdk.groups.children(group_id, query_params)     >>> mf_resp 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(group: dict, token: str)
```

Creates a group entity in the database. 

Creates a group entity in the database using the provided group object and token. 

params:  group: dict - group information for example:  {  "name": "groupName",  }  token: str - token used to create a new group.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
``` 

    >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> group = {     ...     "name": "groupName",     ... }     >>> mf_resp = mfsdk.groups.create(group)     >>> mf_resp 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L471"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(group_id: str, user_token: str)
```

Disables a group entity from database 

Deletes a group from the database when provided with group_id and  user_token. 

params:  group_id: str - group id  user_token: str - token used to delete a group.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```               >>> from mainflux import sdk          >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")          >>> group_id = "group_id"          >>> mf_resp = mfsdk.groups.disable(group_id)          >>> mf_resp 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(group_id: str, token: str)
```

Gets a group entity 

Provides information about a group entity using the provided group_id and a token. 

params:   group_id: str - group id  token: str - token used to get a group.   



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
``` 

    >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> group_id = "group_id"     >>> mf_resp = mfsdk.groups.get(group_id)     >>> mf_resp 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L111"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, token: str)
```

Gets all groups from database 

Gets all groups from database using the provided query_params and token. 

params:  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10,  }  where offset is the number of items to skip before starting to collect   the result set and limit is the numbers of items to return.  token: str - token used to get all groups.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
``` 

    >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> query_params = {     ...     "offset": 0,     ...     "limit": 10,     ... }     >>> mf_resp = mfsdk.groups.get_all(query_params)     >>> mf_resp 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L294"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `members`

```python
members(group_id: str, query_params: dict, token: str)
```

Gets members associated with the group specified by id 

Provides information about members associated with the group specified by id when provided with group_id, query_params and token. 

params:   group_id: str - group id  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10,  }  where offset is the number of items to skip before starting to collect   the result set and limit is the numbers of items to return.  token: str - token used to get members associated with the group specified by id.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
``` 

    >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> group_id = "group_id"     >>> query_params = {     ...     "offset": 0,     ...     "limit": 10,     ... }     >>> mf_resp = mfsdk.groups.members(group_id, query_params)     >>> mf_resp        

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L341"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `memberships`

```python
memberships(member_id: str, query_params: dict, token: str)
```

Retrieves a list of groups the user is connected to 

Retrieves a list of groups the user is connected to when provided with the users id, query_params and token.  

params:   member_id: str - user id  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10,  }  where offset is the number of items to skip before starting to collect  the result set and limit is the numbers of items to return.  token: str - token used to retrieve a list of groups the user is connected to. 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```               >>> from mainflux import sdk          >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")          >>> member_id = "member_id"          >>> query_params = {          ...     "offset": 0,          ...     "limit": 10,          ... }          >>> mf_resp = mfsdk.groups.memberships(member_id, query_params)          >>> mf_resp     

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parents`

```python
parents(group_id: str, query_params: dict, token: str)
```

Gets parents for a specific group from database 

Provides information about parents for a specific group from database when provided with group_id, query_params and token. 

params:   group_id: str - group id of the child group in question.  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10,  }  where offset is the number of items to skip before starting to collect   the result set and limit is the numbers of items to return.  token: str - token used to get parents for a specific group.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
``` 

    >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> group_id = "group_id"     >>> query_params = {     ...     "offset": 0,     ...     "limit": 10,     ... }     >>> mf_resp = mfsdk.groups.parents(group_id, query_params)     >>> mf_resp 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L434"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unassign`

```python
unassign(group_id: str, token: str, members_ids)
```

Unassign 

Deletes a user's policy from over a group when provided with group_id, token and members_ids. 

params:  group_id: str - group id  token: str - token used to delete a user's policy from over a group.  members_ids: str - member id  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```                        >>> from mainflux import sdk              >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")              >>> group_id = "group_id"              >>> members_ids = "members_ids"              >>> mf_resp = mfsdk.groups.unassign(group_id, members_ids)              >>> mf_resp 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L250"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(group_id: str, group: dict, token: str)
```

Updates group entity 

Updates a group entity in the database using the provided group_id,  group object and token. It updates the group name and metadata. 

params:  group_id: str - group id  group: dict - group information for example:  {  "name": "groupName",  }  token: str - token used to update a group.  



**returns:**
 


 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```               >>> from mainflux import sdk          >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")          >>> group_id = "group_id"          >>> group = {          ...     "name": "groupName",          ... }          >>> mf_resp = mfsdk.groups.update(group_id, group)          >>> mf_resp 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

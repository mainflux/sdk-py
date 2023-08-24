<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `groups`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Groups`




<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `assign`

```python
assign(group_id: str, members_ids: str, member_type: dict, token: str)
```

Assign 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `children`

```python
children(group_id: str, query_params: dict, token: str)
```

Gets children for a specific group from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(group: dict, token: str)
```

Creates group entity in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L184"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(group_id: str, user_token: str)
```

Disables a group entity from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(group_id: str, token: str)
```

Gets a group entity 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, token: str)
```

Gets all groups from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `members`

```python
members(group_id: str, query_params: dict, token: str)
```

Get list of members ID's from group 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `memberships`

```python
memberships(member_id: str, query_params: dict, token: str)
```

Get list of members ID's from group 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parents`

```python
parents(group_id: str, query_params: dict, token: str)
```

Gets parents for a specific group from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L198"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `share_groups`

```python
share_groups(token: str, user_group_id: str, thing_group_id: str)
```

Adds access rights on thing groups to the user group 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unassign`

```python
unassign(group_id: str, token: str, members_ids)
```

Unassign 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(group_id: str, group: dict, token: str)
```

Updates group entity 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

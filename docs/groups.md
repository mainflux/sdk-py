<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `groups`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Groups`




<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `assign`

```python
assign(group_id: str, member_id: str, member_type: list, token: str)
```

Assign 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `children`

```python
children(group_id: str, query_params: dict, token: str)
```

Gets children for a specific group from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(group: dict, token: str)
```

Creates group entity in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(group_id: str, user_token: str)
```

Disables a group entity from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(group_id: str, token: str)
```

Gets a group entity 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, token: str)
```

Gets all groups from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `members`

```python
members(group_id: str, query_params: dict, token: str)
```

Get list of members ID's from group 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `memberships`

```python
memberships(member_id: str, query_params: dict, token: str)
```

Get list of members ID's from group 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parents`

```python
parents(group_id: str, query_params: dict, token: str)
```

Gets parents for a specific group from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unassign`

```python
unassign(group_id: str, token: str, members_ids)
```

Unassign 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(group_id: str, group: dict, token: str)
```

Updates group entity 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

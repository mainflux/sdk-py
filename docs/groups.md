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

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L148"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `assign`

```python
assign(group_id: str, members_ids, member_type: str, token: str)
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

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(group: dict, token: str)
```

Creates group entity in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete(group_id: str, token: str)
```

Deletes a group entity from database 

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

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parents`

```python
parents(group_id: str, query_params: dict, token: str)
```

Gets parents for a specific group from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L196"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `share_groups`

```python
share_groups(token: str, user_group_id: str, thing_group_id: str)
```

Adds access rights on thing groups to the user group 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L165"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unassign`

```python
unassign(group_id: str, token: str, members_ids)
```

Assign 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/groups.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(group_id: str, group: dict, token: str)
```

Updates group entity 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

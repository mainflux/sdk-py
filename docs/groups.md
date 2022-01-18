<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `groups`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Groups`




<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `assign`

```python
assign(group_id, token, members)
```

Assign 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `construct_query`

```python
construct_query(params)
```





---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(group, token)
```

Creates group entity in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete(group_id, token)
```

Deletes a group entity from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(group_id, token)
```

Gets a group entity 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(group_id, token, query_params=None)
```

Gets all groups from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `members`

```python
members(group_id, token)
```

Get list of members ID's from group 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `share_groups`

```python
share_groups(token, user_group_id, thing_group_id)
```

Adds access rights on thing groups to the user group 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unassign`

```python
unassign(group_id, token, members)
```

Assign 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/groups.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(group_id, token, group)
```

Updates group entity 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

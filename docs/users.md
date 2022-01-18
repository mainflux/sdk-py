<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/users.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `users`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/users.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Users`




<a href="https://github.com/mainflux/sdk-py/blob/main/lib/users.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/users.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(user)
```

Creates user entity in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/users.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(user_id, token)
```

Gets a user entity for a logged-in user 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/users.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(token)
```

Gets all users from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/users.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `login`

```python
login(user)
```

Creates a user token 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/users.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(user, token)
```

Updates user entity 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/users.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_password`

```python
update_password(old_password, password, token)
```

Changes user password 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

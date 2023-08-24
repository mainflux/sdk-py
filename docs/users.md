<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `users`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Users`




<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L248"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `authorise_user`

```python
authorise_user(access_request: dict, token: str)
```

Authorises user 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(user: dict, token: str = '')
```

Registers new user account given email and password. New account will be uniquely identified by its email address. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L232"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(user_id: str, user_token: str)
```

Disables an enabled user account for a given user ID. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable`

```python
enable(user_id: str, user_token: str)
```

Enables a disabled user account for a given user ID. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(user_id: str, token: str)
```

Gets a user information 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, user_token: str)
```

Retrieves a list of users 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `login`

```python
login(user: dict)
```

Generates an access token when provided with proper credentials. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `refresh_token`

```python
refresh_token(user: dict, token: str)
```

Refreshes Access and Refresh Token used for authenticating into the system. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset_password`

```python
reset_password(password: str, confirm_password: str, token: str)
```

Changes user password with the reset_request token 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset_password_request`

```python
reset_password_request(email: str, url: str)
```

User Password reset request 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(user: dict, user_token: str)
```

Updates info on currently logged in user. Info is updated using authorization user_token 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_password`

```python
update_password(old_secret: str, new_secret: str, user_token: str)
```

Changes user password 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_user_identity`

```python
update_user_identity(user: dict, user_token: str)
```

Updates Identity of the user 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_user_owner`

```python
update_user_owner(user: dict, user_token: str)
```

Updating user tags in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_user_tags`

```python
update_user_tags(user: dict, user_token: str)
```

Updating user tags in the database 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

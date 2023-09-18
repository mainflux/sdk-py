<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `users`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Users`
Users API client. 

Users API is used for creating and managing users. It is used for creating new users, logging in, refreshing tokens, getting user information, updating user information, disabling  and enabling users. 



**Attributes:**
 
 - <b>`URL`</b>:  str - URL of the Users API 
 - <b>`USERS_ENDPOINT`</b>:  str - Users API endpoint 

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L647"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `authorise_user`

```python
authorise_user(access_request: dict, token: str)
```

Authorises user 

Creates policies for a user as a subject over a group which is the object.  It authorizes the User to perform some actions over the group.  

params:  access_request = {  "subject": "<user_id>",  "object": "<group_id>",  "action": "<action>",  "entity_type": "<entity_type>"  }  token: strOnly admin can use this endpoint. Therefore, you need   an authentication token for the admin. Also, only policies   defined on the system are allowed to add.  



**returns:**
 
 - <b>`mf_resp`</b>:  "True" 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user_id= "886b4266-77d1-4258-abae-2931fb4f16de"     >>> mf_resp = mfsdk.users.authorise_user(user)     >>> mf_resp             

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(user: dict, token: str = '')
```

Creates a new user. 

Creates a new user with provided user information. If token is provided, it will be used to create a new user. 

params:  user: dict - user information for example:  

 {  "name": "example",  "credentials": {  "identity": "example@main.com",  "secret": "12345678"  }  }  token: str - token used for creating a new user  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user = {     ...     "name": "example",     ...     "credentials": {     ...         "identity": "example@mail.com",     ...         "secret": "12345678"     ...     }     ... }     >>> mf_resp = mfsdk.users.create(user)     >>> mf_resp             

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L615"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(user_id: str, user_token: str)
```

Disables an enabled user account for a given user ID.  

params:  user_id: str - the user's given ID.  token: str - token used for enabling a user  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user_id= "886b4266-77d1-4258-abae-2931fb4f16de"     >>> mf_resp = mfsdk.users.disable(user)     >>> mf_resp             

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L581"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable`

```python
enable(user_id: str, user_token: str)
```

Enables a disabled user account for a given user ID.  

Takes in the disabled User's ID and a valid token and enables the user. 

params:  user_id: str - the user's given ID.  token: str - token used for enabling a user  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user_id= "886b4266-77d1-4258-abae-2931fb4f16de"     >>> mf_resp = mfsdk.users.enable(user)     >>> mf_resp             

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(user_id: str, token: str)
```

Gets a user information. 

Gets info on currently logged in user. Info is obtained  using authorization token and the user id. 

params:  user_id: str - user information eg "886b4266-77d1-4258-abae-2931fb4f16de",  token: str - token used for creating a new user  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user_id = "886b4266-77d1-4258-abae-2931fb4f16de"     >>> mf_resp = mfsdk.users.get(user)     >>> mf_resp             

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L201"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, user_token: str)
```

Retrieves a list of users.  

Gets a list of users from the database when provided with a user token and some parameters.  

params:   user_token: str - token used for creating a new user  query_params: dict - has a limit(int) which is the size of the subset  to be expected and offset which is the number of items to skip during retrieval.  For example:  {  "offset" : 0, "limit" : 10  }  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
``` 

      >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> query_params = {     ...     "offset" : 0, "limit" : 10     ...     }     >>> mf_resp = mfsdk.users.get(user)     >>> mf_resp         

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `login`

```python
login(user: dict)
```

Generates an access token when provided with proper credentials. 

Issues a new access and refresh token for a user for authenticating  into the system. 

params:   user: a dict with the user information and password.   {  "identity": "user@mainflux.com",  "secret": "12345678"  } 

**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```  

    >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user = {     ...     "name": "example",     ...     "credentials": {     ...         "identity": "user@mainflux.com",     ...         "secret": "12345678"     ...     }     ... }     >>> mf_resp = mfsdk.users.login(user)     >>> mf_resp                 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `refresh_token`

```python
refresh_token(refresh_token: str)
```

Refreshes Access and Refresh Token used for authenticating  into the system. 

Creates a new access token and refresh token for a user when  provided with a valid refresh token. 

params:   refresh_token: str - token used to refresh access.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```  

    >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user = {     ...     "name": "example",     ...     "credentials": {     ...         "identity": "example@mail.com",     ...         "secret": "12345678"     ...     }     ... }     >>> mf_resp = mfsdk.users.refresh_token(user)     >>> mf_resp 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L546"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset_password`

```python
reset_password(password: str, confirm_password: str, token: str)
```

Changes user password with the reset_request token 

When user gets reset token, after he submitted email to  /password/reset-request, posting a new password along to this  endpoint will change password. 

params:   passwor: str - the user's new password.  confirm_password: str - a recurrence of the password to ensure it  is the same.  token: str - the reset token recieved from the reset_request email.  



**returns:**
 
 - <b>`mf_resp`</b>:  "OK" 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L517"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset_password_request`

```python
reset_password_request(email: str, url: str)
```

User Password reset request.  

Generates a reset token and sends and email  with link for resetting password. 

params:  referrer email: str - this is the host being sent by the browser.  the email is part of the header.  url: str.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L245"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(user: dict, user_token: str)
```

Updates information on currently logged in user.  

Information such as name and metadata is updated using authorization user_token 

params:  user: dict - user information for example:  

 {  "name": "example",  "id": "886b4266-77d1-4258-abae-2931fb4f16de"  "credentials": {  "identity": "example@main.com",  "secret": "12345678"  },  "metadata": {  "foo": "bar"  }  }  token: str - token used for creating a new user  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user = {          "name": "example",          "id": "886b4266-77d1-4258-abae-2931fb4f16de"          "credentials": {              "identity": "example@main.com",              "secret": "12345678"          },          "metadata": {              "foo": "bar"          }     }     >>> mf_resp = mfsdk.users.update(user)     >>> mf_resp             

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L478"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_password`

```python
update_password(old_secret: str, new_secret: str, user_token: str)
```

Changes user password. 

Updates secret of currently logged in user. Secret is updated using  authorization token and the new received info.  

params:  old_secret: str - the logged in user's current secret.  new_secret: str - the user's new secret.  token: str - token used for creating a new user  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> old_secret = old_secret     >>> new_secret = new_secret     >>> mf_resp = mfsdk.users.update(user)     >>> mf_resp             

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L302"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_user_identity`

```python
update_user_identity(user: dict, user_token: str)
```

Updates identity information on currently logged in user.  

The user Identity is updated using authorization user_token 

params:  user: dict - user information for example:  

 {  "name": "example",  "id": "886b4266-77d1-4258-abae-2931fb4f16de"  "credentials": {  "identity": "example@main.com",  "secret": "12345678"  },  "metadata": {  "foo": "bar"  }  }  token: str - token used for creating a new user  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user = {          "name": "example",          "id": "886b4266-77d1-4258-abae-2931fb4f16de"          "credentials": {              "identity": "example@main.com",              "secret": "12345678"          },          "metadata": {              "foo": "bar"          }     }     >>> mf_resp = mfsdk.users.update_user_idenity(user)     >>> mf_resp             

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L421"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_user_owner`

```python
update_user_owner(user: dict, user_token: str)
```

Updates owner on currently logged in user.  

Updates owner for the user with provided ID. Owner is updated using  authorization token and a new owner identifier received in request. 

params:  user: dict - user information for example:  

 {  "name": "example",  "id": "886b4266-77d1-4258-abae-2931fb4f16de"  "tags": [  "yello",  "orange"  ]  "credentials": {  "identity": "example@main.com",  "secret": "12345678"  },  "metadata": {  "foo": "bar"  },  "owner": "c52d-3b0d-43b9-8c3e-275c087d875af"  }  token: str - token used for creating a new user  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user = {          "name": "example",          "id": "886b4266-77d1-4258-abae-2931fb4f16de",          "owner": "c52d-3b0d-43b9-8c3e-275c087d875af"     }     >>> mf_resp = mfsdk.users.update(user)     >>> mf_resp             

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/users.py#L359"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_user_tags`

```python
update_user_tags(user: dict, user_token: str)
```

Updates tags on currently logged in user.  

Updates tags of the user with provided ID. Tags is updated using  authorization token and the new tags received in request. 

params:  user: dict - user information for example:  

 {  "name": "example",  "id": "886b4266-77d1-4258-abae-2931fb4f16de"  "tags": [  "yello",  "orange"  ]  "credentials": {  "identity": "example@main.com",  "secret": "12345678"  },  "metadata": {  "foo": "bar"  }  }  token: str - token used for creating a new user  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from mainflux import sdk     >>> mfsdk = sdk.SDK(users_url="http://localhost:9002")     >>> user = {          "name": "example",          "id": "886b4266-77d1-4258-abae-2931fb4f16de"          "credentials": {              "identity": "example@main.com",              "secret": "12345678"          },          "metadata": {              "foo": "bar"          }     }     >>> mf_resp = mfsdk.users.update(user)     >>> mf_resp             




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `things`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Things`




<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L268"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `authorise_thing`

```python
authorise_thing(access_request: dict, token: str)
```

Authorises thing 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connect`

```python
connect(thing_id: str, channel_id: str, action: str, token: str)
```

Connects thing and channel 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connects`

```python
connects(thing_ids: list, channel_ids: list, actions: list, token: str)
```

Connects thing and channel 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(thing: dict, token: str)
```

Creates thing entity in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_bulk`

```python
create_bulk(things: list, token: str)
```

Creates multiple things in a bulk 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(thing_id: str, token: str)
```

Deletes a thing entity from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L234"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect(thing_id: str, channel_id: str, token: str)
```

Disconnect thing and channel 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L200"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnects`

```python
disconnects(thing_ids: list, channel_ids: list, token: str)
```

Disconnect thing and channel 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(thing_id: str, token: str)
```

Gets a thing entity for a logged-in user 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, token: str)
```

Gets all things from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_channel`

```python
get_by_channel(channel_id: str, query_params: dict, token: str)
```

Gets all things to which a specific thing is connected to 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L250"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `share_thing`

```python
share_thing(user_id: str, channel_id: str, actions: list, token: str)
```

Share thing 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L100"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(thing_id: str, thing: dict, token: str)
```

Updates thing entity 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_thing_owner`

```python
update_thing_owner(thing_id: str, thing: dict, token: str)
```

Updates thing secret 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_thing_secret`

```python
update_thing_secret(thing_id: str, thing: dict, token: str)
```

Updates thing secret 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/things.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_thing_tags`

```python
update_thing_tags(thing_id: str, thing: dict, token: str)
```

Updates thing secret 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

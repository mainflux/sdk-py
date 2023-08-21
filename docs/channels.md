<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `channels`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Channels`




<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(channel: dict, token: str)
```

Creates channel entity in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_bulk`

```python
create_bulk(channels: list, token: str)
```

Creates multiple channels in a bulk 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(channel_id: str, token: str)
```

Deletes a channel entity from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(channel_id: str, token: str)
```

Gets a channel entity for a logged-in user 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, token: str)
```

Gets all channels from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_thing`

```python
get_by_thing(thing_id: str, query_params: dict, token: str)
```

Gets all channels to which a specific thing is connected to 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `identify_thing`

```python
identify_thing(thing_key: str)
```

Validates thing's key and returns it's ID if key is valid 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/channels.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(channel_id: str, channel: dict, token: str)
```

Updates channel entity 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

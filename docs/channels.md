<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `channels`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Channels`




<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `check_access_by_id`

```python
check_access_by_id(channel_id, thing_id)
```

Checks if thing has access to a channel 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `construct_query`

```python
construct_query(params)
```





---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(channel, token)
```

Creates channel entity in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_bulk`

```python
create_bulk(channels, token)
```

Creates multiple channels in a bulk 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete(chanID, token)
```

Deletes a channel entity from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(chanID, token)
```

Gets a channel entity for a logged-in user 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(token, query_params=None)
```

Gets all channels from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_thing`

```python
get_by_thing(thing_id, params, token)
```

Gets all channels to which a specific thing is connected to 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `identify_thing`

```python
identify_thing(thing_key)
```

Validates thing's key and returns it's ID if key is valid 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/channels.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(channel_id, token, channel)
```

Updates channel entity 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

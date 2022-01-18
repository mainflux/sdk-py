<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `things`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Things`




<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connect`

```python
connect(channel_ids, thing_ids, token)
```

Connects thing and channel 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `construct_query`

```python
construct_query(params)
```





---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(thing, token)
```

Creates thing entity in the database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_bulk`

```python
create_bulk(things, token)
```

Creates multiple things in a bulk 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete(thing_id, token)
```

Deletes a thing entity from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect(channel_ids, thing_ids, token)
```

Disconnect thing and channel 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnect_things`

```python
disconnect_things(channel_ids, thing_ids, token)
```

Disconnect things from channels specified by lists of IDs 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(thing_id, token)
```

Gets a thing entity for a logged-in user 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(token, query_params=None)
```

Gets all things from database 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_channel`

```python
get_by_channel(channel_id, params, token)
```

Gets all things to which a specific thing is connected to 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/lib/things.py#L92"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(thing_id, token, thing)
```

Updates thing entity 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

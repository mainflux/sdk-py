<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `messages`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Messages`




<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(adapter_url: str, reader_url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read`

```python
read(channel_id: str, token: str)
```

Reads messages from database for a given channel 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(channel_id: str, msg: dict, thing_key: str)
```

Sends message via HTTP protocol 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

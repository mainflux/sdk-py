<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/keys.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `keys`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/keys.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Keys`




<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/keys.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/keys.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_key_details`

```python
get_key_details(key_id: str, token: str)
```

Gets API key details for the given key 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/keys.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `issue`

```python
issue(duration: str, token: str)
```

Generates a new API key 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/keys.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `revoke`

```python
revoke(key_id: str, token: str)
```

Revoke API key identified by the given ID. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

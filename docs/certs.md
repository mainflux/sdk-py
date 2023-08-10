<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `certs`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Certs`




<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `issue`

```python
issue(thing_id: str, key_bits: int, key_type: str, valid: str, token: str)
```





---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `revoke`

```python
revoke(thing_id: str, token: str)
```





---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `view`

```python
view(thing_id: str, token: str)
```

Generates an access token when provided with proper credentials. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

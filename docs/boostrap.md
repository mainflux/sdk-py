<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `boostrap`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Bootstrap`




<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add`

```python
add(config: dict, token: str)
```

Adds new config to the list of config owned by user identified using the provided access token. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `bootstrap`

```python
bootstrap(external_id: str, external_key: str)
```

Retrieves a configuration with given external ID and external key. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `remove`

```python
remove(config_id: str, token: str)
```

Removes a Config. In case of successful removal the service will ensure that the removed config is disconnected from all the Mainflux channels. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(config: dict, token: str)
```

Update is performed by replacing the current resource data with values provided in a request payload. Note that the owner, ID, external ID, external key, Mainflux Thing ID and key cannot be changed. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_certs`

```python
update_certs(
    config_id: str,
    client_cert: str,
    client_key: str,
    ca: str,
    token: str
)
```

Update is performed by replacing the current certificate data with values provided in a request payload. 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `view`

```python
view(config_id: str, token: str)
```

Retrieves a configuration with given config id 

---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `whitelist`

```python
whitelist(config: dict, token: str)
```

Updating state represents enabling/disabling Config, i.e.connecting and disconnecting corresponding Mainflux Thing to the list of Channels. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

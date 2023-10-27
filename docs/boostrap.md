<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `boostrap`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Bootstrap`
Bootstrap service API client. 

Bootstrap service is used to manage configurations for Mainflux Things. It provides  services such as updating, viewing, removing and adding new configurations. 



**Attributes:**
 
 - **`url`** (str):  Mainflux Bootstrap API URL. 
 - **`CONFIGS_ENDPOINT`** (str):  Configurations API endpoint. 
 - **`BOOTSTRAP_ENDPOINT`** (str):  Bootstrap API endpoint. 
 - **`WHITELIST_ENDPOINT`** (str):  Whitelist API endpoint. 
 - **`BOOTSTRAP_CERTS_ENDPOINT`** (str):  Bootstrap certificates API endpoint. 



<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```

Initializes Bootstrap with the provided URL. 

params:  url (str): Mainflux Bootstrap API URL.  



**returns:**
 
 - **`Bootstrap`**:  Bootstrap object. 



**raises:**
 None 




---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add`

```python
add(config: dict, token: str)
```

Adds new config to the list of config owned by user identified using the provided access token. 

Some of the key data needed include the external_key and external_id which must be specific to the thing provided with the thing_id. Mind that every configuration  must have a specific thing_id. 

params:  config (dict): Configuration data for example:   {    "external_id": "123",  "external_key": "456",  "thing_id": "fdb1057c-2905-4f71-9a80-e0ce9191e667",  "name": "thing_name"  }  token (str): Authorization token.  



**returns:**
 
 - **`mf_response `**:  response.Response. 

Usage: 

``` from mainflux import sdk```

 - **`    >>> mfsdk = sdk.SDK(bootstrap_url="http`**: //localhost:9013")
    >>> config = {

 - **`    ... "external_id"`**:  "123",

 - **`    ... "external_key"`**:  "456",

 - **`    ... "thing_id"`**:  "fdb1057c-2905-4f71-9a80-e0ce9191e667",

 - **`    ... "name"`**:  "thing_name"
    ... }
    >>> mf_resp = mfsdk.bootstrap.add(config, token)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L300"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `bootstrap`

```python
bootstrap(external_id: str, external_key: str)
```

Retrieves a configuration with given external ID and external key. 

params:  external_id (str): External ID.  external_key (str): External key.  



**returns:**
 
 - **`mf_resp `**:  response.Response - response object. 

Usage: 

``` from mainflux import sdk```

 - **`    >>> mfsdk = sdk.SDK(bootstrap_url="http`**: //localhost:9013")
    >>> external_id = "external_id"
    >>> external_key = "external_key"
    >>> mf_resp = mfsdk.bootstrap.bootstrap(external_id, external_key)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L266"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `remove`

```python
remove(config_id: str, token: str)
```

Removes a Config. In case of successful removal the service will ensure that the removed config is disconnected from all the Mainflux channels. 

params:  config_id (str): Configuration ID.  token (str): Authorization token.  



**returns:**
 
 - **`mf_response `**:  response.Response. 

Usage: 

``` from mainflux import sdk```

 - **`    >>> mfsdk = sdk.SDK(bootstrap_url="http`**: //localhost:9013")
    >>> config_id = "config_id"
    >>> mf_resp = mfsdk.bootstrap.remove(config_id, token)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L173"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(config: dict, token: str)
```

Update is performed by replacing the current resource data with values provided in a request payload. Note that the owner, ID, external ID, external key, Mainflux Thing ID and key cannot be changed. 

params:  config (dict): Configuration data for example:   {    "external_id": "123",  "external_key": "456",  "thing_id": "fdb1057c-2905-4f71-9a80-e0ce9191e667",  "name": "thing_name"  }  token (str): Authorization token.  



**returns:**
 


 - **`mf_response `**:  response.Response. 

Usage: 

``` from mainflux import sdk```

 - **`    >>> mfsdk = sdk.SDK(bootstrap_url="http`**: //localhost:9013")
    >>> config = {

 - **`    ... "external_id"`**:  "123",

 - **`    ... "external_key"`**:  "456",

 - **`    ... "thing_id"`**:  "fdb1057c-2905-4f71-9a80-e0ce9191e667",

 - **`    ... "name"`**:  "thing_name"
    ... }
    >>> mf_resp = mfsdk.bootstrap.update(config, token)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L224"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

params:   config_id (str): Configuration ID.  client_cert (str): Client certificate.  client_key (str): Client key.  ca (str): CA certificate.  token (str): Authorization token.  



**returns:**
 
 - **`mf_response `**:  response.Response. 

Usage: 

``` from mainflux import sdk```

 - **`    >>> mfsdk = sdk.SDK(bootstrap_url="http`**: //localhost:9013")
    >>> config_id = "config_id"
    >>> client_cert = "client_cert"
    >>> client_key = "client_key"
    >>> ca = "ca"
    >>> mf_resp = mfsdk.bootstrap.update_certs(config_id, client_cert, client_key, ca, token)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `view`

```python
view(thing_id: str, token: str)
```

Retrieves a configuration with given config id 

Provides a configuration with given config id. 

params:  thing_id (str): Thing ID.  token (str): Authorization token.  



**returns:**
 
 - **`mf_resp `**:  response.Response - response object. 

Usage: 

``` from mainflux import sdk```

 - **`    >>> mfsdk = sdk.SDK(bootstrap_url="http`**: //localhost:9013")
    >>> thing_id = "thing_id"
    >>> mf_resp = mfsdk.bootstrap.view(thing_id, token)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/boostrap.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `whitelist`

```python
whitelist(config: dict, token: str)
```

Updating state represents enabling/disabling Config, i.e.connecting and disconnecting corresponding Mainflux Thing to the list of Channels. 

params:  config (dict): Configuration data for example:   {    "external_id": "123",  "external_key": "456",  "thing_id": "fdb1057c-2905-4f71-9a80-e0ce9191e667",  "name": "thing_name"  }  token (str): Authorization token.  



**returns:**
 
 - **`mf_response `**:  response.Response. 

Usage: 

``` from mainflux import sdk```

 - **`    >>> mfsdk = sdk.SDK(bootstrap_url="http`**: //localhost:9013")
    >>> config = {

 - **`    ... "external_id"`**:  "123",

 - **`    ... "external_key"`**:  "456",

 - **`    ... "thing_id"`**:  "fdb1057c-2905-4f71-9a80-e0ce9191e667",

 - **`    ... "name"`**:  "thing_name"
    ... }
    >>> mf_resp = mfsdk.bootstrap.whitelist(config, token)
    >>> mf_resp        





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `certs`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Certs`
Mainflux Certificates API 

Certs is used to issue, view, and revoke certificates. It is used to issue certificates for things.  



**Args:**
 
 - <b>`url`</b> (str):  Mainflux Certificates API URL. 
 - <b>`CERTS_ENDPOINT`</b> (str):  Certificates API endpoint. 

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```

Initializes Certs with the provided URL. 



**Args:**
 
 - <b>`url`</b> (str):  Mainflux Certificates API URL. 



**Returns:**
 
 - <b>`Certs`</b>:  Certs object. 




---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `issue`

```python
issue(thing_id: str, valid: str, token: str)
```

Issues a certificate for a given thing ID. 



**Args:**
 
 - <b>`thing_id`</b> (str):  Thing ID. 
 - <b>`valid`</b> (str):  Certificate validity period. 
 - <b>`token`</b> (str):  Authorization token. 



**Returns:**
 
 - <b>`Response`</b>:  Mainflux response. 

Usage: ``` from mainflux import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(certs_url="http`</b>: //localhost:9019")
    >>> thing_id = "thing_id"
    >>> valid = "1h"
    >>> mf_resp = mfsdk.certs.issue(thing_id, valid)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `revoke`

```python
revoke(thing_id: str, token: str)
```

Revokes a certificate for a given thing ID. 

Deletes a certificate for a given thing ID and valid token. 

params:  thing_id (str): thing id  token (str): valid authorization token used to delete the certificate 



**Returns:**
 
 - <b>`mf_resp `</b>:  response.Response - response object. 

Usage: 

``` from mainflux import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(certs_url="http`</b>: //localhost:9019")
    >>> thing_id = "thing_id"
    >>> mf_resp = mfsdk.certs.revoke(thing_id)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `view_by_serial`

```python
view_by_serial(cert_id: str, token: str)
```

Retrieves a certificate for a given cert ID. 

Provides a certificate for a given cert ID. 

Params: 

 cert_id (str): Certificate ID.  token (str): Authorization token.  



**Returns:**
 
 - <b>`mf_resp `</b>:  response.Response - response object. 

Usage: 

``` from mainflux import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(certs_url="http`</b>: //localhost:9019")
    >>> cert_id = "cert_id"
    >>> mf_resp = mfsdk.certs.view_by_serial(cert_id)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/certs.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `view_by_thing`

```python
view_by_thing(thing_id: str, token: str)
```

Retrieves a list of certificates' serial IDs for a given thing ID. 

Provides a list of certificates' serial IDs for a given thing ID. 

Params:  thing_id (str): Thing ID.  token (str): Authorization token.  



**Returns:**
 
 - <b>`mf_resp `</b>:  response.Response - response object. 

Usage: 

``` from mainflux import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(certs_url="http`</b>: //localhost:9019")
    >>> thing_id = "thing_id"
    >>> mf_resp = mfsdk.certs.view_by_thing(thing_id)
    >>> mf_resp





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

<!-- markdownlint-disable -->

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `messages`






---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Messages`
Messages API client 

Messages API client enables interaction with Mainflux Messages API. It provides methods for sending and reading messages. 



**Attributes:**
 
 - <b>`adapter_url`</b>:  URL of the Mainflux Messages adapter 
 - <b>`reader_url`</b>:  URL of the Mainflux Messages reader 

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(adapter_url: str, reader_url: str)
```








---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read`

```python
read(channel_id: str, token: str)
```

Reads messages from database for a given channel 

Reads message from a given channel via HTTP protocol. Message is read through a reader add-on such as timescale. 

params:  channel_id: ID of the channel to read message from  token: token of the user reading the message 



**returns:**
 
 - <b>`mf_resp`</b>:  response object 

usage: 

``` from mainflux import sdk```

 - <b>`    >>> mfsdk = sdk.Sdk("http`</b>: //localhost:9011")
    >>> channel_id = "2b86beba-83dd-4b39-8165-4dda4e6eb4ad"
    >>> mf_resp = mfsdk.messages.read(channel_id, token)
    >>> mf_resp


---

<a href="https://github.com/mainflux/sdk-py/blob/main/mainflux/messages.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `send`

```python
send(channel_id: str, msg: str, thing_key: str)
```

Sends message via HTTP protocol 

Sends message to a given channel via HTTP protocol. Message is sent through a writer add-on such as timescale. Message is sent to a http port specific to the writer add-on. The thing and channel must be created before sending the message and connected.  

params:  channel_id: ID of the channel to send message to  msg: message to send to the channel that should be in encoded into  bytes format for example:   [{"bn":"demo", "bu":"V", "n":"voltage", "u":"V", "v":5}]  thing_key: secret of the thing sending the message 



**returns:**
 
 - <b>`mf_resp`</b>:  response object 

usage: 

``` from mainflux import sdk```

 - <b>`    >>> mfsdk = sdk.Sdk("http`</b>: //localhost:9011")
    >>> channel_id = "2b86beba-83dd-4b39-8165-4dda4e6eb4ad"

 - <b>`    >>> msg = '[{"bn"`</b>: "demo", "bu":"V", "n":"voltage", "u":"V", "v":5}]'
    >>> thing_key = "fc68b31b-d7fd-4879-b3a7-0baf4580c5b1"
    >>> mf_resp = mfsdk.messages.send(channel_id, msg, thing_key)
    >>> mf_resp





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._

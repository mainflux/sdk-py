from mainflux import sdk

s = sdk.SDK()

msg = "helloMF"
token = "9a8b7c6d5e4f3g21"
url = "http://localhost"
channel_id = "224-335-668"


def test_send(requests_mock):
    requests_mock.register_uri("POST", url + "/http/channels/" + channel_id + "/messages/", status_code=202)
    r = s.messages.send(channel_id=channel_id, msg=msg, thing_key=token)
    assert r.error.status == 0


def test_read(requests_mock):
    requests_mock.register_uri("GET", url + "/channels/" + channel_id + "/messages", json=msg, status_code=200)
    r = s.messages.read(channel_id=channel_id, token=token)
    assert r.error.status == 0
    assert msg == r.value
    
def test_send_malformed_channel_id(requests_mock):
    requests_mock.register_uri("POST", url + "/http/channels/" + channel_id + "/messages/", status_code=400)
    r = s.messages.send(channel_id=channel_id, msg=msg, thing_key=token)
    assert r.error.status == 1
    assert r.error.message == "Message discarded due to its malformed content."

def test_read_malformed_query_params(requests_mock):
    requests_mock.register_uri("GET", url + "/channels/" + channel_id + "/messages", json=msg, status_code=400)
    r = s.messages.read(channel_id=channel_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed query parameters."

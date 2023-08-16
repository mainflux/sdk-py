from mainflux import sdk

import json
import requests_mock

s = sdk.SDK()

channel ={
  "id": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
  "name": "channelName",
  "owner_id": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
  "parent_id": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
  "description": "long channel description",
  "metadata": {
    "role": "general"
  },
  "path": "bb7edb32-2eac-4aad-aebe-ed96fe073879.bb7edb32-2eac-4aad-aebe-ed96fe073879",
  "level": 2,
  "created_at": "2019-11-26 13:31:52",
  "updated_at": "2019-11-26 13:31:52",
  "status": "enabled"
}
channel_id = "123-456-789"
channel_id1 = "123-223-333"
thing_id = "332-665-998"
thing_key = "664-220-886"
token = "9a8b7c6d5e4f3g21"
url = "http://localhost"
params = None


def test_create_channel(requests_mock):
    requests_mock.register_uri( "POST", url + "/channels", headers={"location": "/channels/" + channel_id}, json=channel, status_code=201)
    r = s.channels.create(channel=channel, token=token)
    assert r.error.status == 0
    assert channel == r.value


def test_create_channel_entity_exist(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/channels", headers={"location": "/channels/" + channel_id}, status_code=409)
    r = s.channels.create(channel=channel, token=token)
    assert r.error.status == 1
    assert r.error.message == "Entity already exist."


def test_create_bulk_channels(requests_mock):
    requests_mock.register_uri("POST", url + "/channels/bulk", json=[channel_id, channel_id1], headers={"location": "/channels/channel_ids"}, status_code=201)
    r = s.channels.create_bulk(channel_id, token=token)
    assert r.error.status == 0
    assert [channel_id, channel_id1] == r.value


def test_create_bulk_channels_server_error(requests_mock):
    requests_mock.register_uri("POST", url + "/channels/bulk", json=[channel_id, channel_id1], headers={"location": "/channels/channel_ids"}, status_code=500)
    r = s.channels.create_bulk(channel_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Unexpected server-side error occurred."


def test_get_channel(requests_mock):
    requests_mock.register_uri("GET", url + "/channels/" + channel_id, json=channel, status_code=200)
    r = s.channels.get(channel_id=channel_id, token=token)
    assert r.error.status == 0
    assert channel == r.value


def test_get_channel_bad_token(requests_mock):
    requests_mock.register_uri("GET", url + "/channels/" + channel_id, json=channel, status_code=401)
    r = s.channels.get(channel_id=channel_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."


def test_get_all_channels(requests_mock):
    requests_mock.register_uri("GET", url + "/channels", json=[channel_id, channel_id1], status_code=200)
    r = s.channels.get_all(token=token, query_params=params)
    assert r.error.status == 0
    assert [channel_id, channel_id1] == r.value


def test_get_all_channels_channel_does_not_exist(requests_mock):
    requests_mock.register_uri("GET", url + "/channels", json=[channel_id, channel_id1], status_code=404)
    r = s.channels.get_all(token=token, query_params=params)
    assert r.error.status == 1
    assert r.error.message == "Channel does not exist."


def test_get_by_thing(requests_mock):
    requests_mock.register_uri("GET", url + "/things/" + thing_id + "/channels", json=channel_id, headers={"Authorization": "/channels/" + channel_id + "/things"}, status_code=200)
    r = s.channels.get_by_thing(
        thing_id=thing_id, query_params=params, token=token)
    assert r.error.status == 0
    assert channel_id == r.value


def test_get_by_thing_does_not_exist(requests_mock):
    requests_mock.register_uri("GET", url + "/things/" + thing_id + "/channels", json=channel_id, headers={"Authorization": "/channels/" + channel_id + "/things"}, status_code=404)
    r = s.channels.get_by_thing(
        thing_id=thing_id, query_params=params, token=token)
    assert r.error.status == 1
    assert r.error.message == "Thing does not exist."


def test_update_channel(requests_mock):
    requests_mock.register_uri("PUT", url + "/channels/" + channel_id, json=json.dumps(channel), status_code=200)
    r = s.channels.update(channel_id=channel_id, token=token, channel=channel)
    assert r.error.status == 0


def test_update_channel_does_not_exist(requests_mock):
    requests_mock.register_uri("PUT", url + "/channels/" + channel_id, json=json.dumps(channel), status_code=404)
    r = s.channels.update(channel_id=channel_id, token=token, channel=channel)
    assert r.error.status == 1
    assert r.error.message == "Channel does not exist."


def test_delete_channel(requests_mock):
    requests_mock.register_uri("POST", url + "/channels/" + channel_id + "/disable", status_code=200)
    r = s.channels.disable(channel_id=channel_id, token=token)
    assert r.error.status == 0


def test_delete_channel_malformed_channel_id(requests_mock):
    requests_mock.register_uri("POST", url + "/channels/" + channel_id + "/disable", status_code=400)
    r = s.channels.disable(channel_id=channel_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed channel's ID."


def test_identify_thing(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/identify", json=thing_key, status_code=200)
    r = s.channels.identify_thing(thing_key)
    assert r.error.status == 0
    assert thing_key == r.value

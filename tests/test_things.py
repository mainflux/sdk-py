from mainflux import sdk

import requests_mock

s = sdk.SDK()

thing = {
  "id": "35ad0272-94bb-4701-9785-ff32334327a0",
  "name": "thing",
  "tags": [
    "tag1",
    "tag2"
  ],
  "owner": "edc876eb-27e2-4bc9-8599-4faf21d2a12f",
  "credentials": {
    "identity": "thingidentity",
    "secret": "f002d93b-fa40-435e-b9d9-37f991e47e9f"
  },
  "metadata": {
    "domain": "example.com"
  },
  "status": "enabled"
}
things = [{
  "id": "4e5532c0-cf92-4ef3-ab7b-65ee30151c99",
  "name": "thing1",
  "tags": [
    "tag1",
    "tag2"
  ],
  "owner": "edc876eb-27e2-4bc9-8599-4faf21d2a12f",
  "credentials": {
    "identity": "thingidentity",
    "secret": "47749f5e-1e32-4834-9a1d-2d38871d4e1e"
  },
  "metadata": {
    "domain": "example.com"
  },
  "status": "enabled"
}, {
  "id": "53ed347d-f277-4e2b-9ee1-442389ad1a9a",
  "name": "thing2",
  "tags": [
    "tag1",
    "tag2"
  ],
  "owner": "edc876eb-27e2-4bc9-8599-4faf21d2a12f",
  "credentials": {
    "identity": "thingidentity",
    "secret": "566eff24-0b55-4033-9ab1-b4df0d9a3266"
  },
  "metadata": {
    "domain": "example.com"
  },
  "status": "enabled"
}]
thing_id = "123-456-789"
thing_id1 = "123-223-333"
channel_id = "654-654-654"
channel_id1 = "654-654-654"
user_id= "123-679-773"
action= "m_read"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
url = "http://localhost"
params = None
access_request= {
    "subject": "123-456-789",
    "object": "654-654-654",
    "action": "m_read",
    "entity_type": "group"
}
policies= {
  "policies": [
    {
      "owner_id": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
      "subject": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
      "object": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
      "actions": [
        "m_write",
        "g_add"
      ],
      "created_at": "2019-11-26 13:31:52",
      "updated_at": "2019-11-26 13:31:52"
    }
  ],
  "total": 1,
  "offset": 0,
  "limit": 10
}

def test_create_thing(requests_mock):
    requests_mock.register_uri("POST", url + "/things", headers={"location": "/things/" + thing["id"]}, json=thing, status_code=201)
    r = s.things.create(thing=thing, token=token)
    assert r.error.status == 0
    assert thing == r.value

def test_create_existing_thing(requests_mock):
    requests_mock.register_uri("POST", url + "/things", headers={"location": "/things/" + thing_id}, status_code=409)
    r = s.things.create(thing=thing, token=token)
    assert r.error.status == 1
    assert r.error.message == "Entity already exist."

def test_create_bulk_things(requests_mock):
    requests_mock.register_uri("POST", url + "/things/bulk", json=things, status_code=200)
    r = s.things.create_bulk(things=things, token=token)
    assert r.error.status == 0
    assert things == r.value

def test_create_bulk_things_missing_token(requests_mock):
    requests_mock.register_uri("POST", url + "/things/bulk", json=[thing_id, thing_id1], headers={"location": "/things/" + thing_id}, status_code=401)
    r = s.things.create_bulk(things=things, token=token)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_get_thing(requests_mock):
    requests_mock.register_uri("GET", url + "/things/" + thing_id, json=thing, status_code=200)
    r = s.things.get(thing_id=thing_id, token=token)
    assert r.error.status == 0
    assert thing == r.value

def test_get_thing_malformed_query(requests_mock):
    requests_mock.register_uri("GET", url + "/things/" + thing_id, json=thing, status_code=400)
    r = s.things.get(thing_id=thing_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed query parameters."

def test_get_all_things(requests_mock):
    requests_mock.register_uri("GET", url + "/things", json=[thing_id, thing_id1], status_code=200)
    r = s.things.get_all(token=token, query_params=params)
    assert r.error.status == 0
    assert [thing_id, thing_id1] == r.value

def test_get_all_thing_does_not_exist(requests_mock):
    requests_mock.register_uri("GET", url + "/things", json=[thing_id, thing_id1], status_code=404)
    r = s.things.get_all(token=token, query_params=params)
    assert r.error.status == 1
    assert r.error.message == "Thing does not exist."

def test_get_by_channel(requests_mock):
    requests_mock.register_uri("GET", url + "/channels/" + channel_id + "/things", json=channel_id, headers={"Authorization": "/channels/" + channel_id + "/things"}, status_code=200)
    r = s.things.get_by_channel(channel_id=channel_id, query_params=params, token=token)
    assert r.error.status == 0
    assert channel_id == r.value

def test_get_by_channel_missing_token(requests_mock):
    requests_mock.register_uri("GET", url + "/channels/" + channel_id + "/things", json=channel_id, headers={"Authorization": "/channels/" + channel_id + "/things"}, status_code=401)
    r = s.things.get_by_channel(channel_id=channel_id, query_params=params, token=token)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_update_thing(requests_mock):
    requests_mock.register_uri("PATCH", url + "/things/" + thing["id"], json=thing, status_code=200)
    r = s.things.update(thing_id=thing["id"], token=token, thing=thing)
    assert r.error.status == 0
    assert thing== r.value

def test_update_thing_bad_json(requests_mock):
    requests_mock.register_uri("PATCH", url + "/things/" + thing["id"], json=thing, status_code=404)
    r = s.things.update(thing_id=thing["id"], token=token, thing=thing)
    assert r.error.status == 1
    assert r.error.message == "Thing does not exist."

def test_update_thing_secret(requests_mock):
    requests_mock.register_uri("PATCH", url + "/things/" + thing["id"] + "/secret", json=thing, status_code=200)
    r = s.things.update_thing_secret(thing_id=thing["id"], token=token, thing=thing)
    assert r.error.status == 0
    assert thing== r.value

def test_update_thing_secret_bad_token(requests_mock):
    requests_mock.register_uri("PATCH", url + "/things/" + thing["id"] + "/secret", json=thing, status_code=401)
    r = s.things.update_thing_secret(thing_id=thing["id"], token=token, thing=thing)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_update_thing_tags(requests_mock):
    requests_mock.register_uri("PATCH", url + "/things/" + thing["id"] + "/tags", json=thing, status_code=200)
    r = s.things.update_thing_tags(thing_id=thing["id"], token=token, thing=thing)
    assert r.error.status == 0
    assert thing== r.value

def test_update_thing_tags_bad_token(requests_mock):
    requests_mock.register_uri("PATCH", url + "/things/" + thing["id"] + "/tags", json=thing, status_code=401)
    r = s.things.update_thing_tags(thing_id=thing["id"], token=token, thing=thing)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_update_thing_owner(requests_mock):
    requests_mock.register_uri("PATCH", url + "/things/" + thing["id"] + "/owner", json=thing, status_code=200)
    r = s.things.update_thing_owner(thing_id=thing["id"], token=token, thing=thing)
    assert r.error.status == 0
    assert thing== r.value

def test_update_thing_owner_bad_token(requests_mock):
    requests_mock.register_uri("PATCH", url + "/things/" + thing["id"] + "/owner", json=thing, status_code=401)
    r = s.things.update_thing_owner(thing_id=thing["id"], token=token, thing=thing)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_disable_thing(requests_mock):
    requests_mock.register_uri("POST", url + "/things/" + thing["id"] + "/disable", status_code=200)
    r = s.things.disable(thing_id=thing["id"], token=token)
    assert r.error.status == 0

def test_disable_bad_thing_id(requests_mock):
    requests_mock.register_uri("POST", url + "/things/" + thing["id"] + "/disable", status_code=400)
    r = s.things.disable(thing_id=thing["id"], token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed thing's ID."

def test_connect_thing(requests_mock):
    requests_mock.register_uri("POST", url + "/policies", status_code=201)
    r = s.things.connect(channel_id=channel_id, thing_id=thing_id, token=token, action=["m_read"])
    assert r.error.status == 0
    assert r.value == "connected"

def test_connects_things(requests_mock):
    requests_mock.register_uri("POST", url + "/connect", json=policies, status_code=201)
    r = s.things.connects(channel_ids=[channel_id], thing_ids=[thing_id, thing_id1], token=token, actions=["m_read"])
    assert r.error.status == 0    
    
def test_connects_things_non_existing_entity(requests_mock):
    requests_mock.register_uri("POST", url + "/connect", status_code=400)
    r = s.things.connects(channel_ids=[channel_id], thing_ids=[thing_id, thing_id1], token=token, actions=["m_read"])
    assert r.error.status == 1
    assert r.error.message == "A non-existent entity request."

def test_connect_non_existing_entity(requests_mock):
    requests_mock.register_uri("POST", url + "/policies", status_code=404)
    r = s.things.connect(channel_id=channel_id, thing_id=thing_id, token=token, action="m_read")
    assert r.error.status == 1
    assert r.error.message == "A non-existent entity request."

def test_disconnect_thing(requests_mock):
    requests_mock.register_uri("DELETE", url + "/policies" + "/" + thing_id + "/" + channel_id, status_code=204)
    r = s.things.disconnect(channel_id=channel_id, thing_id=thing_id, token=token)
    assert r.error.status == 0
    
def test_disconnect_thing_or_channel_does_not_exist(requests_mock):
    requests_mock.register_uri("DELETE", url + "/policies" + "/" + thing_id + "/" + channel_id, status_code=404)
    r = s.things.disconnect(channel_id=channel_id, thing_id=thing_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Channel or thing does not exist."

def test_disconnects(requests_mock):
    requests_mock.register_uri("POST", url + "/disconnect", status_code=204)
    r = s.things.disconnects(channel_ids=[channel_id], thing_ids=[thing_id, thing_id1], token=token)
    assert r.error.status == 0

def test_disconnects_bad_json(requests_mock):
    requests_mock.register_uri("POST", url + "/disconnect", status_code=404)
    r = s.things.disconnects(channel_ids=[channel_id], thing_ids=[thing_id, thing_id1], token=token)
    assert r.error.status == 1
    assert r.error.message == "Channel or thing does not exist."

def test_share_thing(requests_mock):
    requests_mock.register_uri("POST", url + "/policies", status_code=201)
    r = s.things.share_thing(channel_id=channel_id, user_id=user_id, actions= action, token=token)
    assert r.error.status == 0

def test_share_thing_bad_token(requests_mock):
    requests_mock.register_uri("POST", url + "/policies", status_code=400)
    r = s.things.share_thing(channel_id=channel_id, user_id=user_id, actions= action, token=token)
    assert r.error.status == 1
    assert r.error.message == "A non-existent entity request."
    
def test_authorise_thing(requests_mock):
    requests_mock.register_uri("POST", url + "/channels/object/access", status_code=200)
    r = s.things.authorise_thing(access_request=access_request , token=token)
    assert r.error.status == 0

def test_authorise_thing_bad_token(requests_mock):
    requests_mock.register_uri("POST", url + "/channels/object/access", status_code=403)
    r = s.things.authorise_thing(access_request=access_request , token=token)
    assert r.error.status == 1
    assert r.error.message == "False"

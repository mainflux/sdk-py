from lib import sdk

import json, requests_mock

s = sdk.SDK()

token = "9a8b7c6d5e4f3g21"
duration_params = {"type":2, "duration":10000}
key_id = "123-456-789"
url = "http://localhost"
params = None


def test_create(requests_mock):
    requests_mock.register_uri("POST", url + "/keys", json=token, status_code=201)
    r = s.api.create(token, duration_params)
    assert r.error.status == 0
    assert token == r.value


def test_create_existing_key(requests_mock):
    requests_mock.register_uri("POST", url + "/keys", status_code=409)
    r = s.api.create(token, duration_params)
    assert r.error.status == 1
    assert r.error.message == "Entity already exist."

def test_get_key_details(requests_mock):
    requests_mock.register_uri("GET", url + "/keys/" + key_id, json=key_id, status_code=200)
    r = s.api.get_key_details(token, key_id)
    assert r.error.status == 0
    assert key_id == r.value

def test_get_key_details_missing_token(requests_mock):
    requests_mock.register_uri("GET", url + "/keys/" + key_id, json=key_id, status_code=403)
    r = s.api.get_key_details(token, key_id)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_revoke(requests_mock):
    requests_mock.register_uri("DELETE", url + "/keys/" + key_id, status_code=204)
    r = s.api.revoke(token, key_id)
    assert r.error.status == 0


def test_revoke_bad_key(requests_mock):
    requests_mock.register_uri("DELETE", url + "/keys/" + key_id, status_code=403)
    r = s.api.revoke(token, key_id)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."
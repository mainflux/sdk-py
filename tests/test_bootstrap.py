from mainflux import sdk

import json
import requests_mock

s= sdk.SDK()

config = {
   "external_id": "234567",
  "external_key": "234567",
  "thing_id": "828b93e3-52b3-43a4-9ce2-ed8a47127ddd",
  "name": "demo5"
}

token= "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI3NzI5NDgsImlhdCI6MTY5MjcxODk0OCwiaWRlbnRpdHkiOiJqb2xseV9uYXBpZXJAZW1haWwuY29tIiwiaXNzIjoiY2xpZW50cy5hdXRoIiwic3ViIjoiZjhiMDIwMmEtOGE4ZS00M2NjLWExZjctOWIzOWZkYmFlYjY3IiwidHlwZSI6ImFjY2VzcyJ9.-aEhFrpXxiCUW-zjCqQvUDi2UTtu5y0nkJgzDtUV-YiN1ZyMYUwwc9z8NvJPAfHCscagP4ifidWJ-ovkZULg4g"
thing_id= "828b93e3-52b3-43a4-9ce2-ed8a47127ddd"
external_id= "234567"
external_key= "234567"
config_id="828b93e3-52b3-43a4-9ce2-ed8a47127ddd"

url = "http://localhost"

def test_add(requests_mock):
    requests_mock.register_uri( "POST", url+ "/things/configs", headers={"location": "/configs/" + thing_id}, json=config, status_code=201)
    r = s.bootstrap.add(config=config, token=token)
    assert r.error.status == 0
    assert r.value == "added"

def test_add_bad_token(requests_mock):
    requests_mock.register_uri( "POST", url+ "/things/configs", headers={"location": "/configs/" + thing_id}, json=config, status_code=401)
    r = s.bootstrap.add(config=config, token=token)
    assert r.error.status == 1
    assert r.error.message =="Missing or invalid access token provided."
    
def test_whitelist(requests_mock):
    requests_mock.register_uri( "PUT", url+ "/things/state/" + config["thing_id"], json=config, status_code=201)
    r = s.bootstrap.whitelist(config=config, token=token)
    assert r.error.status == 0
    assert r.value == "OK"
    
def test_whitelist_bad_config(requests_mock):
    requests_mock.register_uri( "PUT", url+ "/things/state/" + config["thing_id"], json=config, status_code=400)
    r = s.bootstrap.whitelist(config=config, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed config's ID."

def test_whitelist_config_removed(requests_mock):
    requests_mock.register_uri( "PUT", url+ "/things/state/" + config["thing_id"], json=config, status_code=204)
    r = s.bootstrap.whitelist(config=config, token=token)
    assert r.error.status == 1
    assert r.error.message == "Config removed."
        
def test_view(requests_mock):
    requests_mock.register_uri( "GET", url+ "/things/configs/" + thing_id, json=config, status_code=200)
    r = s.bootstrap.view(thing_id=thing_id, token=token)
    assert r.error.status == 0
    assert config == r.value

def test_view_bad_config(requests_mock):
    requests_mock.register_uri( "GET", url+ "/things/configs/" + thing_id, json=config, status_code=404)
    r = s.bootstrap.view(thing_id=thing_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Config does not exist."
    
def test_update(requests_mock):
    requests_mock.register_uri( "PUT", url+ "/things/configs/" + config["thing_id"], json=config, status_code=200)
    r = s.bootstrap.update(config=config, token=token)
    assert r.error.status == 0
    assert r.value == "Config updated."

def test_update_bad_config(requests_mock):
    requests_mock.register_uri( "PUT", url+ "/things/configs/" + config["thing_id"], json=config, status_code=404)
    r = s.bootstrap.update(config=config, token=token)
    assert r.error.status == 1
    assert r.error.message == "Config does not exist."

def test_bootstrap(requests_mock):
    requests_mock.register_uri( "GET", url+ "/things/bootstrap/" + external_id, json=config, status_code=200)
    r = s.bootstrap.bootstrap(external_id=external_id, external_key=external_key)
    assert r.error.status == 0
    assert config == r.value

def test_bootstrap_bad_config(requests_mock):
    requests_mock.register_uri( "GET", url+ "/things/bootstrap/" + external_id, json=config, status_code=404)
    r = s.bootstrap.bootstrap(external_id=external_id, external_key=external_key)
    assert r.error.status == 1
    assert r.error.message == "Failed to retrieve corresponding config."

def test_remove(requests_mock):
    requests_mock.register_uri( "DELETE", url+ "/things/configs/" + config_id, status_code=204)
    r = s.bootstrap.remove(config_id=config_id, token=token)
    assert r.error.status == 0
    assert r.value== "Config removed."

def test_remove_bad_config(requests_mock):
    requests_mock.register_uri( "DELETE", url+ "/things/configs/" + config_id, status_code=400)
    r = s.bootstrap.remove(config_id=config_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed config ID."
    
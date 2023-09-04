from mainflux import sdk

import requests_mock

s = sdk.SDK()
user = {
  "id": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
  "name": "userName",
  "tags": [
    "tag1",
    "tag2"
  ],
  "owner": "aa68f94c-de36-48dd-9c53-d8ac8b12d86b",
  "credentials": {
    "identity": "test@email.com"
  },
  "metadata": {
    "domain": "example.com"
  },
  "status": "enabled",
  "created_at": "2019-11-26 13:31:52",
  "updated_at": "2019-11-26 13:31:52"
}
user1 = {
  "id": "1d36ac54-9bb7-4079-a46b-63c34f7fc678",
  "name": "userName1",
  "tags": [
    "tag1",
    "tag2"
  ],
  "owner": "aa68f94c-de36-48dd-9c53-d8ac8b12d86b",
  "credentials": {
    "identity": "test1@email.com"
  },
  "metadata": {
    "domain": "example.com"
  },
  "status": "enabled",
  "created_at": "2019-11-26 13:31:52",
  "updated_at": "2019-11-26 13:31:52"
}

user2 = {
  "id": "e2c769b8-8b8c-4886-8b19-e155c4d363e6",
  "name": "userName",
  "tags": [
    "tag1",
    "tag2"
  ],
  "owner": "aa68f94c-de36-48dd-9c53-d8ac8b12d86b",
  "credentials": {
    "identity": "test2@email.com"
  },
  "metadata": {
    "domain": "example.com"
  },
  "status": "enabled",
  "created_at": "2019-11-26 13:31:52",
  "updated_at": "2019-11-26 13:31:52"
}
old_secret = {"old_secret": "12345678"}
new_secret = {"new_secret": "dsa"}
user_id = "123-456"
token = {
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
  "access_type": "access"
}
access_request ={
    "subject": "e2c769b8-8b8c-4886-8b19-e155c4d363e6",
    "object": "f20e0b0e-b05e-401e-ac53-59b99eea3519",
    "action": "g_add",
    "entity_type": "client"
}
password= "12345678"
confirm_password="12345678"
email={"admin@example.com": "email"}
url = "http://localhost"
url2 = "http://localhost/password/reset-request" 

def test_create_user(requests_mock):
    requests_mock.register_uri("POST", url + "/users", headers={"location": "/users/" + user_id}, json=user, status_code=201)
    r = s.users.create(user=user)
    assert r.error.status == 0
    assert user == r.value

def test_create_user_bad_user(requests_mock):
    requests_mock.register_uri("POST", url + "/users", headers={"location": "/users/" + user_id}, status_code=409)
    r = s.users.create(user=user)
    assert r.error.status == 1
    assert r.error.message == "Failed due to using an existing identity."
     
def test_login_user(requests_mock):
    requests_mock.register_uri("POST", url + "/users/tokens/issue", json=token, status_code=201)
    r = s.users.login(user=user)
    assert r.error.status == 0
    assert token == r.value

def test_login_user_bad_email(requests_mock):
    requests_mock.register_uri("POST", url + "/users/tokens/issue", status_code=409)
    r = s.users.login(user=user)
    assert r.error.status == 1
    assert r.error.message == "Failed due to using an existing email address."
    
def test_refresh_token(requests_mock):
    requests_mock.register_uri("POST", url + "/users/tokens/refresh", json=token, status_code=201)
    r = s.users.refresh_token(refresh_token=token["refresh_token"])
    assert r.error.status == 0
    assert token == r.value

def test_refresh_token_bad_token(requests_mock):
    requests_mock.register_uri("POST", url + "/users/tokens/refresh",json=token, status_code=404)
    r = s.users.refresh_token(refresh_token=token["refresh_token"])
    assert r.error.status == 1
    assert r.error.message == "A non-existent entity request."

def test_get_user(requests_mock):
    requests_mock.register_uri("GET", url + "/users/" + user_id, json=user, status_code=200)
    r = s.users.get(user_id=user_id, token=token["access_token"])
    assert r.error.status == 0
    assert user == r.value

def test_get_user_bad_token(requests_mock):
    requests_mock.register_uri("GET", url + "/users/" + user_id, json=user, status_code=401)
    r = s.users.get(user_id=user_id, token=token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_get_all_users(requests_mock):
    requests_mock.register_uri("GET", url + "/users", json=[user, user2], status_code=200)
    r = s.users.get_all(query_params=None, user_token=token["access_token"])
    assert r.error.status == 0
    assert [user, user2] == r.value

def test_get_all_user_bad_request(requests_mock):
    requests_mock.register_uri("GET", url + "/users" , json=user, status_code=422)
    r = s.users.get_all(query_params=None, user_token=token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Database can't process request."

def test_update_user(requests_mock):
    requests_mock.register_uri("PATCH", url + "/users/" + user["id"], json=user, status_code=200)
    r = s.users.update(user=user, user_token=token["access_token"])
    assert r.error.status == 0

def test_non_existing_user_update(requests_mock):
    requests_mock.register_uri("PATCH",url + "/users/" + user["id"], json=user, status_code=404)
    r = s.users.update(user=user, user_token=token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Failed due to non existing user."

def test_update_user_identity(requests_mock):
    requests_mock.register_uri("PATCH", url + "/users/" + user["id"] + "/identity", json=user, status_code=200)
    r = s.users.update_user_identity(user=user, user_token=token["access_token"])
    assert r.error.status == 0

def test_non_existing_user_identity_update(requests_mock):
    requests_mock.register_uri("PATCH",url + "/users/" + user["id"] + "/identity", json=user, status_code=401)
    r = s.users.update_user_identity(user=user, user_token=token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_update_user_tags(requests_mock):
    requests_mock.register_uri("PATCH", url + "/users/" + user["id"] + "/tags", json=user, status_code=200)
    r = s.users.update_user_tags(user=user, user_token=token["access_token"])
    assert r.error.status == 0


def test_non_existing_user_tags_update(requests_mock):
    requests_mock.register_uri("PATCH",url + "/users/" + user["id"] + "/tags", json=user, status_code=401)
    r = s.users.update_user_tags(user=user, user_token=token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."
    
def test_update_user_owner(requests_mock):
    requests_mock.register_uri("PATCH", url + "/users/" + user["id"] + "/owner", json=user, status_code=200)
    r = s.users.update_user_owner(user=user, user_token=token["access_token"])
    assert r.error.status == 0

def test_non_existing_user_owner_update(requests_mock):
    requests_mock.register_uri("PATCH",url + "/users/" + user["id"] + "/owner", json=user, status_code=401)
    r = s.users.update_user_owner(user=user, user_token=token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_update_user_password(requests_mock):
    requests_mock.register_uri("PATCH", url + "/users" + "/secret", status_code=200)
    r = s.users.update_password(old_secret=old_secret, new_secret=new_secret, user_token=token["access_token"])
    assert r.error.status == 0

def test_update_user_password_bad_token(requests_mock):
    requests_mock.register_uri("PATCH",url + "/users" + "/secret", status_code=415)
    r = s.users.update_password(old_secret=old_secret, new_secret=new_secret, user_token=token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid content type."

def test_reset_password_request(requests_mock):
    requests_mock.register_uri("POST", url + "/password/reset-request", json=email, status_code=201)
    r = s.users. reset_password_request(email=email, url=url2)
    assert r.error.status == 0

def test_reset_password_request_bad_email(requests_mock):
    requests_mock.register_uri("POST",url + "/password/reset-request", status_code=400)
    r = s.users. reset_password_request(email=email, url=url2)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed JSON."

def test_reset_password(requests_mock):
    requests_mock.register_uri("PUT", url + "/password/reset", status_code=201)
    r = s.users. reset_password(password=password, confirm_password=confirm_password, token=token)
    assert r.error.status == 0

def test_reset_password_bad_token(requests_mock):
    requests_mock.register_uri("PUT",url + "/password/reset", status_code=400)
    r = s.users. reset_password(password=password, confirm_password=confirm_password, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed JSON."

def test_enable_user(requests_mock):
    requests_mock.register_uri("POST", url + "/users/" + user["id"] + "/enable", json=user, status_code=204)
    r = s.users.enable(user_id=user["id"], user_token= token["access_token"])
    assert r.error.status == 0
    assert user == r.value 
    
def test_disable_user(requests_mock):
    requests_mock.register_uri("POST", url + "/users/" + user["id"] + "/disable", json=user, status_code=200)
    r = s.users.disable(user_id=user["id"], user_token= token["access_token"])
    assert r.error.status == 0
    assert user == r.value  
    
def test_enable_user_bad_user(requests_mock):
    requests_mock.register_uri("POST", url + "/users/" + user["id"] + "/enable", json=user, status_code=404)
    r = s.users.enable(user_id=user["id"], user_token= token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Failed due to non existing user."
    
def test_disable_user_bad_user(requests_mock):
    requests_mock.register_uri("POST", url + "/users/" + user["id"] + "/disable", json=user, status_code=404)
    r = s.users.disable(user_id=user["id"], user_token= token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Failed due to non existing user."

def test_authorise_user(requests_mock):
    requests_mock.register_uri("POST", url + "/authorize", status_code=200)
    r = s.users.authorise_user(access_request=access_request , token=token["access_token"])
    assert r.error.status == 0

def test_authorise_user_bad_token(requests_mock):
    requests_mock.register_uri("POST", url + "/authorize", status_code=400)
    r = s.users.authorise_user(access_request=access_request , token=token["access_token"])
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed JSON."

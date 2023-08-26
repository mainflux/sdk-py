from mainflux import sdk

import requests_mock

s = sdk.SDK()

channel_id = "654-559-774"
members = {"members": channel_id, "type": "channels"}
members_ids ="4e5532c0-cf92-4ef3-ab7b-65ee30151c99"
member_id= "4e5532c0-cf92-4ef3-ab7b-65ee30151c99"
group ={
  "id": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
  "name": "groupName",
  "owner_id": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
  "parent_id": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
  "description": "long group description",
  "metadata": {
    "role": "general"
  },
  "path": "bb7edb32-2eac-4aad-aebe-ed96fe073879.bb7edb32-2eac-4aad-aebe-ed96fe073879",
  "level": 2,
  "created_at": "2019-11-26 13:31:52",
  "updated_at": "2019-11-26 13:31:52",
  "status": "enabled"
}
query_params= {
    "offset": 0, 
    "limit": 5
}
group_id = "888-888-888"
group_id1 = "989-787-686"
thing_group_id = "868-464-262"
token = "9a8b7c6d5e4f3g21"
url = "http://localhost"

def test_create_group(requests_mock):
    requests_mock.register_uri("POST", url + "/groups", headers={"location": "/groups/" + group_id}, json=group, status_code=201)
    r = s.groups.create(group=group, token=token)
    assert r.error.status == 0
    assert group == r.value

def test_create_group_existing_email_address(requests_mock):
    requests_mock.register_uri("POST", url + "/groups", headers={"location": "/groups/" + group_id}, status_code=409)
    r = s.groups.create(group=group, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to using an existing email address."

def test_get_group(requests_mock):
    requests_mock.register_uri("GET", url + "/groups/" + group_id, json=group, status_code=200)
    r = s.groups.get(group_id=group_id, token=token)
    assert r.error.status == 0
    assert group == r.value

def test_get_group_does_not_exist(requests_mock):
    requests_mock.register_uri("GET", url + "/groups/" + group_id, json=group, status_code=404)
    r = s.groups.get(group_id=group_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Group does not exist."
    
def test_get_parents(requests_mock):
    requests_mock.register_uri("GET", url + "/groups/" + group_id + "/parents", json=group, status_code=200)
    r = s.groups.parents(group_id=group_id, query_params= query_params, token=token)
    assert r.error.status == 0
    assert group == r.value

def test_get_parents_bad_json(requests_mock):
    requests_mock.register_uri("GET", url + "/groups/" + group_id + "/parents", status_code=400)
    r = s.groups.parents(group_id=group_id, query_params= query_params, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed query parameters."

def test_get_children(requests_mock):
    requests_mock.register_uri("GET", url + "/groups/" + group_id + "/children", json=group, status_code=200)
    r = s.groups.children(group_id=group_id, query_params= query_params, token=token)
    assert r.error.status == 0
    assert group == r.value

def test_get_children_bad_json(requests_mock):
    requests_mock.register_uri("GET", url + "/groups/" + group_id + "/children", status_code=400)
    r = s.groups.children(group_id=group_id, query_params= query_params, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed query parameters."

def test_get_all_groups(requests_mock):
    requests_mock.register_uri("GET", url + "/groups", json=group_id, status_code=200)
    r = s.groups.get_all(query_params=None, token=token)
    assert r.error.status == 0
    assert group_id == r.value

def test_get_all_groups_malformed_query(requests_mock):
    requests_mock.register_uri("GET", url + "/groups", json=group_id, status_code=400)
    r = s.groups.get_all(query_params=None, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed query parameters."

def test_update_group(requests_mock):
    requests_mock.register_uri("PUT", url + "/groups/" + group_id, json=group, status_code=200)
    r = s.groups.update(group_id=group_id, group=group, token=token)
    assert r.error.status == 0

def test_update_group_server_error(requests_mock):
    requests_mock.register_uri("PUT", url + "/groups/" + group_id, json=group, status_code=500)
    r = s.groups.update(group_id=group_id, group=group, token=token)
    assert r.error.status == 1
    assert r.error.message == "Unexpected server-side error occurred."

def test_members(requests_mock):
    requests_mock.register_uri("GET", url + "/groups/" + group_id + "/members",json=group_id, status_code=200)
    r = s.groups.members(group_id=group_id, query_params=None, token=token)
    assert r.error.status == 0

def test_members_bad_content_type(requests_mock):
    requests_mock.register_uri("GET", url + "/groups/" + group_id + "/members", status_code=415)
    r = s.groups.members(group_id=group_id, query_params=None, token=token)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid content type."

def test_membership(requests_mock):
    requests_mock.register_uri("GET", url + "/users/" + member_id + "/memberships", json=members_ids, status_code=200)
    r = s.groups.memberships(member_id=member_id, query_params=query_params, token=token)
    assert r.error.status == 0

def test_membership_bad_content_type(requests_mock):
    requests_mock.register_uri("GET", url + "/users/" + member_id + "/memberships", status_code=400)
    r = s.groups.memberships(member_id=member_id, query_params=query_params, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed query parameters."

def test_assign(requests_mock):
    requests_mock.register_uri("POST", url + "/users/policies" , status_code=200)
    r = s.groups.assign(group_id=group_id, token=token, members_ids=members, member_type= ["m_read"])
    assert r.error.status == 0

def test_assign_malformed_json(requests_mock):
    requests_mock.register_uri("POST", url + "/users/policies", status_code=400)
    r = s.groups.assign(group_id=group_id, token=token, members_ids=members, member_type= ["m_read"])
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed JSON."

def test_unassign(requests_mock):
    requests_mock.register_uri("DELETE", url + "/users/policies" + "/" + members_ids + "/" + group_id, json=group, status_code=204)
    r = s.groups.unassign(group_id=group_id, members_ids=members_ids, token=token)
    assert r.error.status == 0
    
def test_unassign_bad_token(requests_mock):
    requests_mock.register_uri("DELETE", url + "/users/policies" + "/" + members_ids + "/" + group_id, status_code=403)
    r = s.groups.unassign(group_id=group_id, token=token, members_ids=members_ids)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_delete_group(requests_mock):
    requests_mock.register_uri("POST", url + "/groups/" + group_id + "/disable", status_code=200)
    r = s.groups.disable(group_id=group_id, user_token=token)
    assert r.error.status == 0

def test_delete_group_does_not_exist(requests_mock):
    requests_mock.register_uri("POST", url + "/groups/" + group_id + "/disable", status_code=404)
    r = s.groups.disable(group_id=group_id, user_token=token)
    assert r.error.status == 1
    assert r.error.message == "Group does not exist."

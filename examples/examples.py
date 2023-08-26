from mainflux import sdk

default_url = "http://localhost"

mfsdk = sdk.SDK(
    users_url=default_url,
    things_url=default_url + ":9000",
    reader_url=default_url + ":9204",
    http_adapter_url=default_url,
    certs_url=default_url + ":9019",
    bootstrap_url=default_url + ":9013",
    auth_url=default_url,
)

"""To start working with the Mainflux system,
you need to create a user account"""
mf_resp = mfsdk.users.create(
    user={"credentials": {"identity": "<user_identity>", "secret": "<user_secret>"}},
    token="",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
  
"""To log in to the Mainflux system, you need to create a user token"""
mf_resp = mfsdk.users.login(
    user={ "identity" : "admin@example.com", "secret": "12345678"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Refreshes Access and Refresh Token used for authenticating into the system."""

mf_resp = mfsdk.users.refresh_token(
    refresh_token="<refresh_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can always check the user entity that is logged in
by entering the user ID and token"""
mf_resp = mfsdk.users.get(user_id="<user_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates user entities in the database"""
user = {
    "id": "<user_id>",
    "name": "<user_name>",
    "metadata": {
        "foo": "bar"
    }
}
mf_resp = mfsdk.users.update(user_token="<token>", user=user)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates user identity in the database"""
user = {
  "credentials": {
    "identity": "<new_user_identity>",
  },
  "id": "<user_id>"
}
mf_resp = mfsdk.users.update_user_identity(user_token="<token>", user=user)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates user tags in the database"""
user = {
  "id": "<user_id>",
  "name": "<user_name>",
  "tags": [
    "yellow",
    "orange"
  ]
}
mf_resp = mfsdk.users.update_user_tags(user_token="<token>", user=user)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates user owner in the database"""
user = {
  "credentials": {
    "identity": "<user_identity>",
    "secret": "<secret>"
  },
  "id": "<user_id>",
  "owner": "<owner_id>"
}
mf_resp = mfsdk.users.update_user_owner(user_token="<token>", user=user)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""User Password reset request"""
mf_resp = mfsdk.users.reset_password_request(email= "<email>", url= "<url>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""User Password reset with the reset_request token"""
mf_resp = mfsdk.users.reset_password(password="<password>", confirm_password="<confirm_password>", token= "<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all users in the database by calling the get_all () function"""
mf_resp = mfsdk.users.get_all(
    query_params={"offset": 0, "limit": 5},
    user_token="<token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""Disables user"""
mf_resp = mfsdk.users.disable(user_id="<user_id>", user_token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""Enables user"""
mf_resp = mfsdk.users.enable(user_id="<user_id>", user_token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Changing the user password can be done by calling the update password function"""
mf_resp = mfsdk.users.update_password(
    old_secret="<old_secret>", new_secret="<new_secret>",
    user_token="<user_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Authorising a User"""
access_request = {
    "subject": "<user_id>",
    "object": "<group_id>",
    "action": "<action>",
    "entity_type": "<entity_type>"
}
mf_resp = mfsdk.users.authorise_user(access_request=access_request, token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Authorising a Thing"""
access_request = {
    "subject": "<thing_id>",
    "object": "<channel_id>",
    "action": "<action>",
    "entity_type": "<entity_type>"
}
mf_resp = mfsdk.things.authorise_thing(access_request=access_request, token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To create a thing, you need the thing name and a user token"""
mf_resp = mfsdk.things.create(
    thing={"name": "<thing_name>"}, token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can create multiple things at once
by entering a series of things structures and a user token"""
mf_resp = mfsdk.things.create_bulk(
    things=[{"name": "<thing_name>"}, {"name": "<thing_name>"}, {"name": "<thing_name>"}],
    token="<token>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get thing information by entering the thing ID and user token"""
mf_resp = mfsdk.things.get(thing_id= "<thing_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all things in the database by calling the get_all () function"""
mf_resp = mfsdk.things.get_all(
    query_params={"offset": 0, "limit": 5}, token="<token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates a thing entity in a database"""
mf_resp = mfsdk.things.update(
    thing_id="<thing_id>", token="<token>", thing={"name": "<thing_name>"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates a thing secret in a database"""
mf_resp = mfsdk.things.update_thing_secret(
    thing_id="<thing_id>", token="<token>", thing={"secret": "<thing_secret>"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates a thing's tags in a database"""
thing=  {
    "id": "<thing_id>",
    "name": "<thing_name>",
    "tags": [
    "dev","back"
    ]
  }
mf_resp = mfsdk.things.update_thing_tags(
    thing_id="<thing_id>", token="<token>", thing=thing
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates a thing's owner"""
thing=  {
    "id": "<thing_id>",
    "name": "<thing_name>",
    "owner": "<owner_id>",
}
mf_resp = mfsdk.things.update_thing_owner(
    thing_id="<thing_id>", token="<token>", thing=thing
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all thing connected to channel"""
mf_resp = mfsdk.things.get_by_channel(
    channel_id="<channel_id>",
    query_params={"offset": 1, "limit": 5},
    token="<user_token>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To disable a thing you need a thing ID and a user token"""
mf_resp = mfsdk.things.disable(thing_id="<thing_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Connect thing to channel"""
mf_resp = mfsdk.things.connect(
    channel_id="4921c9f2-6b7b-4291-98bf-fefd4a43591d", thing_id="d58ca9f5-e5f1-4a1b-9063-0c31ff9ba298", action="m_read", token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI5MzI0MjMsImlhdCI6MTY5Mjg3ODQyMywiaWRlbnRpdHkiOiJkZXRlcm1pbmVkX3JvZW50Z2VuQGVtYWlsLmNvbSIsImlzcyI6ImNsaWVudHMuYXV0aCIsInN1YiI6IjVhN2M1NGExLTgzMzUtNDBiNy1hOTE3LTc2MmZmYmFmOGFkOSIsInR5cGUiOiJhY2Nlc3MifQ.s74K5y6k9Hjzhi3MNU0cX1U9lKpJiRUwrIBLWgw_fcXUeMUN9HAIidu0sWj-iGxI6c-KUUy993I9yNIBOrUqaw"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Disconnect thing from channel"""
mf_resp = mfsdk.things.disconnect(
    channel_id="<channel_id>", thing_id="<thing_id>", token="<token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Connect things to channels"""
mf_resp = mfsdk.things.connects(
    thing_ids=["<thing_id>", "<thing_id>"],
    channel_ids=["<channel_ids>"],
    actions="<action>",
    token="<token>",
)

if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Disconnect things from channels"""
mf_resp = mfsdk.things.disconnects(
    thing_ids=["<thing_id1>", "<thing_id2>"],
    channel_ids=["<channel_id1>", "<channel_id2>"],
    token="<user_token>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Share thing"""
mf_resp = mfsdk.things.share_thing(
    channel_id= "<channel_id>", 
    user_id= "<user_id>", 
    actions= ["<actions>"], 
    token= "<admin_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message) 

"""To create a channel, you need a channel and a token"""
mf_resp = mfsdk.channels.create(
    channel={"name": "<channel_name>"}, token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""As with things, you can create multiple channels at once"""
mf_resp = mfsdk.channels.create_bulk(
    channels=[{"name": "<channel_name>"}, {"name": "<channel_name>"}],
    token="<token>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""Update channel entities in the database"""
mf_resp = mfsdk.channels.update(
    channel_id="<channel_id>",
    token="<token>",
    channel={"name": "<channel_name>"},
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get channel information by entering the channel ID and user token"""
mf_resp = mfsdk.channels.get(token="<token>", channel_id="<channel_id>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all channels in the database by calling the get_all ()
function"""
mf_resp = mfsdk.channels.get_all(
    query_params={"offset": 0, "limit": 5}, token="<token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""A list of all the channels to which a given thing is connected"""
mf_resp = mfsdk.channels.get_by_thing(
    thing_id="<thing_id>", query_params={"offset": 0, "limit": 5},
    token="<token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Identifies thing when given thing key"""
mf_resp = mfsdk.channels.identify_thing(thing_key="<thing_secret>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Delete channels from the database"""
mf_resp = mfsdk.channels.disable(
    channel_id="<channel_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To create a group, you need the group name and a user token"""
mf_resp = mfsdk.groups.create(
    group={"name": "group_auth", "parent_id": ""}, token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get group information by entering the group ID and token"""
mf_resp = mfsdk.groups.get(group_id="<group_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Group update"""
group={
    "id": "<group_id>",
    "name": "<group_name>"
}
mf_resp = mfsdk.groups.update(
    token="<token>", group= group, group_id="group_id"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get groups in the database by calling the get_all () function"""
mf_resp = mfsdk.groups.get_all(
    token="<token>", query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Assign user, thing or channel to a group"""
mf_resp = mfsdk.groups.assign(
    group_id="<object>",
    token="<token>",
    members_ids="<subject>",
    member_type=["<actions>"],
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Unassign"""
mf_resp = mfsdk.groups.unassign(
    group_id="<object>",
    token="<token>",
    members_ids="<subject>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of children from group"""
mf_resp = mfsdk.groups.children(
    group_id="<group_id>", token="<token>",
    query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of parents from group"""
mf_resp = mfsdk.groups.parents(
    group_id="<group_id>", token="<token>",
    query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of members from group"""
mf_resp = mfsdk.groups.members(
    group_id="<group_id>", token="<token>",
    query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of memberships from member"""
mf_resp = mfsdk.groups.memberships(
    member_id="<member_id>",
    token="<token>",
    query_params={"offset": 0, "limit": 5},
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Delete group from the database"""
mf_resp = mfsdk.groups.disable(group_id="<group_id>", user_token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Sends message via HTTP protocol"""
mf_resp = mfsdk.messages.send(
    channel_id="<channel_id>", msg="<[message]>", thing_key="<thing_secret>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Reads messages from database for a given channel"""
mf_resp = mfsdk.messages.read(channel_id="<channel_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Issue certs"""
mf_resp = mfsdk.certs.issue(thing_id="<thing_id>",valid="10h", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
 
"""View Certs"""
mf_resp = mfsdk.certs.view_by_thing(thing_id="<thing_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""View Certs"""
mf_resp = mfsdk.certs.view_by_serial(cert_id="<cert_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Revoke Certs"""
mf_resp = mfsdk.certs.revoke(thing_id="<thing_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Adds new config to the list of config owned by user identified using the provided access token."""
config = {
   "external_id": "<external_id>",
  "external_key": "<external_key>",
  "thing_id": "<thing_id>",
  "name": "<name>"
}
mf_resp = mfsdk.bootstrap.add(config=config, token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""Updating state represents enabling/disabling Config, i.e.connecting and disconnecting corresponding Mainflux Thing to the list of Channels."""
config = {
   "external_id": "<external_id>",
  "external_key": "<external_key>",
  "thing_id": "<thing_id>",
  "name": "<name>"
}
mf_resp = mfsdk.bootstrap.whitelist(config=config, token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message) 
 
"""Retrieves a configuration with given config id"""
mf_resp = mfsdk.bootstrap.view(thing_id= "<thing_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)  
  
"""Update is performed by replacing the current resource data with values provided in a request payload. Note that the owner, ID, external ID, external key, Mainflux Thing ID and key cannot be changed."""
config = {
 "external_id": "<external_id>",
  "external_key": "<external_key>",
  "thing_id": "<thing_id>",
  "name": "<name>"
}
mf_resp = mfsdk.bootstrap.update(config=config, token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message) 
   
"""Retrieves a configuration with given external ID and external key."""
mf_resp = mfsdk.bootstrap.bootstrap(external_id="<external_id>", external_key= "<external_key>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Removes a Config. In case of successful removal the service will ensure that the removed config is disconnected from all the Mainflux channels."""
mf_resp = mfsdk.bootstrap.remove(config_id= "<config_id>", token="<token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

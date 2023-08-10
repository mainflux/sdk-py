from mainflux import sdk

default_url = "http://localhost"

mfsdk = sdk.SDK(
    users_url=default_url,
    things_url=default_url,
    reader_url=default_url + ":9204",
    http_adapter_url=default_url,
    certs_url=default_url + ":8204",
    bootstrap_url=default_url + ":8202",
    auth_url=default_url,
)

"""To start working with the Mainflux system,
you need to create a user account"""
mf_resp = mfsdk.users.create(
    user={"email": "<user_email>", "password": "<user_password>"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To log in to the Mainflux system, you need to create a user token"""
mf_resp = mfsdk.users.login(
    user={"email": "<user_email>", "password": "<user_password>"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can always check the user entity that is logged in
by entering the user ID and token"""
mf_resp = mfsdk.users.get(id="<user_id>", token="<user_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updating user entities in the database"""
mf_resp = mfsdk.users.update(
    user_token="<user_token>", user={"metadata": {"foo": "bar"}}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all users in the database by calling the get_all () function"""
mf_resp = mfsdk.users.get_all(
    query_params={"offset": 1, "limit": 5}, admin_token="<admin_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

mf_resp = mfsdk.users.disable(user_id="<user_id>", admin_token="<admin_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)


mf_resp = mfsdk.users.enable(user_id="<user_id>", admin_token="<admin_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Changing the user password can be done by calling
the update password function"""
mf_resp = mfsdk.users.update_password(
    old_password="<old_password>", password="<new_password>",
    user_token="<user_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To create a thing, you need the thing name and a user token"""
mf_resp = mfsdk.things.create(
    thing={"name": "<thing_name>"}, token="<user_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can create multiple things at once
by entering a series of things structures and a user token"""
mf_resp = mfsdk.things.create_bulk(
    things=[{"name": "<thing_name_1>"}, {"name": "<thing_name_2>"}],
    token="<user_token>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get thing information by entering the thing ID and user token"""
mf_resp = mfsdk.things.get(token="<user_token>", thing_id="<thing_id>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all things in the database by calling the get_all () function"""
mf_resp = mfsdk.things.get_all(
    query_params={"offset": 1, "limit": 5}, token="<user_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updating a thing entity in a database"""
mf_resp = mfsdk.things.update(
    thing_id="<thing_id>", token="<user_token>", thing={"name": "<thing_name>"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)


"You can get all thing connected to channel"
mf_resp = mfsdk.things.get_by_channel(
    channel_id="<channel_id>",
    query_params={"offset": 1, "limit": 5},
    token="<user_token>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To delete a thing you need a thing ID and a user token"""
mf_resp = mfsdk.things.delete(thing_id="<thing_id>", token="<user_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Connect thing to channel"""
mf_resp = mfsdk.things.connect(
    channel_id="<channel_id>", thing_id="<thing_id>", token="<user_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Disconnect thing from channel"""
mf_resp = mfsdk.things.disconnect(
    channel_id="<channel_id>", thing_id="<thing_id>", token="<user_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Connect things to channels"""
mf_resp = mfsdk.things.connects(
    channel_ids=["<channel_id1>", "<channel_id2>"],
    thing_ids=["<thing_id1>", "<thing_id2>"],
    token="<user_token>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Disconnect things from channels"""
mf_resp = mfsdk.things.disconnects(
    channel_ids=["<channel_id1>", "<channel_id2>"],
    thing_ids=["<thing_id1>", "<thing_id2>"],
    token="<user_token>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To create a channel, you need a channel and a token"""
mf_resp = mfsdk.channels.create(
    channel={"name": "channel_name"}, token="<user_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""As with things, you can create multiple channels at once"""
mf_resp = mfsdk.channels.create_bulk(
    channels=[{"name": "<channel_name_1>"}, {"name": "<channel_name_2>"}],
    token="<user_token>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Update channel entities in the database"""
mf_resp = mfsdk.channels.update(
    channel_id="<channel_id>",
    token="<user_token>",
    channel={"name": "<channel_name_3>"},
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get channel information by entering the channel ID and user token"""
mf_resp = mfsdk.channels.get(token="<user_token>", channel_id="<channel_id>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all channels in the database by calling the get_all ()
function"""
mf_resp = mfsdk.channels.get_all(
    query_params={"offset": 1, "limit": 5}, token="<user_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""A list of all the channels to which a given thing is connected"""
mf_resp = mfsdk.channels.get_by_thing(
    thing_id="<thing_id>", query_params={"offset": 1, "limit": 5},
    token="<user_token>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Identifies thing when given thing key"""
mf_resp = mfsdk.channels.identify_thing(thing_key="<thing_id>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Delete channels from the database"""
mf_resp = mfsdk.channels.delete(
    channel_id="<channel_id>", token="<user_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To create a group, you need the group name and a user token"""
mf_resp = mfsdk.groups.create(
    group={"name": "group_name"}, token="<user_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get group information by entering the group ID and token"""
mf_resp = mfsdk.groups.get(group_id="<group_id>", token="<user_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Group update"""
mf_resp = mfsdk.groups.update(
    group_id="<group_id>", token="<user_token>", group={"<metadata>"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get groups in the database by calling the get_all () function"""
mf_resp = mfsdk.groups.get_all(
    token="<user_token>", query_params={"offset": 1, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Assign user, thing or channel to a group"""
mf_resp = mfsdk.groups.assign(
    group_id="<group_id>",
    token="<user_token>",
    members_ids=["<user_id>" | "<thing_id_>" | "<channel_id_>"],
    member_type='<"users" | "things" | "channels">',
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Unassign"""
mf_resp = mfsdk.groups.unassign(
    group_id="<group_id>",
    token="<user_token>",
    members_ids=["<user_id>" | "<thing_id_>" | "<channel_id_>"],
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of children from group"""
mf_resp = mfsdk.groups.children(
    group_id="<group_id>", token="<user_token>",
    query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of parents from group"""
mf_resp = mfsdk.groups.parents(
    group_id="<group_id>", token="<user_token>",
    query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of members from group"""
mf_resp = mfsdk.groups.members(
    member_id="<thing_id>", token="<user_token>",
    query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of memberships from member"""
mf_resp = mfsdk.groups.memberships(
    group_id="<member_id>",
    token="<user_token>",
    query_params={"offset": 0, "limit": 5},
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Delete group from the database"""
mf_resp = mfsdk.groups.delete(group_id="<group_id>", token="<user_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Sends message via HTTP protocol"""
mf_resp = mfsdk.messages.send(
    channel_id="<channel_id>", msg="<msg>", thing_key="<thing_key>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Reads messages from database for a given channel"""
mf_resp = mfsdk.messages.read(channel_id="<channel_id>", token="<user_token>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

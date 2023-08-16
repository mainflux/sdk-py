from mainflux import sdk

default_url = "http://localhost"

mfsdk = sdk.SDK(
    users_url=default_url,
    things_url=default_url + ":9000",
    reader_url=default_url + ":9204",
    http_adapter_url=default_url,
    certs_url=default_url + ":8204",
    bootstrap_url=default_url + ":8202",
    auth_url=default_url,
)
'''
"""To start working with the Mainflux system,
you need to create a user account"""
mf_resp = mfsdk.users.create(
    user={"credentials": {"identity": "example23@example.com", "secret": "12345678"}},
    token="",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)  

"""To log in to the Mainflux system, you need to create a user token"""
mf_resp = mfsdk.users.login(
    user={ "identity" : "example23@example.com", "secret": "12345678"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
'''
"""You can always check the user entity that is logged in
by entering the user ID and token"""
mf_resp = mfsdk.users.get(user_id="0f047968-b170-4dd4-85f5-6e03e1b3798e", token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTE3NTIxOTcsImlhdCI6MTY5MTc1MTI5NywiaWRlbnRpdHkiOiJleGFtcGxlMTJAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiIwZjA0Nzk2OC1iMTcwLTRkZDQtODVmNS02ZTAzZTFiMzc5OGUiLCJ0eXBlIjoiYWNjZXNzIn0.REa8wv-veZm2fpAeLe3jO9SMYMnyPrcT07YTmx4M_lOE3wYYal26HYp8RHd6z3Igy7ccadSKiqaygyvrpkMLzw")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
'''
"""Updating user entities in the database"""
user = {
    "id": "",
    "name": "",
    "metadata": {
        "foo": "bar"
    }
}
mf_resp = mfsdk.users.update(
    user_token="", user=user
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
'''
"""You can get all users in the database by calling the get_all () function"""
mf_resp = mfsdk.users.get_all(
    query_params={"offset": 0, "limit": 5},
    admin_token="",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
'''
mf_resp = mfsdk.users.disable(user_id="46c266a8-084d-4863-b013-9d27be7617e5", user_token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTE4MTIxMjQsImlhdCI6MTY5MTc1ODEyNCwiaWRlbnRpdHkiOiJleGFtcGxlMTVAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiJhZTE4ZjZiZS01OTJmLTQ1NjAtOGIxNy1jMmUxYmYyNzNhYWUiLCJ0eXBlIjoiYWNjZXNzIn0.SO3Z6-mNbYFEuJDlO1E477nQblg0UR6r0C7aR8jhRcTpDA62isovYjXhdoDdjPrRrDb7K1hHSHrxHhMFPiYz7w")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

mf_resp = mfsdk.users.enable(user_id="46c266a8-084d-4863-b013-9d27be7617e5", user_token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTE4MTIxMjQsImlhdCI6MTY5MTc1ODEyNCwiaWRlbnRpdHkiOiJleGFtcGxlMTVAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiJhZTE4ZjZiZS01OTJmLTQ1NjAtOGIxNy1jMmUxYmYyNzNhYWUiLCJ0eXBlIjoiYWNjZXNzIn0.SO3Z6-mNbYFEuJDlO1E477nQblg0UR6r0C7aR8jhRcTpDA62isovYjXhdoDdjPrRrDb7K1hHSHrxHhMFPiYz7w")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Changing the user password can be done by calling
the update password function"""
'''
"""
mf_resp = mfsdk.users.update_password(
    old_secret="", secret="",
    user_token=""
)

if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
"""
'''
"""To create a thing, you need the thing name and a user token"""
mf_resp = mfsdk.things.create(
    thing={"name": "thing1"}, token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can create multiple things at once
by entering a series of things structures and a user token"""
mf_resp = mfsdk.things.create_bulk(
    things=[{"name": "thing_8"}, {"name": "thing_9"}, {"name": "thing_10"}],
    token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get thing information by entering the thing ID and user token"""
mf_resp = mfsdk.things.get(token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ", thing_id="6d591627-8657-43af-bfaa-79047b5f8ec3")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all things in the database by calling the get_all () function"""
mf_resp = mfsdk.things.get_all(
    query_params={"offset": 0, "limit": 5}, token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updating a thing entity in a database"""
mf_resp = mfsdk.things.update(
    thing_id="6d591627-8657-43af-bfaa-79047b5f8ec3", token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ", thing={"name": "thing_1"}
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

"""To disable a thing you need a thing ID and a user token"""
mf_resp = mfsdk.things.disable(thing_id="2ad76a79-640b-44c3-ab1c-3894d4013391", token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Connect thing to channel"""
mf_resp = mfsdk.things.connect(
    channel_id="2b7ff10e-9294-47a9-a66b-e8f7de7c5a8b", thing_id="6d591627-8657-43af-bfaa-79047b5f8ec3", action="m_read", token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Disconnect thing from channel"""
mf_resp = mfsdk.things.disconnect(
    channel_id="2b7ff10e-9294-47a9-a66b-e8f7de7c5a8b", thing_id="6d591627-8657-43af-bfaa-79047b5f8ec3", token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Connect things to channels"""
mf_resp = mfsdk.things.connects(
    thing_ids=["769c8d58-bc7e-4003-8e5b-84301534ba7f", "a937d27a-b0aa-4e4f-a85e-bb95bf0ac1bf"],
    channel_ids=["6a4c094d-b192-4e7b-837f-6d2a2bae12d5"],
    action="m_read",
    token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ",
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

"""To create a channel, you need a channel and a token"""
mf_resp = mfsdk.channels.create(
    channel={"name": "channel_3"}, token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""As with things, you can create multiple channels at once"""
mf_resp = mfsdk.channels.create_bulk(
    channels=[{"name": "channel_6"}, {"name": "channel_7"}],
    token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""Update channel entities in the database"""
mf_resp = mfsdk.channels.update(
    channel_id="2b7ff10e-9294-47a9-a66b-e8f7de7c5a8b",
    token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ",
    channel={"name": "channel_3"},
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
'''
"""You can get channel information by entering the channel ID and user token"""
mf_resp = mfsdk.channels.get(token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ", channel_id="2b7ff10e-9294-47a9-a66b-e8f7de7c5a8b")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all channels in the database by calling the get_all ()
function"""
mf_resp = mfsdk.channels.get_all(
    query_params={"offset": 0, "limit": 5}, token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""A list of all the channels to which a given thing is connected"""
mf_resp = mfsdk.channels.get_by_thing(
    thing_id="2ad76a79-640b-44c3-ab1c-3894d4013391", query_params={"offset": 0, "limit": 5},
    token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)


"""Identifies thing when given thing key"""
mf_resp = mfsdk.channels.identify_thing(thing_key="a0c5471a-b7a6-4337-81af-b6113f41d898", user_token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    

"""Delete channels from the database"""
mf_resp = mfsdk.channels.disable(
    channel_id="2b7ff10e-9294-47a9-a66b-e8f7de7c5a8b", token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIwNTUxNzIsImlhdCI6MTY5MjAwMTE3MiwiaWRlbnRpdHkiOiJleGFtcGxlMTlAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI2OWFkNjk0Ny0xZGQ1LTRmNzItYTQ3NC1kMGZmNDE0MTUyYTEiLCJ0eXBlIjoiYWNjZXNzIn0.mlfRaQG69XmKUei9KW2287Kvk7_EiuAVeGbmq9aojA2FzzoicRxsTWkwEJGuhwWBHxQgBMe99j5rdb6EbJHkWQ")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
'''
"""To create a group, you need the group name and a user token"""
mf_resp = mfsdk.groups.create(
    group={"name": "group_2"}, token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get group information by entering the group ID and token"""
mf_resp = mfsdk.groups.get(group_id="1705dbd3-e542-4a38-8bef-aa7c33bdcf2d", token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
'''
"""Group update"""
#group= {
#  "name": "group_1",
#  "description": "",
#  "metadata": {
#    "role": "general"
#  }
#}
mf_resp = mfsdk.groups.update(

    group_id="1705dbd3-e542-4a38-8bef-aa7c33bdcf2d", token="yJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ", group={"name: group_nat"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
'''
"""You can get groups in the database by calling the get_all () function"""
mf_resp = mfsdk.groups.get_all(
    token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ", query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
# """Assign user, thing or channel to a group"""
# mf_resp = mfsdk.groups.assign(
#     group_id="<group_id>",
#     token="<user_token>",
#     members_ids=["<user_id>" | "<thing_id_>" | "<channel_id_>"],
#     member_type='<"users" | "things" | "channels">',
# )
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# """Unassign"""
# mf_resp = mfsdk.groups.unassign(
#     group_id="<group_id>",
#     token="<user_token>",
#     members_ids=["<user_id>" | "<thing_id_>" | "<channel_id_>"],
# )
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# """Get list of children from group"""
# mf_resp = mfsdk.groups.children(
#     group_id="<group_id>", token="<user_token>",
#     query_params={"offset": 0, "limit": 5}
# )
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# """Get list of parents from group"""
# mf_resp = mfsdk.groups.parents(
#     group_id="<group_id>", token="<user_token>",
#     query_params={"offset": 0, "limit": 5}
# )
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# """Get list of members from group"""
# mf_resp = mfsdk.groups.members(
#     member_id="<thing_id>", token="<user_token>",
#     query_params={"offset": 0, "limit": 5}
# )
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# """Get list of memberships from member"""
# mf_resp = mfsdk.groups.memberships(
#     group_id="<member_id>",
#     token="<user_token>",
#     query_params={"offset": 0, "limit": 5},
# )
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)
'''
"""Delete group from the database"""
mf_resp = mfsdk.groups.disable(group_id="29474bea-a8d6-4e5c-9336-5de0c8ca9aaf", user_token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTIxNDM0MTEsImlhdCI6MTY5MjA4OTQxMSwiaWRlbnRpdHkiOiJleGFtcGxlMjBAZXhhbXBsZS5jb20iLCJpc3MiOiJjbGllbnRzLmF1dGgiLCJzdWIiOiI4N2MxZTY5MC1kMDFhLTRhN2YtOGYyNy0xZjhhOWE2ZGIwMmUiLCJ0eXBlIjoiYWNjZXNzIn0.BgXBpOdkOP6s2QMLdzv4jHsl3rX16ZkA_r34BS4wL8UA_xr5gWxeyqaNL8x9tkNNRz4RML40Lo2lGtd2sMvVZQ")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
'''
# """Sends message via HTTP protocol"""
# mf_resp = mfsdk.messages.send(
#     channel_id="<channel_id>", msg="<msg>", thing_key="<thing_key>"
# )
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# """Reads messages from database for a given channel"""
# mf_resp = mfsdk.messages.read(channel_id="<channel_id>", token="<user_token>")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

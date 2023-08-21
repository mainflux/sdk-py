from mainflux import users
from mainflux import things
from mainflux import messages
from mainflux import channels
from mainflux import groups
from mainflux import boostrap
from mainflux import certs

import requests

default_url = "http://localhost"


class SDK:
    def __init__(
        self,
        users_url=default_url,
        things_url=default_url,
        reader_url=default_url,
        http_adapter_url=default_url,
        certs_url=default_url,
        bootstrap_url=default_url,
        auth_url=default_url,
    ):
        self.users = users.Users(users_url)
        self.things = things.Things(things_url)
        self.messages = messages.Messages(
            adapter_url=http_adapter_url, reader_url=reader_url
        )
        self.channels = channels.Channels(things_url)
        self.groups = groups.Groups(auth_url)
        self.bootstrap = boostrap.Bootstrap(bootstrap_url)
        self.certs = certs.Certs(certs_url)
        self.version_url = things_url

    def version(self):
        response = requests.get(self.version_url + "/version")
        return response.json()

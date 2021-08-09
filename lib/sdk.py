from lib import users
from lib import things
from lib import messages
from lib import channels
from lib import groups

import requests

default_url = "http://localhost"


class SDK:
    def __init__(
        self,
        users_url=default_url,
        things_url=default_url,
        messages_url=default_url,
        groups_url=default_url
    ):
        self.users = users.Users(users_url)
        self.things = things.Things(things_url)
        self.messages = messages.Messages(messages_url)
        self.channels = channels.Channels(things_url)
        self.groups = groups.Groups(groups_url)
        self.version_url = things_url

    def version(self):
        response = requests.get(self.version_url + "/version")
        return response.json()

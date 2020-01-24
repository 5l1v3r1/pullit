"""
This file is just the boot method to load some stuff
Do not edit this file, it could break pullit
"""
from ruamel import yaml
from modules.core.notifications import Notifications


class Boot:

    # Boot constructor
    def __init__(self):
        self.config = yaml.safe_load(open('./config.yml'))
        self.notifications = Notifications()


boot = Boot()

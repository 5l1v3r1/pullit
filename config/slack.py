from modules.core.config import *


class Slack:

    # Return the slack token
    @staticmethod
    def token():
        return config['SLACK']['token']

    # Return the slack channel
    @staticmethod
    def channel():
        return config['SLACK']['channel']

    # Is slack enabled?
    @staticmethod
    def enabled():
        return config['SLACK']['enabled']


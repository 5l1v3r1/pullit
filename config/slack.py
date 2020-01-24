from modules.core.config import *


class Slack:

    # Return the slack config
    @staticmethod
    def get():
        return config['SLACK']


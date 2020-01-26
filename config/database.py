from modules.core.config import *


class Database:

    # Name of the database to use
    @staticmethod
    def database():
        return "%s.sqlite" % config['DATABASE']['name']

    # Should we save checked repos?
    @staticmethod
    def save_checked():
        return config['DATABASE']['save_checked']

    # Should we save found credentials?
    @staticmethod
    def save_found():
        return config['DATABASE']['save_found']
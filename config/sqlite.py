from modules.core.config import *


class Sqlite:

    # Return the SQLITE database
    @staticmethod
    def get():
        return config['SQLITE']


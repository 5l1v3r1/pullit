import sqlite3
from config.sqlite import Sqlite


class Sqlite:

    # Instance of sqlite
    instance = ''

    # Connect to the database
    @staticmethod
    def __init__(self):
        if not self.instance:
            self.instance = sqlite3.connect(Sqlite.get())

    # Return the instance
    def get(self):
        return self.instance


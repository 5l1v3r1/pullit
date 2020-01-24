import sqlite3
from config.sqlite import Sqlite


class Sqlite:

    # Instance of sqlite
    instance = ''

    # Connect to the database
    def __init__(self):
        if not self.instance:
            print("here")
            self.instance = sqlite3.connect(Sqlite.get())

        print("fjffjfjf")

    # Return the instance
    @staticmethod
    def get(self):
        print(self.instance)
        return self.instance


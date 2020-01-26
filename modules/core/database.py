import sqlite3
from config.database import Database as Config


class Database:

    # Instance of sqlite
    instance = ''

    # Connect to the database
    def __init__(self):
        if not self.instance:
            self.instance = sqlite3.connect(Config.database())
            self.initalize()

    # Return the instance
    def get(self):
        return self.instance

    # Create the table structure
    def initalize(self):
        createRepositories = """
            CREATE TABLE IF NOT EXISTS repositories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar(32), 
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        createCredentials = """
            CREATE TABLE IF NOT EXISTS credentials(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                repository_id int, 
                match varchar(32), 
                name varchar(32), 
                credentials json, 
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        self.instance.cursor().execute(createRepositories)
        self.instance.cursor().execute(createCredentials)


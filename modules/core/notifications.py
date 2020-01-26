from modules.core.events import Events
from modules.core.slack import Slack
from modules.core.mail import Mail
from modules.github.repositories import Repositories
from modules.core.database import Database
from config.database import Database as Config
import json


class Notifications:

    # Notifications constructor
    def __init__(self):
        self.repo_id = ''
        self.github = Repositories()
        self.connection = Database().get()
        Events.listen(Events, 'checked-repo', self.checked)
        Events.listen(Events, 'regex-found', self.slack)
        Events.listen(Events, 'extension-found', self.slack)
        Events.listen(Events, 'filename-found', self.slack)
        Events.listen(Events, 'regex-found', self.found)
        Events.listen(Events, 'extension-found', self.found)
        Events.listen(Events, 'filename-found', self.found)

    # Send information to slack
    def slack(self, payload):
        Slack().broadcast(payload)

    # Send information to an email
    def email(self, payload):
        Mail().broadcast(payload)

    # Add the repo checked database
    def checked(self, payload):
        if not Config.save_checked():
            return

        sql = """
            INSERT INTO repositories(
                name
            )
            VALUES(?)            
        """
        data = (payload['name'],)
        with self.connection as connection:
            cur = connection.cursor()
            cur.execute(sql, data)
            self.repo_id = cur.lastrowid

    # Store information in the database
    def found(self, payload):
        if not Config.save_found():
            return

        sql = """
            INSERT INTO credentials(
                repository_id,
                match, 
                name, 
                credentials
            )
            VALUES(?, ?, ?, ?)
        """
        data = (self.repo_id, payload['match'], payload['name'], payload['credentials'])

        with self.connection as connection:
            cur = connection.cursor()
            cur.execute(sql, data)

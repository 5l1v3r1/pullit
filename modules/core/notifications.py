from modules.core.events import Events
from modules.core.slack import Slack
from modules.core.mail import Mail

class Notifications:

    # Notifications constructor
    def __init__(self):
        Events.listen(Events, 'regex-found', self.slack)
        Events.listen(Events, 'extension-found', self.slack)
        Events.listen(Events, 'filename-found', self.slack)

    # Send information to slack
    def slack(self, payload):
        Slack().broadcast(payload)

    # Send information to an email
    def email(self, payload):
        Mail().broadcast(payload)

    # Store information in the database
    def database(self, payload):
        pass
        #print("Stored in the database", payload)
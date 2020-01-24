from modules.core.events import Events


class Notifications:

    # Notifications constructor
    def __init__(self):
        Events.listen(Events, 'regex-found', self.slack)
        Events.listen(Events, 'extension-found', self.slack)
        Events.listen(Events, 'filename-found', self.slack)

    # Send information to slack
    def slack(self, payload):
        pass
        #print("Sent to slack", payload)

    # Send information to an email
    def email(self, payload):
        pass
        #print("Sent to email", payload)

    # Store information in the database
    def database(self, payload):
        pass
        #print("Stored in the database", payload)
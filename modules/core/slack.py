import slack, json
from config.slack import Slack as Config


class Slack:

    # Slack constructor
    def __init__(self):
        self.client = slack.WebClient(token=Config.token())

    # Broadcast a message to slack
    def broadcast(self, payload):
        if not Config.enabled():
            return

        message = "Method: %s \n Matches: %s \n Found Credentials: %s \n Repository: %s" % (
            payload['name'],
            payload['match'],
            payload['credentials'],
            payload['repo'],
        )
        try:
            self.client.chat_postMessage(
                channel="#%s" % Config.channel(),
                text=message,
            )
        except Exception as e:
            return


from modules.github.authenticate import Authenticate


class Repositories:

    # Repositories constructor
    def __init__(self):
        self.authentication = Authenticate().get()

    # Get a list of repositories
    def get(self):
        return self.authentication.get_repos()

    # Check current rate limit
    def rate_limit(self):
        pass


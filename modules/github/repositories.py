from modules.github.authenticate import Authenticate
from config.keywords import Keywords


class Repositories:

    # Repositories constructor
    def __init__(self):
        self.keywords = Keywords
        self.authentication = Authenticate().get()

    # Get repo by name
    def get(self, name):
        return self.authentication.get_repo(name)

    # Get a list of repositories
    def all(self):
        return self.authentication.get_repos()

    # Search repos for keyword
    def search(self, keyword):
        return self.authentication.search_repositories(keyword)

    # Check current rate limit
    def rate_limit(self):
        pass


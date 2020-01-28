#!/usr/bin/env python3

from modules.core.git import Git
from config.metadata import Metadata
from modules.core.file import File
from modules.core.boot import Boot
from modules.github.repositories import Repositories
from config.threads import Threads
from config.keywords import Keywords
from functools import partial
from multiprocessing import Pool

logo = f"""
{'#' * 60}
#                                                          #
# Pullit: Created by @Filtration                           #
#                                                          #
# I take no responsibility for what you do with this tool  #
# It is more than likely illegal to use in your country    #
#                                                          #
{'#' * 60}
"""


class Pullit:

    # Pullit constructor
    def __init__(self):
        self.repos = []
        self.keywords = Keywords()
        self.repositories = Repositories()

    # Find credentials
    @staticmethod
    def find(repo):

        # todo
        # Database.done(repo)

        # Clone the repo
        Git.clone(repo, "https://github.com/%s.git" % repo)

        # Run the metadata on the repo
        for metadata in Metadata.get():
            if metadata['type'] == 'contents':
                File(repo).find_by_content(metadata)
            elif metadata['type'] == 'extension':
                File(repo).find_by_extension(metadata)
            elif metadata['type'] == 'filename':
                File(repo).find_by_name(metadata)

        # todo
        # Database.checked(repo)

        # Delete the repo
        Git.delete(repo)

    # Run on all repos
    def all(self, pool):
        for repo in self.repositories.all():
            self.repos.append(repo.full_name)
            if len(self.repos) >= Threads.get():
                function = partial(self.find)
                pool.map(function, self.repos)
                self.repos.clear()

    # Run on searched repos
    def search(self, pool):
        for keyword in self.keywords.get():
            for repo in self.repositories.search(keyword):
                self.repos.append(repo.full_name)
                if len(self.repos) >= Threads.get():
                    function = partial(self.find)
                    pool.map(function, self.repos)
                    self.repos.clear()

    # Run Pullit
    def main(self):
        # Pool connections to speed up our job
        with Pool(processes=Threads.get()) as pool:
            if self.keywords.get():
                self.search(pool)
            else:
                self.all(pool)


# Pullit logo
print(logo)

# Boot method (LEAVE ALONE)
Boot()

# Let's go!
Pullit().main()


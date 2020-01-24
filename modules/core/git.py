import os
from shutil import rmtree


class Git:

    # Clone a git repo
    # todo maybe use python
    @staticmethod
    def clone(name, url):
        os.system("git clone --single-branch --no-tags --depth 1 %s /tmp/pullit/git/%s > /dev/null 2>&1" % (url, name))

    # Delete the repo
    @staticmethod
    def delete(name):
        try:
            rmtree("/tmp/pullit/git/%s" % name)
        except FileNotFoundError:
            # I don't know why it would throw this but it does
            return

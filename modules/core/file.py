import glob, re
from modules.core.events import Events


class File:

    # File constructor
    def __init__(self, repo):
        self.repo = repo

    # Find a file by its content
    def find_by_content(self, pattern):
        for file in glob.glob("/tmp/pullit/git/%s/**/*.*" % self.repo.full_name, recursive=True):
            with open(file) as f:
                try:
                    for line in f:
                        for found in re.finditer(pattern, line):
                            print("File: %s contains: %s" % (file, found.string))
                            Events.emit(Events, 'regex-found')
                except UnicodeDecodeError:
                    return

    # Find a file by its extension
    def find_by_extension(self, match):
        for file in glob.glob("/tmp/pullit/git/%s/*%s" % (self.repo.full_name, match), recursive=True):
            print(file)
            Events.emit(Events, 'extension-found')

    # Find a file by its name
    def find_by_name(self, match):
        for file in glob.glob("/tmp/pullit/git/%s/%s" % (self.repo.full_name, match), recursive=True):
            print(file)
            Events.emit(Events, 'filename-found')


import glob, re, json
from modules.core.events import Events


class File:

    # File constructor
    def __init__(self, repo):
        self.repo = repo
        Events.emit(Events, 'checked-repo', {'name': repo})

    # Find a file by its content
    def find_by_content(self, metadata):
        for file in glob.glob("/tmp/pullit/git/%s/**/*.*" % self.repo, recursive=True):
            try:
                with open(file) as f:
                    try:
                        for line in f:
                            for pattern in metadata['match']:
                                for found in re.finditer(pattern, line):
                                    meta = {
                                        'name': metadata['name'],
                                        'match': pattern,
                                        'content': found.string
                                    }
                                    self.found(meta, 'regex-found')
                    except UnicodeDecodeError:
                        return
            except IsADirectoryError:
                return
            except FileNotFoundError:
                return

    # Find a file by its extension
    def find_by_extension(self, metadata):
        for file in glob.glob("/tmp/pullit/git/%s/*%s" % (self.repo, metadata['match']), recursive=True):
            meta = {
                'name': metadata['name'],
                'match': metadata['match'],
                'content': file
            }
            self.found(meta, 'extension-found')

    # Find a file by its name
    def find_by_name(self, metadata):
        for file in glob.glob("/tmp/pullit/git/%s/%s" % (self.repo, metadata['match']), recursive=True):
            meta = {
                'name': metadata['name'],
                'match': metadata['match'],
                'content': file
            }
            self.found(meta, 'filename-found')

    # We have found matching metadata
    def found(self, metadata, event):
        information = "Repo: %s contains: %s" % (self.repo, metadata['content'])
        payload = {
            'name': metadata['name'],
            'match': metadata['match'],
            'credentials': json.dumps(metadata['content']),
            'repo': self.repo
        }
        print(information)
        Events.emit(Events, event, payload)


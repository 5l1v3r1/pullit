import glob, os, re, json
from modules.core.events import Events
from config.files import Files


class File:

    # File constructor
    def __init__(self, repo):
        self.repo = repo
        Events.emit(Events, 'checked-repo', {'name': repo})

    # Find a file by its content
    def find_by_content(self, metadata):
        for root, dirs, files in os.walk("/tmp/pullit/git/%s" % self.repo):
            for file in files:
                for extension in Files.extensions():
                    if file.endswith(extension):
                        break
                try:
                    with open(os.path.join(root, file), 'r') as f:
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
                        except Exception as e:
                            break
                except:
                    break

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
        information = "%s" % metadata['content']
        payload = {
            'name': metadata['name'],
            'match': metadata['match'],
            'credentials': json.dumps(metadata['content']),
            'repo': self.repo
        }
        print(information)
        Events.emit(Events, event, payload)


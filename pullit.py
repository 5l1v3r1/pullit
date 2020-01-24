from modules.github.authenticate import Authenticate
from modules.core.git import Git
from config.metadata import Metadata
from modules.core.file import File

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
        self.auth = Authenticate().get()

    # Run pullit
    # todo: threading
    def main(self):

        # Loop through repos and find matches
        for repo in self.auth.get_repos():

            # Clone the repo
            Git.clone(repo.full_name, "https://github.com/%s.git" % repo.full_name)

            # Run the metadata on the repo
            for metadata in Metadata.get():
                if metadata['type'] == 'contents':
                    File(repo).find_by_content(metadata['match'])
                elif metadata['type'] == 'extension':
                    File(repo).find_by_extension(metadata['match'])
                elif metadata['type'] == 'filename':
                    File(repo).find_by_name(metadata['match'])

            # Delete the repo
            Git.delete(repo.full_name)


# Pullit logo
print(logo)

# Let's go!
Pullit().main()


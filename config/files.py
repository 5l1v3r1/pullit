from modules.core.config import *


class Files:

    # Blacklisted file paths
    @staticmethod
    def extensions():
        return config['FILES']['blacklisted']['extensions']

    # Blacklisted file paths
    @staticmethod
    def paths():
        return config['FILES']['blacklisted']['paths']
from modules.core.config import *


class Keywords:

    # Return a list of keywords to search
    @staticmethod
    def get():
        return config['KEYWORDS']


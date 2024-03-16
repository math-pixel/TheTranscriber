import os

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def getDirectoryAbsolutePath():
        return os.path.abspath(os.getcwd())
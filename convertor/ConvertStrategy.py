from DLog import *

class ConvertStrategy:
    def __init__(self):
        DLog.warning("Initialize strategy")
        pass

    def executeConversion(self, path):
        DLog.warning("Execute conversion")
        pass

class MP4ToMP3ConvertStrategy(ConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, path):
        super().executeConversion(path)
        # Execute some conversion from MP4 to MP3
        # and return the result path
        return path

class AviToMP3ConvertStrategy(ConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, path):
        super().executeConversion(path)
        # Execute some conversion from Avi to MP3
        # and return the result path
        return path
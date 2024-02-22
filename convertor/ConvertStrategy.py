from DLog import *

class ConvertStrategy:
    def __init__(self):
        DLog.warning("Initialize strategy")
        pass

    def executeConversion(self, trContext):
        DLog.warning("Execute conversion")
        pass

class MP4ToMP3ConvertStrategy(ConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)
        # Execute some conversion from MP4 to MP3
        # and return the result trContext
        return trContext

class AviToMP3ConvertStrategy(ConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)
        # Execute some conversion from Avi to MP3
        # and return the result trContext
        return trContext
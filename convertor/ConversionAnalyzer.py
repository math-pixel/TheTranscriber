from DLog import *
from convertor.ConvertStrategy import *


class ConversionAnalyzer:
    def __init__(self):
        pass

    def analyze(self, path, convertor):
        DLog.goodlog("Start analyze the file: " + path)
        # - Ce que je fais temporairement
        convertor.setConvertStrategy(MP4ToMP3ConvertStrategy())
        return True
        # - Ce qu'il peut être fait ensuite
        # ------
        # Ici on peut imaginer du code du genre
        # if path == mp4:
        #   self.convertor.setStrategy(MP4toMP3Strategy())
        #   Return True
        # ...
        # Et ainsi de suite pour pouvoir set la bonne "strategie"
        # Et si à la fin aucune stratégie n'est set, on return False
        pass

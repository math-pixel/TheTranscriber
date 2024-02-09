from convertor.Convertor import *
from convertor.ConversionAnalyzer import *
from DLog import *

class ConversionCoordinator:
    def __init__(self, analyzer, convertor):
        self.analyzer = analyzer
        self.convertor = convertor
        pass

    # Je le fais pas ici mais il est FORTEMENT probable qu'on ait de l'asynchronicité dans cette
    # fonction, donc il faudra sûrement passer une callback en paramètre, mais on verra ça plus tard
    def convert(self, path):
        # Ici on va 'set' comment est ce que le convertor va convertir le path (genre mp4 to mp3 ou jsp)
        # Et si la conversion doit ou non être réaliser
        needAnalyze = self.analyzer.analyze(path, self.convertor)
        if needAnalyze:
            DLog.goodlog("Will convert file : " + path)
            return self.convertor.convert(path)
        else:
            DLog.goodlog("Won't convert file : " + path)
            return path

    @staticmethod
    def getConversionCoordinator():
        return ConversionCoordinator(ConversionAnalyzer(), Convertor())




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
    def convert(self, trContext):
        # Ici on va 'set' comment est ce que le convertor va convertir le trContext (genre mp4 to mp3 ou jsp)
        # Et si la conversion doit ou non être réaliser
        needConversion = self.analyzer.analyze(trContext, self.convertor)
        if needConversion:
            DLog.goodlog("Will convert file")
            self.convertor.convert(trContext)
            return trContext
        else:
            DLog.goodlog("Won't convert file")
            return trContext

    @staticmethod
    def getConversionCoordinator():
        return ConversionCoordinator(ConversionAnalyzer(), Convertor())




from convertor.Convertor import *
from convertor.ConversionAnalyzer import *
from DLog import *

# This class is use to coordinate analyzer and convertor
class ConversionCoordinator:
    def __init__(self, analyzer, convertor):
        self.analyzer = analyzer
        self.convertor = convertor
        pass

    # This method is use to analyze the file to set the strategy then execute that strategy
    def convert(self, trContext):
        # Here we set the convertor's strategy and get a boolean if the file is able to convert
        canConversion = self.analyzer.analyze(trContext, self.convertor)
        if canConversion:
            # Here we fill audioPath and videoPath that return the convertor in transcriber context
            trContext.audioPath, trContext.videoPath = self.convertor.convert(trContext)
            return True
        else:
            DLog.error("/!\ == FATAL: can't convert file, verify if the file is convertible by the program")
            return False

    # This factory method is use to initialize the default analyzer and convertor to use
    @staticmethod
    def getConversionCoordinator():
        return ConversionCoordinator(ConversionAnalyzer(), Convertor())




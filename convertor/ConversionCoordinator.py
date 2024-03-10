from convertor.Convertor import *
from convertor.ConversionAnalyzer import *
from TranscriberContext import TranscriberContext
from DLog import *

class ConversionCoordinator:
    """
    This class is use to coordinate the conversion. 
    We have to analyze the file to determine which strategy of conversion we need to use. 
    Then convert the file.

    Attributes:
        convertor (Convertor): This class convert file according to its strategy.
    
    """
    def __init__(self, convertor:Convertor):
        self.convertor = convertor

    def convert(self, trContext:TranscriberContext) -> bool:
        """
        This method is use to analyze the file to set the strategy then execute that strategy.

        Args: 
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.

        Returns:
            bool: this boolean determine if the conversion was executed or not        
        """
        # Here we set the convertor's strategy and get a boolean if the file is able to convert
        canConversion = ConversionAnalyzer.analyze(trContext, self.convertor)
        if canConversion:
            # Here we fill audioPath and videoPath that return the convertor in transcriber context
            trContext.audioPath, trContext.videoPath = self.convertor.convert(trContext)
            return True
        else:
            DLog.error("/!\ == FATAL: can't convert file, verify if the file is convertible by the program")
            return False

    @staticmethod
    def getConversionCoordinator():
        """
        This factory method is use to initialize the default convertor to use.        
        """
        return ConversionCoordinator(Convertor())




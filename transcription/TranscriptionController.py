from TranscriberContext import *
from downloader.DownloaderManager import *
from convertor.ConversionCoordinator import *
from transcriber.transcriberManager import *


# The idea behind the code is to use https://refactoring.guru/fr/design-patterns/facade
# So the design pattern of Facade (in french yes) wan't to simplify the interaction
# with a set of class
# This object is also a singleton, a singleton facade ahah


# I named this class a controller cause the controller need to process the user input
class TranscriptionController:

    instance = None

    def __init__(self):
        pass

    # The main function that we need to call, here, the input is only a string
    # cause the only way for the user to talk with this object is by passing an
    # input text that contains the url // the path of the video
    # We may need to thread that in the future
    # The callback of this function take a value in parameter so, in this callback, you will need
    # to put something like trContext.text = result["text"]
    def startTranscription(self, input: str, callback):
        transcriberContext = TranscriberContext(input)

        downloaderManager = DownloaderManager()
        downloaderManager.startDownload(transcriberContext)

        converterCoordinator = ConversionCoordinator.getConversionCoordinator()
        conversionResult = converterCoordinator.convert(transcriberContext)

        contextTranscriber = IATranscriberContext("small", callback)
        trManager = TranscriberManager()
        trManager.useAI(ListAI.WHISPER, contextTranscriber)
        trManager.transcribe(transcriberContext.audioPath)
        pass

    # For some reason, this function worked as a static even without the @staticmethod... so i searched and lol
    # https://stackoverflow.com/questions/52831534/why-is-a-method-of-a-python-class-declared-without-self-and-without-decorators
    # This is funny, what a snake
    @staticmethod
    def getInstance() -> 'TranscriptionController' :
        if TranscriptionController.instance == None :
            TranscriptionController.instance = TranscriptionController()
        return TranscriptionController.instance

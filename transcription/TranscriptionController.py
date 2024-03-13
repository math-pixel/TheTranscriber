from TranscriberContext import *
from downloader.DownloaderManager import *
from convertor.ConversionCoordinator import *
from transcriber.transcriberManager import *


# The idea behind the code is to use https://refactoring.guru/fr/design-patterns/facade
# So the design pattern of Facade (in french yes) wan't to simplify the interaction
# with a set of class


# I named this class a controller cause the controller need to process the user input
class TranscriptionController:

    def __init__(self):
        pass

    # The main function that we need to call, here, the input is only a string
    # cause the only way for the user to talk with this object is by passing an
    # input text that contains the url // the path of the video
    # We may need to thread that in the future
    def startTranscription(self, input: str):
        transcriberContext = TranscriberContext(input)

        downloaderManager = DownloaderManager()
        downloaderManager.startDownload(transcriberContext)

        converterCoordinator = ConversionCoordinator.getConversionCoordinator()
        conversionResult = converterCoordinator.convert(transcriberContext)


        def myEndedFunctionDamour(result):
            print(f"result of transcriber : {result['text']}")
            transcriberContext.transcribeText = result["segments"]


        contextTranscriber = IATranscriberContext("small", myEndedFunctionDamour)
        myManager = TranscriberManager()
        myManager.useAI(ListAI.WHISPER, contextTranscriber)
        myManager.transcribe(transcriberContext.audioPath)
        pass

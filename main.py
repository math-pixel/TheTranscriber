from TranscriberContext import *
from downloader.DownloaderManager import *
from convertor.ConversionCoordinator import *
from transcriber.transcriberManager import *
from GUI.mainUI import *

# transcriberContext = TranscriberContext.getContextWithUrl()


def lauchOtherScripts(url):
    
    transcriberContext = TranscriberContext(url)

    downloaderManager = DownloaderManager()
    downloaderManager.startDownload(transcriberContext)

    converterCoordinator = ConversionCoordinator.getConversionCoordinator()
    conversionResult = converterCoordinator.convert(transcriberContext)

    def myEndedFunctionDamour(result):
        print(f"result of transcriber : {result['text']}")
        tsContext.transcribeText = result["segments"]


    contextTranscriber = IATranscriberContext("small", myEndedFunctionDamour)
    myManager = TranscriberManager()
    myManager.useAI(ListAI.WHISPER, contextTranscriber)
    myManager.transcribe(transcriberContext.audioPath)


startUI(lauchOtherScripts)

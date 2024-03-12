from TranscriberContext import *
from downloader.DownloaderManager import *
from convertor.ConversionCoordinator import *
from transcriber.transcriberManager import *

transcriberContext = TranscriberContext.getContextWithUrl()

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

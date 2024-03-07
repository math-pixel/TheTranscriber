from transcriber.transcriberManager import *
from TranscriberContext import *

tsContext = TranscriberContext.getContextWithVideoAndAudio()

def myEndedFunctionDamour(result):
    print(f"result of transcriber : {result['text']}")
    tsContext.transcribeText = result["segments"]

contextTranscriber = IATranscriberContext("small", myEndedFunctionDamour)
myManager = TranscriberManager()
myManager.useAI(ListAI.WHISPER, contextTranscriber)
myManager.transcribe(tsContext.audioPath)

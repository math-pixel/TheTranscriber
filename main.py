from transcriber.transcriberManager import *
from TranscriberContext import *

tsContext = TranscriberContext.getContextWithVideoAndAudio()

def myEndedFunctionDamour(result):
    print(f"result of transcriber : {result}")
    tsContext.transcribeText = result

contextTranscriber = IATranscriberContext(tsContext.audioPath, myEndedFunctionDamour)
myManager = TranscriberManager()
myManager.useAI(ListAI.WHISPER, contextTranscriber)
myManager.transcribe("./export/audio.mp3")

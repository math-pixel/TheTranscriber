from transcriber.transcriberManager import *


def myEndedFunctionDamour(result):
    print(f"result of transcriber : {result}")

contextTranscriber = TranscriberContext("small", myEndedFunctionDamour)
myManager = TranscriberManager()
myManager.useAI(ListAI.WHISPER, contextTranscriber)
myManager.transcribe("./export/audio.mp3")

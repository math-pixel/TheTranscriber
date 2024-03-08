from transcriber.transcriberManager import *
from TranscriberContext import *
from DLog import *

DLog.goodbiglog("==========TEST : TRANSCRIBER STARTED==========")
try:
    tsContext = TranscriberContext.getContextWithVideoAndAudio()

    def myEndedFunctionDamour(result):
        print(f"result of transcriber : {result['text']}")
        tsContext.transcribeText = result["segments"]

    contextTranscriber = IATranscriberContext("small", myEndedFunctionDamour)
    myManager = TranscriberManager()
    myManager.useAI(ListAI.WHISPER, contextTranscriber)
    myManager.transcribe(tsContext.audioPath)
    DLog.goodbiglog("==========TEST : TRANSCRIBER PASSED==========")
except:
    DLog.exception("==========TEST : TRANSCRIBER FAILED==========")

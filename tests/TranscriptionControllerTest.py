from transcription.TranscriptionController import *
from DLog import *

def callback(result):
    DLog.goodbiglog("callback called")
    DLog.goodlog(f"result of transcriber : {result['text']}")


DLog.goodbiglog("==========TEST : TRANSCRIPTION CONTROLLER STARTED==========")
try:
    trController = TranscriptionController.getInstance().startTranscription("https://www.youtube.com/watch?v=z9w6tO4d90U", callback);
    DLog.goodbiglog("==========TEST : TRANSCRIPTION CONTROLLER PASSED==========")
except:
    DLog.exception("==========TEST : TRANSCRIPTION CONTROLLER FAILED==========")

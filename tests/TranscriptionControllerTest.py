from transcription.TranscriptionController import *
from DLog import *


DLog.goodbiglog("==========TEST : TRANSCRIPTION CONTROLLER STARTED==========")
try:
    trController = TranscriptionController()
    trController.startTranscription("https://www.youtube.com/watch?v=z9w6tO4d90U");
    DLog.goodbiglog("==========TEST : TRANSCRIPTION CONTROLLER PASSED==========")
except:
    DLog.exception("==========TEST : TRANSCRIPTION CONTROLLER FAILED==========")

from TranscriberContext import *
from transcription.TranscriptionController import *
from GUI.mainUI import *
from DLog import *

def tempCallback(result):
    DLog.errorbiglog("Callback function for transcription isn't set")
    pass

def launchTranscription(url, callback = tempCallback):
    TranscriptionController.getInstance().startTranscription(url, tempCallback)


startUI(launchTranscription)

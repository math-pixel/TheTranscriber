from TranscriberContext import *
from transcription.TranscriptionController import *
from GUI.Application import *
from DLog import *

def tempCallback(result):
    print(result)
    
    window.startSecondPage(result, 'export/video.mp4')
    
    DLog.errorbiglog("Callback function for transcription isn't set")
    

def launchTranscription(url, callback = tempCallback):
    TranscriptionController.getInstance().startTranscription(url, tempCallback)


app = Application.getInstance()


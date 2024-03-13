from transcription.TranscriptionController import *
from DLog import *

def callback(result):
    DLog.goodlog("callback called")
    DLog.goodlog(f"result of transcriber : {result['text']}")

trController = TranscriptionController.getInstance().startTranscription("https://www.youtube.com/watch?v=z9w6tO4d90U", callback);

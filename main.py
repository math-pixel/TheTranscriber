from transcriber.whisperTranscriber import *

def finished(string):
    print(string)

myWhisper = Whisper("./export/audio.mp3",finished, "small")

# myWhisper.start()
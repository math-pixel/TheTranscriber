from transcriber.WhisperTranscriber import *
from transcriber.IATranscriberContext import *
from enum import Enum


# ---------------------------------------------------------------------------- #
#                                  Enumerator                                  #
# ---------------------------------------------------------------------------- #
class ListAI(Enum):
    WHISPER = 1
    # FASTERWHISPER = 2


class ListState(Enum):
    IDLE = "IDLE"
    LOADINGMODEL =  "LOADINGMODEL"
    TRANSCRIBING = "TRANSCRIBING" 

# ---------------------------------------------------------------------------- #
#                                    Manager                                   #
# ---------------------------------------------------------------------------- #

class TranscriberManager:

    def __init__(self) -> None:
        self.currentAI = None
        self.state = ListState.IDLE

    def setCurrentAI(self, aiName, aiContext):

        if aiName == ListAI.WHISPER:
            self.state = ListState.LOADINGMODEL
            self.currentAI = WhisperTranscriber(customContext=aiContext)
            self.currentAI.loadModel()
            self.state = ListState.IDLE

        else:
            DLog.error("Error : AI not in list")


    def transcribe(self, filename, callback):

        if self.currentAI != None:
            self.state = ListState.TRANSCRIBING
            self.currentAI.transcribe(filename, callback)
            self.state = ListState.IDLE



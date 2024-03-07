from transcriber.whisperTranscriber import *
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
#                              Context IATranscriber                             #
# ---------------------------------------------------------------------------- #

def finished(string):
    print(string)

class IATranscriberContext:
    def __init__(self, model, customCallback) -> None:
        self.myModel = model
        self.myCallback = customCallback

    @staticmethod
    def whisper():
        return IATranscriberContext(model="small", customCallback=finished)
    
    # @staticmethod
    # def fasterWhisper():
    #     return IATranscriberContext("172.20.10.2", 8080)


# ---------------------------------------------------------------------------- #
#                                    Manager                                   #
# ---------------------------------------------------------------------------- #

class TranscriberManager:

    def __init__(self) -> None:
        self.currentAI = None
        self.state = ListState.IDLE

    def useAI(self, aiName, aiContext):

        if aiName == ListAI.WHISPER:
            self.state = ListState.LOADINGMODEL
            self.currentAI = Whisper(customContext=aiContext)
            self.currentAI.loadModel()
            self.state = ListState.IDLE

        else:
            DLog.error("Error : AI not in list")


    def transcribe(self, filename):

        if self.currentAI != None:
            self.state = ListState.TRANSCRIBING
            self.currentAI.transcribe(filename)
            self.state = ListState.IDLE



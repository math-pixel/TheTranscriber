from transcriber.WhisperTranscriber import *

class IATranscriberContext:
    def __init__(self, model) -> None:
        self.myModel = model

    @staticmethod
    def whisper():
        return IATranscriberContext(model="small")
    
    # @staticmethod
    # def fasterWhisper():
    #     return IATranscriberContext("172.20.10.2", 8080)


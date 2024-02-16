from interfaceTranscriber import InterfaceTranscriber
import whisper
from DLog import *

class Whisper(InterfaceTranscriber):

    def __init__(self,fileName,callback, model = "small"):
        self.avaibleModelForTranscriber = [ "tiny", "base",  "small", "medium", "large" ]
        self.callback = callback
        self.fileName = fileName
        self.model = None

        self.loadModel(model)

    # load model
    def loadModel(self, model):

        # test if model is valid
        if model in self.avaibleModelForTranscriber: 
            self.model = whisper.load_model(model)
            DLog.goodlog(f"model '{model}' loaded succesfully")
        else:
            DLog.error(f"Error : model '{model}' not in avaible list !!! \n if you are develloper add it in 'avaibleModelForTranscriber' array of your custom AI")


    # transcribe
    def transcribe(self):
        try:
            result = self.model.transcribe(self.fileName)
            self.callback(result["text"])
        except:
            DLog.error(f"Error : When module trannscribe")
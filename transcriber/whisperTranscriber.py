from transcriber.InterfaceTranscriber import InterfaceTranscriber
from DLog import *
import whisper

class WhisperTranscriber(InterfaceTranscriber):

    def __init__(self, customContext):
        self.avaibleModelForTranscriber = [ "tiny", "base",  "small", "medium", "large" ]
        self.callback = customContext.myCallback
        self.model = customContext.myModel

    # load model
    def loadModel(self):

        # test if model is valid
        if self.model in self.avaibleModelForTranscriber: 
            DLog.goodlog(f"model '{ self.model }' loading")
            self.model = whisper.load_model(self.model)
            DLog.goodlog(f"model loaded succesfully")
        else:
            DLog.error(f"Error : model '{self.model}' not in avaible list !!! \n if you are develloper add it in 'avaibleModelForTranscriber' array of your custom AI")

    def changeModel(self, model):

        if self.model in self.avaibleModelForTranscriber: 
            self.model = model
            self.loadModel() 

    # transcribe
    def transcribe(self, filename):
        try:
            result = self.model.transcribe(filename)
            self.callback(result)
        except:
            DLog.error(f"Error : When module trannscribe")
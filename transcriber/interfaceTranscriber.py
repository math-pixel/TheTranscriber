import whisper
from DLog import *


class InterfaceTranscriber:

    def __init__(self, fileName, callback, model = ""):

        self.avaibleModelForTranscriber = [] # avaible model for current AI
        self.callback = callback # callback after transcribe
        self.fileName = fileName # url of audio

        self.model = None

        self.loadModel(model)

    # load model
    def loadModel(self, model):

        # test if model is valid
        if model in self.avaibleModelForTranscriber: 
            
            #! ##### load model #####

            DLog.goodlog(f"model '{model}' loaded succesfully")
        else:
            DLog.error(f"Error : model '{model}' not in avaible list !!! \n if you are develloper add it in 'avaibleModelForTranscriber' array of your custom AI")


    # transcribe
    def transcribe(self):
        try:
            pass
            #! ##### Transcribe ##### 
            #* ex : result = self.model.transcribe(self.fileName)

            #! ##### Callback ##### 
            #* ex : self.callback(result["text"])
        except:
            DLog.error(f"Error : When module trannscribe")


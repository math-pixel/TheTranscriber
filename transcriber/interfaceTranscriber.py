from DLog import *


class InterfaceTranscriber:

    def __init__(self, fileName, customContext):

        self.avaibleModelForTranscriber = [] # avaible model for current AI
        self.callback = customContext.myCallback # callback after transcribe
        self.model = customContext.myModel


    # load model
    def loadModel(self):

        # test if model is valid
        if self.model in self.avaibleModelForTranscriber: 
            DLog.goodlog(f"model '{ self.model }' loading")
            
            #! ##### load model #####
            
            DLog.goodlog(f"model loaded succesfully")

        else:
            DLog.error(f"Error : model '{self.model}' not in avaible list !!! \n if you are develloper add it in 'avaibleModelForTranscriber' array of your custom AI")


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


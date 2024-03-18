from TranscriberContext import *
from downloader.DownloaderManager import *
from convertor.ConversionCoordinator import *
from transcriber.TranscriberManager import *
from enum import Enum
from transcription.TranscriptionObserver import *

class TranscriptionState(Enum):
    IDLE = "IDLE"
    DOWNLOADINGVIDEO = "DOWNLOADINGVIDEO"
    CONVERTINGVIDEO = "CONVERTINGVIDEO"
    LOADINGMODEL =  "LOADINGMODEL"
    TRANSCRIBING = "TRANSCRIBING" 


# The idea behind the code is to use https://refactoring.guru/fr/design-patterns/facade
# So the design pattern of Facade (in french yes) wan't to simplify the interaction
# with a set of class
# This object is also a singleton, a singleton facade ahah


# I named this class a controller cause the controller need to process the user input
# This controller is also an Observable object lol : a singleton facade observable lol
class TranscriptionController:

    instance = None

    # In the constructor, i set the current AI of the TranscriberManager, so like that, we
    # directly load the model of the Transcriber Manager once and because it's a singleton,
    # we load it only once !
    def __init__(self):
        contextTranscriber = IATranscriberContext("small")
        self.trManager = TranscriberManager()
        self.trManager.setCurrentAI(ListAI.WHISPER, contextTranscriber)
        self.state = TranscriptionState.LOADINGMODEL
        self.trSubscribers = [] # This is an array of TranscriptionObserver
        pass

    # The main function that we need to call, here, the input is only a string
    # cause the only way for the user to talk with this object is by passing an
    # input text that contains the url // the path of the video
    # We may need to thread that in the future
    def startTranscription(self, input: str):
        transcriberContext = TranscriberContext(input)

        self.updateState(TranscriptionState.DOWNLOADINGVIDEO)
        downloaderManager = DownloaderManager()
        downloaderManager.startDownload(transcriberContext)

        self.updateState(TranscriptionState.CONVERTINGVIDEO)
        converterCoordinator = ConversionCoordinator.getConversionCoordinator()
        conversionResult = converterCoordinator.convert(transcriberContext)

        self.updateState(TranscriptionState.TRANSCRIBING)
        result = self.trManager.transcribe(transcriberContext.audioPath)
        self.updateState(TranscriptionState.IDLE)
        return result

    # Update the state of the controller
    def updateState(self, state):
        DLog.goodlog("updated state into " + str(state))
        # In this function, we will set the state and
        # TODO : NOTIFY SUBSCRIBERS THAT THE STATE CHANGED CAUSE THIS OBJECT IS AN OBSERVABLE
        for sub in self.trSubscribers :
            if isinstance(sub, TranscriptionObserver) == False:
                DLog.bigerrorlog("You didn't put a Transcription Observer in the trSubscribers Array !!")
            sub.update(state)
        self.state = state

    def addSubscriber(self, subscriber):
        self.trSubscribers.append(subscriber)

    def removeSubscriber(self, subscriber):
        # After you added a subscriber, if you don't use it in the future, DELETE IT PLZ !!!!
        self.trSubscribers.remove(subscriber)

    # For some reason, this function worked as a static even without the @staticmethod... so i searched and lol
    # https://stackoverflow.com/questions/52831534/why-is-a-method-of-a-python-class-declared-without-self-and-without-decorators
    # This is funny, what a snake (python lol)
    @staticmethod
    def getInstance() -> 'TranscriptionController' :
        if TranscriptionController.instance == None :
            TranscriptionController.instance = TranscriptionController()
        return TranscriptionController.instance

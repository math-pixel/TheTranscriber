
# This is the observer class of the Transcription Observer, to do this, i checked that : 
# https://refactoring.guru/fr/design-patterns/observer
class TranscriptionObserver:
    def __init__(self):
        pass

    def update(self, state):
        DLog.goodlog(state)
        pass
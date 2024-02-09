class TranscriberContext:

    def __init__(self, url, videoPath=None, audioPath=None, downloadPath=None, transcribeText=None):
        self.url = None
        self.videoPath = None
        self.audioPath = None
        self.downloadPath = None
        self.transcribeText = None

    @staticmethod
    def getContextWithUrl():
        return TranscriberContext()

    @staticmethod
    def getContextWithVideo():
        return TranscriberContext()

    @staticmethod
    def getContextWithVideoAndAudio():
        return TranscriberContext()

    @staticmethod
    def getContextWithUrlAndPath():
        return TranscriberContext()

    @staticmethod
    def getContextWithFull():
        return TranscriberContext()

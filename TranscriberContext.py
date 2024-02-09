class TranscriberContext:

    def __init__(self, url, videoPath=None, audioPath=None, downloadPath=None, transcribeText=None):
        self.url = None
        self.videoPath = None
        self.audioPath = None
        self.downloadPath = None
        self.transcribeText = None

    @staticmethod
    def getContextWithUrl():
        return TranscriberContext("https://www.youtube.com/watch?v=z9w6tO4d90U", None, None, None, None)

    @staticmethod
    def getContextWithVideo():
        return TranscriberContext("https://www.youtube.com/watch?v=z9w6tO4d90U", "./export/video.mp4", None, "./export/video.mp4", None)

    @staticmethod
    def getContextWithVideoAndAudio():
        return TranscriberContext("https://www.youtube.com/watch?v=z9w6tO4d90U", "./export/video.mp4", "./export/audio.mp3", "./export/video.mp4", None)

    @staticmethod
    def getContextWithUrlAndPath():
        return TranscriberContext("https://www.youtube.com/watch?v=z9w6tO4d90U", None, None, "./export/video.mp4", None)

    @staticmethod
    def getContextWithFull():
        # Add Text went convert for the first time
        return TranscriberContext("https://www.youtube.com/watch?v=z9w6tO4d90U", "./export/video.mp4", "./export/audio.mp3", "./export/video.mp4", None)

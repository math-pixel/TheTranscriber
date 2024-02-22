class TranscriberContext:

    def __init__(self, url, inputPath=None, videoPath=None, audioPath=None, transcribeText=None):
        self.url = url
        self.inputPath = inputPath
        self.videoPath = videoPath
        self.audioPath = audioPath
        self.transcribeText = transcribeText

    @staticmethod
    def getContextWithUrl():
        return TranscriberContext("https://www.youtube.com/watch?v=z9w6tO4d90U", None,  None, None, None,)

    @staticmethod
    def getContextWithVideo():
        return TranscriberContext("https://www.youtube.com/watch?v=z9w6tO4d90U", "./export/video.mp4", None, None, None)

    @staticmethod
    def getContextWithVideoAndAudio():
        return TranscriberContext("https://www.youtube.com/watch?v=z9w6tO4d90U", "./export/video.mp4", "./export/video.mp4", "./export/audio.mp3", None)

    @staticmethod
    def getContextWithFull():
        # Add Text went convert for the first time
        return TranscriberContext("https://www.youtube.com/watch?v=z9w6tO4d90U", "./export/video.mp4", "./export/video.mp3", "./export/audio.mp4", None)

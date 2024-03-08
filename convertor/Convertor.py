from convertor.SoundConvertStrategy import *
from convertor.VideoConvertStrategy import *

# This class convert file according to its strategy
# There is two types of conversion : video conversion and audio conversion
# https://refactoring.guru/design-patterns/strategy
class Convertor:
    def __init__(self):
        self.soundConvertStrategy = DefaultSoundConvertStrategy()
        self.videoConvertStrategy = DefaultVideoConvertStrategy()
        pass

    def setVideoConvertStrategy(self, videoConvertStrategy):
        self.videoConvertStrategy = videoConvertStrategy

    def setSoundConvertStrategy(self, soundConvertStrategy):
        self.soundConvertStrategy = soundConvertStrategy

    # This method convert file from inputPath of transcriber context 
    # and returns the new path of audio and video with the correct format
    def convert(self, trContext):
        audioPath = self.soundConvertStrategy.executeConversion(trContext)
        videoPath = self.videoConvertStrategy.executeConversion(trContext)
        return audioPath, videoPath
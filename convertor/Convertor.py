from convertor.SoundConvertStrategy import *
from convertor.VideoConvertStrategy import *

# Ici on s'inspire du design pattern Strategy :
# https://refactoring.guru/fr/design-patterns/strategy
class Convertor:
    def __init__(self):
        self.soundConvertStrategy = DefaultSoundConvertStrategy()
        self.videoConvertStrategy = DefaultVideoConvertStrategy()
        pass

    def setVideoConvertStrategy(self, videoConvertStrategy):
        self.videoConvertStrategy = videoConvertStrategy

    def setSoundConvertStrategy(self, soundConvertStrategy):
        self.soundConvertStrategy = soundConvertStrategy

    def convert(self, trContext):
        audioPath = self.soundConvertStrategy.executeConversion(trContext)
        videoPath = self.videoConvertStrategy.executeConversion(trContext)
        return audioPath, videoPath
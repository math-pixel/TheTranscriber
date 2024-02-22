
# Ici on s'inspire du design pattern Strategy :
# https://refactoring.guru/fr/design-patterns/strategy
class Convertor:
    def __init__(self):
        self.soundConvertStrategy = None
        self.videoConvertStrategy = None
        pass

    def setConvertStrategy(self, soundConvertStrategy, videoConvertStrategy):
        self.soundConvertStrategy = soundConvertStrategy
        self.videoConvertStrategy = videoConvertStrategy
        pass

    def convert(self, trContext):
        audioPath = self.soundConvertStrategy.executeConversion(trContext)
        videoPath = self.videoConvertStrategy.executeConversion(trContext)
        return audioPath, videoPath
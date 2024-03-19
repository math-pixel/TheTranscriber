from convertor.convertorStrategy.SoundConvertStrategy import *
from convertor.convertorStrategy.VideoConvertStrategy import *
from TranscriberContext import TranscriberContext

# This class convert file according to its strategy
# There is two types of conversion : video conversion and audio conversion
# https://refactoring.guru/design-patterns/strategy
class Convertor:
    """
    This class convert file according to its strategy. There is two types of conversion : video conversion and audio conversion.

    Attributes: 
        soundConvertStrategy (SoundConvertStrategy): 
        videoConvertStrategy (VideoConvertStrategy): 
    """
    def __init__(self) -> None:
        self.soundConvertStrategy = DefaultSoundConvertStrategy()
        self.videoConvertStrategy = DefaultVideoConvertStrategy()

    def setSoundConvertStrategy(self, soundConvertStrategy:SoundConvertStrategy) -> None:
        """
        This method is use to set the sound convert strategy to use for the convertor.

        Args:
            soundConvertStrategy (SoundConvertStrategy):
        """
        self.soundConvertStrategy = soundConvertStrategy

    def setVideoConvertStrategy(self, videoConvertStrategy:VideoConvertStrategy) -> None:
        """
        This method is use to set the video convert strategy to use for the convertor.

        Args:
            videoConvertStrategy (VideoConvertStrategy):
        """
        self.videoConvertStrategy = videoConvertStrategy

    def convert(self, trContext:TranscriberContext):
        """
        This method convert file from inputPath of transcriber context and returns the new path of audio and video with the correct format

        Args:
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.

        Returns:
            audioPath (str): This is the audio path of the new audio file that has been converted.
            videoPath (str): This is the video path of the new video file that has been converted.
        """
        if trContext.audioPath is not None:
            DLog.warning(f"The audio path is already filled. It will probably be overwritten. Here is the old audio path: {trContext.audioPath}")
        if trContext.videoPath is not None:
            DLog.warning(f"The video path is already filled. It will probably be overwritten. Here is the old video path: {trContext.videoPath}")

        audioPath = self.soundConvertStrategy.executeConversion(trContext)
        videoPath = self.videoConvertStrategy.executeConversion(trContext)
        return audioPath, videoPath
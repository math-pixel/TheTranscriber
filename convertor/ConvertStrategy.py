from DLog import *
from moviepy.editor import *

class ConvertStrategy:
    def __init__(self):
        DLog.warning("Initialize strategy")
        pass

    def executeConversion(self, trContext):
        DLog.warning("Execute conversion")
        pass

class MP4ToMP3ConvertStrategy(ConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)
        # Execute some conversion from MP4 to MP3
        # and return the result path

        video_clip = VideoFileClip(trContext.videoPath)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(trContext.audioPath)
        audio_clip.close()
        video_clip.close()
        
        return True

class AviToMP3ConvertStrategy(ConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)
        # Execute some conversion from Avi to MP3
        # and return the result trContext

        video_clip = VideoFileClip(trContext.videoPath)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(trContext.audioPath)
        audio_clip.close()
        video_clip.close()

        return True
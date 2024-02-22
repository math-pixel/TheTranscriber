from DLog import *
from moviepy.editor import *
from pydub import AudioSegment

class SoundConvertStrategy:
    def __init__(self):
        DLog.warning("Initialize strategy")
        pass

    def executeConversion(self, trContext):
        DLog.warning("Execute conversion")
        pass

class MP4ToMP3ConvertStrategy(SoundConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)

        video_clip = VideoFileClip(trContext.inputPath)
        audio_clip = video_clip.audio
        # Set the ouput path like this, temporary
        audio_clip.write_audiofile("export/output.mp3")
        audio_clip.close()
        video_clip.close()
        
        return "export/output.mp3"

class AviToMP3ConvertStrategy(SoundConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)

        video_clip = VideoFileClip(trContext.inputPath)
        audio_clip = video_clip.audio
        # Set the ouput path like this, temporary
        audio_clip.write_audiofile("export/output.mp3")
        audio_clip.close()
        video_clip.close()

        return "export/output.mp3"

class WavToMP3ConvertStrategy(SoundConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)

        sound = AudioSegment.from_wav(trContext.inputPath)
        sound.export("export/output.mp3", format="mp3")

        return "export/output.mp3"
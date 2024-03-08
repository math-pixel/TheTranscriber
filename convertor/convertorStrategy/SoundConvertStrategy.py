from DLog import *
from TranscriberContext import TranscriberContext
from moviepy.editor import *
from pydub import AudioSegment

class SoundConvertStrategy:
    """
    This class implements strategies for audio file conversion.
    """
    def __init__(self):
        DLog.warning("Initialize strategy")
        pass

    def executeConversion(self, trContext:TranscriberContext):
        """
        This method launch the file conversion according to the strategy selected.
        
        Args:
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.
        """
        DLog.warning("Execute conversion")
        pass

class DefaultSoundConvertStrategy(SoundConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext:TranscriberContext):
        """
        This method do not launch conversion and return None.
        
        Args:
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.
        """
        super().executeConversion(trContext)
        return None

class MP4ToMP3ConvertStrategy(SoundConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext:TranscriberContext):
        """
        This method launch the file conversion from MP4 to MP3.
        
        Args:
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.
        
        Returns:
            audioPath (str): That is the audio path of the file resulting from the conversion.
        """
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

    def executeConversion(self, trContext:TranscriberContext):
        """
        This method launch the file conversion from Avi to MP3.
        
        Args:
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.
        
        Returns:
            audioPath (str): That is the audio path of the file resulting from the conversion.
        """
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

    def executeConversion(self, trContext:TranscriberContext):
        """
        This method launch the file conversion from Wav to MP3.
        
        Args:
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.
        
        Returns:
            audioPath (str): That is the audio path of the file resulting from the conversion.
        """
        super().executeConversion(trContext)

        sound = AudioSegment.from_wav(trContext.inputPath)
        sound.export("export/output.mp3", format="mp3")

        return "export/output.mp3"

class MP3ToMP3ConvertStrategy(SoundConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext:TranscriberContext):
        """
        This method launch the file conversion from MP3 to MP3. We are using this strategy to get the new audio path.
        We are not using DefaultSoundConvertStrategy because its method return None.
        
        Args:
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.
        
        Returns:
            audioPath (str): That is the audio path of the file resulting from the conversion.
        """
        super().executeConversion(trContext)
        return trContext.inputPath
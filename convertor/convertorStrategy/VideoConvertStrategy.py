from DLog import *
from TranscriberContext import TranscriberContext
from moviepy.editor import *

class VideoConvertStrategy:
    """
    This class implements strategies for video file conversion.
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

class DefaultVideoConvertStrategy(VideoConvertStrategy):
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
    
class MP4ToMP4ConvertStrategy(VideoConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext:TranscriberContext):
        """
        This method launch the file conversion from MP4 to MP4. We are using this strategy to get the new video path.
        We are not using DefaultVideoConvertStrategy because its method return None.
        
        Args:
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.
        
        Returns:
            videoPath (str): That is the video path of the file resulting from the conversion.
        """
        super().executeConversion(trContext)
        
        return trContext.inputPath

class AviToMP4ConvertStrategy(VideoConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext:TranscriberContext):
        """
        This method launch the file conversion from Wav to MP4.
        
        Args:
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.
        
        Returns:
            videoPath (str): That is the video path of the file resulting from the conversion.
        """
        super().executeConversion(trContext)
        video_clip = VideoFileClip(trContext.inputPath)
        video_clip.write_videofile("export/output.mp4", codec='libx264')
        video_clip.close()

        return "export/output.mp4"
from DLog import *
from moviepy.editor import *

class VideoConvertStrategy:
    def __init__(self):
        DLog.warning("Initialize strategy")
        pass

    def executeConversion(self, trContext):
        DLog.warning("Execute conversion")
        pass

class NoneConvertStrategy(VideoConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)
        return None
    
class MP4ToMP4ConvertStrategy(VideoConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)
        
        return trContext.inputPath

class AviToMP4ConvertStrategy(VideoConvertStrategy):
    def __init__(self):
        super().__init__()
        pass

    def executeConversion(self, trContext):
        super().executeConversion(trContext)
        video_clip = VideoFileClip(trContext.inputPath)
        video_clip.write_videofile("export/output.mp4", codec='libx264')
        video_clip.close()

        return "export/output.mp4"
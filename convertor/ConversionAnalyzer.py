from DLog import *
from convertor.SoundConvertStrategy import *
from convertor.VideoConvertStrategy import *
import magic

# This class analyze the file type to determine which strategy the convertor will use
class ConversionAnalyzer:
    def __init__(self):
        pass

    def analyze(self, trContext, convertor):
        DLog.goodlog("Start analyze the file")
        # If we don't have audio path we must check how to convert
        if trContext.audioPath != None :
            return False 

        # Verify the mime type of the file
        file_type = self.get_file_type(trContext.inputPath) 
        DLog.goodlog(f"File type of the input : {file_type}")
        if file_type == None :
            DLog.error("File doesn't have a mime type ? Check that the file you want to analyze exists")

        if file_type == "video/mp4":
            convertor.setSoundConvertStrategy(MP4ToMP3ConvertStrategy())
            convertor.setVideoConvertStrategy(MP4ToMP4ConvertStrategy())
            return True 
        elif file_type == "video/x-msvideo": # AVI
            convertor.setSoundConvertStrategy(AviToMP3ConvertStrategy())
            convertor.setVideoConvertStrategy(AviToMP4ConvertStrategy())
            return True 
        elif file_type == "audio/mpeg":
            convertor.setSoundConvertStrategy(MP3ToMP3ConvertStrategy())
            return True 
        elif file_type == "audio/x-wav":
            convertor.setSoundConvertStrategy(WavToMP3ConvertStrategy())
            return True 
        else :
            DLog.error("inputPath of trContext isn't convertible.")
        
        return False

    
    def get_file_type(self, videoPath):
        # Try catch lol
        try:
            mime = magic.Magic(mime=True)
            file_type = mime.from_file(videoPath)
            return file_type
        except Exception as e:
            DLog.error(f"An error occurred in the analyze of the file : {e}")
            return None
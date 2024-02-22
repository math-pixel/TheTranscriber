from DLog import *
from convertor.ConvertStrategy import *
import magic


class ConversionAnalyzer:
    def __init__(self):
        pass

    def analyze(self, trContext, convertor):
        DLog.goodlog("Start analyze the file")
        # If we don't have audio path we must check how to convert
        if trContext.audioPath != None :
            return False;

        # Verify the mime type of the file
        file_type = self.get_file_type(trContext.inputPath);
        DLog.goodlog(f"File type of the input : {file_type}")
        if file_type == None :
            DLog.error("File doesn't have a mime type ? Check if the file you wan't to analyze exist")

        if file_type == "video/mp4":
            convertor.setConvertStrategy(MP4ToMP3ConvertStrategy())
            return True;
        elif file_type == "video/x-msvideo":
            convertor.setConvertStrategy(AviToMP3ConvertStrategy())
            return True;
        elif file_type == "audio/mpeg":
            # don't need a conversion, we can directly take the input path in that case
            return False;
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
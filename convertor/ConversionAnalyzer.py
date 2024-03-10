from DLog import *
from convertor.convertorStrategy.SoundConvertStrategy import *
from convertor.convertorStrategy.VideoConvertStrategy import *
from convertor.Convertor import Convertor
from TranscriberContext import TranscriberContext
import magic

# This class analyze the file type to determine which strategy the convertor will use
class ConversionAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def analyze(trContext:TranscriberContext, convertor:Convertor) -> bool:
        """
        This method is used to analyze the file and set the strategy to use for the convertor.
        
        Args: 
            trContext (TranscriberContext): Main object with data use for download, convert and transcribe.
            convertor (Convertor): Object use to convert files based on specified strategies.

        Returns:
            bool: This boolean determine if the file is able to convert.
        """

        # If there is not an input path, we can not convert the file
        if trContext.inputPath is None:
            DLog.error(f"The input path is None. Check that you have provided a valid input path.")
            return False

        DLog.goodlog("Start analyze the file")
        # Verify the mime type of the file
        file_type = ConversionAnalyzer.get_file_type(trContext.inputPath) 
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
            DLog.error("The input path of transcriber context isn't convertible.")
        
        return False

    @staticmethod
    def get_file_type(filePath):
        """
        This method determine the file type using its mime type.
        
        Args: 
            filePath (str): This string is the file path of the file that you want to determine.
        """
        try:
            mime = magic.Magic(mime=True)
            file_type = mime.from_file(filePath)
            return file_type
        except Exception as e:
            DLog.error(f"An error occurred in the analyze of the file : {e}")
            return None
import subprocess
import shutil
import os 
from pytube import YouTube

from DLog import *


class Downloader:

    def __init__(self):
        self.downloadPath = "./export"
        self.fileName = "video.mp4"

    def startDownload(self, transcriberContext):
        pass

    def getFileLocation(self):
        return self.downloadPath + "/" + self.fileName


class DownloaderYoutube(Downloader):

    def __init__(self):
        super().__init__()

    def startDownload(self, transcriberContext):
        if os.path.exists(self.getFileLocation()) :
            os.remove(self.getFileLocation())

        DLog.goodlog("Starting Youtube Download")
        
        # Create a YouTube object
        yt = YouTube(transcriberContext.url)

        # Select the stream with normal resolution (360p)
        stream = yt.streams.filter(res="360p").first()

        # Download the video to the specified path
        stream.download(output_path=self.downloadPath, filename=self.fileName)

        DLog.goodlog("Ending Youtube Download")
        transcriberContext.inputPath = self.getFileLocation()


class DownloaderLocal(Downloader):

    def __init__(self):
        super().__init__()

    def startDownload(self, transcriberContext):
        DLog.goodlog("Starting Local Download")
        shutil.copy(transcriberContext.url, self.downloadPath)
        DLog.goodlog("Ending Local Download")
        transcriberContext.inputPath = self.downloadPath

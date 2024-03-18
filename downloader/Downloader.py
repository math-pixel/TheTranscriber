import subprocess
import shutil
import os 

from DLog import *


class Downloader:

    def __init__(self):
        self.downloadPath = "./export/video.mp4"

    def startDownload(self, transcriberContext):
        pass


class DownloaderYoutube(Downloader):

    def __init__(self):
        super().__init__()

    def startDownload(self, transcriberContext):
        if os.path.exists(self.downloadPath) :
            os.remove(self.downloadPath)

        command = ["youtube-dl", "-o", self.downloadPath, transcriberContext.url, "-f" , "mp4"]
        DLog.goodlog("Starting Youtube Download")
        subprocess.run(command)
        DLog.goodlog("Ending Youtube Download")
        transcriberContext.inputPath = self.downloadPath


class DownloaderLocal(Downloader):

    def __init__(self):
        super().__init__()

    def startDownload(self, transcriberContext):
        DLog.goodlog("Starting Local Download")
        shutil.copy(transcriberContext.url, self.downloadPath)
        DLog.goodlog("Ending Local Download")
        transcriberContext.inputPath = self.downloadPath

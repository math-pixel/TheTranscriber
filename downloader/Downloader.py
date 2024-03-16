import subprocess
import shutil

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
        # TODO: add an args that automatically overwrite the file
        command = ["youtube-dl", "-o", self.downloadPath, transcriberContext.url]
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

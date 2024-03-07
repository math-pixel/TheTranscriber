import subprocess
import shutil

from DLog import *


class Downloader:

    def __init__(self):
        self.downloadPath = "./export/video.mp4"

    def startDownload():
        pass


class DownloaderYoutube(Downloader):

    def __init__(self):
        super().__init__()

    def startDownload(self, url):
        command = ["youtube-dl", "-o", self.downloadPath, url]
        DLog.goodlog("Starting Youtube Download")
        subprocess.run(command)
        DLog.goodlog("Ending Youtube Download")


class DownloaderLocal(Downloader):

    def __init__(self):
        super().__init__()

    def startDownload(self, localPath):
        DLog.goodlog("Starting Local Download")
        shutil.copy(localPath, self.downloadPath)
        DLog.goodlog("Ending Local Download")

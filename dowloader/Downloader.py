import subprocess
import shutil


class Downloader:

    def __init__(self):
        self.downloadPath = "../export/video.mp4"

    def startDownload():
        pass


class DownloaderYoutube(Downloader):

    def __init__(self):
        super().__init__()

    def startDownload(self, url):
        command = ["youtube-dl", "-o", self.downloadPath, url]
        subprocess.run(command)


class DownloaderLocal(Downloader):

    def __init__(self):
        super().__init__()

    def startDownload(self, localPath):
        shutil.copy(localPath, self.downloadPath)

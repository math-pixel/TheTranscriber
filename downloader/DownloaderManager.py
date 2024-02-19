from downloader.Downloader import *


class DownloaderManager:
    def __init__(self, url):
        self.url = url
        self.downloader = self._initialize_downloader()

    def _initialize_downloader(self):
        if "youtube" in self.url:
            return DownloaderYoutube()
        else:
            return DownloaderLocal()

    def startDownload(self):
        self.downloader.startDownload(self.url)

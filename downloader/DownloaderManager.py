from downloader.Downloader import *


class DownloaderManager:
    def __init__(self):
        pass

    def _initialize_downloader(self, url):
        if "youtube" in url:
            DLog.goodlog("Actual Video State Is Youtube")
            return DownloaderYoutube()
        else:
            DLog.goodlog("Actual Video State Is Local")
            return DownloaderLocal()

    def startDownload(self, transcriberContext):
        downloader = self._initialize_downloader(transcriberContext.url)
        downloader.startDownload(transcriberContext)

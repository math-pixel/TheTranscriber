from downloader.Downloader import *


class DownloaderManager:
    def __init__(self):
        pass

    def _initialize_downloader(self, url):
        if "youtube.com/" in url:
            DLog.goodlog("Actual Video Is Youtube")
            return DownloaderYoutube()
        elif os.path.exists(url) == True:
            DLog.goodlog("Actual Video Is Local")
            return DownloaderLocal()
        DLog.errorbiglog("Actual Video Is not Local or Youtube !!! PROGRAM IS CRYING")
        return False;

    # Return if the downloader did a download or not
    def startDownload(self, transcriberContext):
        downloader = self._initialize_downloader(transcriberContext.url)
        if downloader == False :
            return False
        downloader.startDownload(transcriberContext)
        return True

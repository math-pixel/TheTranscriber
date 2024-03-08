from downloader.DownloaderManager import *
from TranscriberContext import *
from DLog import *

DLog.goodbiglog("==========TEST : DOWNLOADER STARTED==========")
try:
    trContext = TranscriberContext.getContextWithUrl()
    dlManager = DownloaderManager()
    dlManager._initialize_downloader(trContext.url)
    dlManager.startDownload(trContext)
    DLog.goodbiglog("==========TEST : DOWNLOADER PASSED==========")
except:
    DLog.exception("==========TEST : DOWNLOADER FAILED==========")

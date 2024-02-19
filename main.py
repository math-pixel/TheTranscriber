from TranscriberContext import *
from downloader.DownloaderManager import *

transcriberContext = TranscriberContext.getContextWithUrl()

downloaderManager = DownloaderManager(transcriberContext.url)
downloaderManager.startDownload()
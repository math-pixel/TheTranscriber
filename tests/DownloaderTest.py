from downloader.DownloaderManager import *
from TranscriberContext import *
from DLog import *
import unittest

class DownloaderTest(unittest.TestCase):
    def test_downloader(self):
        trContext = TranscriberContext.getContextWithUrl()
        dlManager = DownloaderManager()
        dlManager._initialize_downloader(trContext.url)
        dlManager.startDownload(trContext)
        self.assertIsNotNone(trContext.inputPath)


if __name__ == '__main__':
    unittest.main()

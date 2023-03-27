from unittest import TestCase

from suger.common import FileUtils


class TestFileUtils(TestCase):
    def test_scan_dir(self):
        fileArray = FileUtils.scanDir('C:/Users/14170/Documents/WeChat Files', 'png')
        print(fileArray)

    pass

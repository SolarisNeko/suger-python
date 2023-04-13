from unittest import TestCase

from suger.common import FileCompareUtils


class TestFileCompareUtils(TestCase):
    def test_write_compare_info(self):
        FileCompareUtils.writeFileVersionInfo(input_scan_directory='./',
                                              isNeedMd5=True)

    def test_compare(self):
        FileCompareUtils.writeCompareFileVersionInfo(input_scan_directory='./',
                                                     isNeedMd5=True)

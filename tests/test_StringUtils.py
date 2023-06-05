from unittest import TestCase

from suger.common import StringUtils


class TestStringUtils(TestCase):

    def test_readBooleanTrue(self):
        # Test true values
        self.assertTrue(StringUtils.readBooleanTrue("ok"))
        self.assertTrue(StringUtils.readBooleanTrue("success"))
        self.assertTrue(StringUtils.readBooleanTrue("1"))
        self.assertTrue(StringUtils.readBooleanTrue("yes"))
        # Test false values
        self.assertFalse(StringUtils.readBooleanTrue("no"))
        self.assertFalse(StringUtils.readBooleanTrue("false"))
        self.assertFalse(StringUtils.readBooleanTrue("0"))
        self.assertFalse(StringUtils.readBooleanTrue(""))

    def test_readBooleanFalse(self):
        # Test true values
        self.assertFalse(StringUtils.readBooleanFalse("ok"))
        self.assertFalse(StringUtils.readBooleanFalse("success"))
        self.assertFalse(StringUtils.readBooleanFalse("1"))
        self.assertFalse(StringUtils.readBooleanFalse("yes"))
        # Test false values
        self.assertTrue(StringUtils.readBooleanFalse("no"))
        self.assertTrue(StringUtils.readBooleanFalse("false"))
        self.assertTrue(StringUtils.readBooleanFalse("0"))
        self.assertTrue(StringUtils.readBooleanFalse(""))

    def test_trim(self):
        string = "   Hello, World!   "
        expected_result = "Hello, World!"
        result = StringUtils.trim(string)
        self.assertEqual(result, expected_result)

        # Test with None
        result = StringUtils.trim(None)
        self.assertEqual(result, "")

    def test_is_blank(self):
        str = "   "
        isBlank = StringUtils.isBlank(str)

        self.assertEqual(True, isBlank)

    def test_coverByteToHexString(self):
        byte_array = b'\x01\x02\x03\x04'
        expected_result = "01020304"
        result = StringUtils.coverByteToHexString(byte_array)
        self.assertEqual(result, expected_result)

        # Test with None
        result = StringUtils.coverByteToHexString(None)
        self.assertEqual(result, "")

    def test_coverStringToByteString(self):
        string = "Hello, World!"
        expected_result = "48656c6c6f2c20576f726c6421"
        result = StringUtils.coverStringToByteString(string)
        self.assertEqual(result, expected_result)

        # Test with None
        result = StringUtils.coverStringToByteString(None)
        self.assertEqual(result, "")

    def test_coverHexStringToByte(self):
        hex_string = "01020304"
        expected_result = b'\x01\x02\x03\x04'
        result = StringUtils.coverHexStringToByte(hex_string)
        self.assertEqual(result, expected_result)

        # Test with None
        result = StringUtils.coverHexStringToByte(None)
        self.assertEqual(result, b'')

    def test_coverByteStringToString(self):
        byte_string = "48656c6c6f2c20576f726c6421"
        expected_result = "Hello, World!"
        result = StringUtils.coverByteStringToString(byte_string)
        self.assertEqual(result, expected_result)

# @author SolarisNeko


class StringUtils:

    @staticmethod
    def trim(string: str) -> str:
        """
        安全 trim string
        """
        if string is None:
            return ""
        return string.strip()

    @staticmethod
    def strip(string: str) -> str:
        return StringUtils.trim(string)

    @staticmethod
    def readBooleanTrue(string: str) -> bool:
        """
        将 string 转换为布尔值 True
        """
        true_values = ["ok", "success", "1", "yes"]
        return string.lower() in true_values

    @staticmethod
    def readBooleanFalse(string: str) -> bool:
        """
        将 string 转换为布尔值 False
        """
        return not StringUtils.readBooleanTrue(string)

    @staticmethod
    def isBlank(str: str) -> bool:
        """
        判断字符串是否为空白，包括空字符串、纯空格、制表符、换行符等。
        """
        return str is None or len(str.strip()) == 0

    @staticmethod
    def isNotBlank(str: str) -> bool:
        """
        判断字符串是否不为空白。
        """
        return not StringUtils.isBlank(str)

    @staticmethod
    def defaultIfBlank(str: str, default):
        """
        如果字符串为空白，则返回 default；否则返回字符串本身。
        """
        return default if StringUtils.isBlank(str) else str

    @staticmethod
    def join(separator, *strs: str):
        """
        使用指定的分隔符连接多个字符串。
        """
        return separator.join(strs)

    @staticmethod
    def abbreviate(str: str, maxWidth):
        """
        将字符串缩短到指定的最大宽度（包括省略号），如果字符串本身已经不超过最大宽度，则返回原字符串。
        """
        if len(str) <= maxWidth:
            return str
        else:
            return str[:maxWidth - 3] + "..."

    @staticmethod
    def coverByteToHexString(byteArray: bytes) -> str:
        if byteArray is None:
            return ""
        """
        将比特流变成Hex字符串
        """
        return ''.join(['%02X' % b for b in byteArray])

    @staticmethod
    def coverStringToByteString(string: str):
        if string is None:
            return ""
        """
        将字符串变成ASCII比特流字符串
        """
        return string.encode().hex()

    @staticmethod
    def coverHexStringToByte(hex_string: str) -> bytes:
        """
        将十六进制字符串, 转换为 bytes
        """
        if hex_string is None:
            return bytes([])
        return bytes.fromhex(hex_string)

    @staticmethod
    def coverByteStringToString(byte_string: str) -> str:
        """
        将ASCII编码的十六进制字符串, 转换为字符串
        """
        return bytes.fromhex(byte_string).decode()

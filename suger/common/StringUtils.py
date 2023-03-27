# @author SolarisNeko
class StringUtils:

    @staticmethod
    def isBlank(str):
        """
        判断字符串是否为空白，包括空字符串、纯空格、制表符、换行符等。
        """
        return str is None or len(str.strip()) == 0

    @staticmethod
    def isNotBlank(str):
        """
        判断字符串是否不为空白。
        """
        return not StringUtils.isBlank(str)

    @staticmethod
    def defaultIfBlank(str, default):
        """
        如果字符串为空白，则返回 default；否则返回字符串本身。
        """
        return default if StringUtils.isBlank(str) else str

    @staticmethod
    def join(separator, *strs):
        """
        使用指定的分隔符连接多个字符串。
        """
        return separator.join(strs)

    @staticmethod
    def abbreviate(str, maxWidth):
        """
        将字符串缩短到指定的最大宽度（包括省略号），如果字符串本身已经不超过最大宽度，则返回原字符串。
        """
        if len(str) <= maxWidth:
            return str
        else:
            return str[:maxWidth - 3] + "..."

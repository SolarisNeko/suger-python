import os
import shutil

from suger.common.StringUtils import StringUtils


# @author SolarisNeko
class FileUtils:

    @staticmethod
    def getFullPath(your_path):
        return os.path.abspath(your_path)

    @staticmethod
    def scanDir(dirPath, suffix=""):
        """
        递归扫描指定目录下指定后缀的所有文件名。
        """
        fileNames = []
        for root, dirs, files in os.walk(dirPath):
            for name in files:
                if (StringUtils.isNotBlank(suffix)):
                    if name.endswith(suffix):
                        fileNames.append(os.path.join(root, name))
                        continue
                    else:
                        continue
                fileNames.append(os.path.join(root, name))
        return list(map(FileUtils.getFullPath, fileNames))

    @staticmethod
    def deleteQuietly(fileOrDir):
        """
        尝试删除文件或目录，如果删除失败则不报错。
        """
        try:
            if os.path.exists(fileOrDir):
                if os.path.isfile(fileOrDir):
                    os.remove(fileOrDir)
                elif os.path.isdir(fileOrDir):
                    shutil.rmtree(fileOrDir)
        except Exception as e:
            pass

    @staticmethod
    def forceMkdir(dirPath):
        """
        创建目录，如果目录已经存在则不做任何操作。
        """
        try:
            os.makedirs(dirPath, exist_ok=True)
        except Exception as e:
            pass

    @staticmethod
    def readFileToString(file, encoding="utf-8"):
        """
        读取文件内容并返回字符串。
        """
        with open(file, "r", encoding=encoding) as f:
            return f.read()

    @staticmethod
    def writeStringToFile(file, data, encoding="utf-8", isAppend: bool = False):
        if (isAppend):
            with open(file, "a", encoding=encoding) as f:
                f.write(data)
            return

        """
        将字符串写入文件。
        """
        with open(file, "w", encoding=encoding) as f:
            f.write(data)

    @classmethod
    def isNotFileExists(cls, path):
        return not FileUtils.isFileExists(path)

    @classmethod
    def isFileExists(cls, path):
        if os.path.exists(path):
            return True
        return False

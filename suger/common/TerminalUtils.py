import locale
import subprocess


class TerminalUtils:
    """
    本地命令行工具
    """

    @staticmethod
    def run_command(command: str):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        osEncode = locale.getpreferredencoding()

        code = process.returncode
        output = output.decode(osEncode)
        err = error.decode(osEncode)

        return code, output, err

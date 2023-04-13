from unittest import TestCase

from suger.terminal.TerminalUtils import TerminalUtils


class TestTerminalUtils(TestCase):
    def test_run_command(self):
        code, output, err = TerminalUtils.run_command('tree .')
        print(output)

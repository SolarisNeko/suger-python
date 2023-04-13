from unittest import TestCase

from suger.common.SSH import SSH


class TestSSH(TestCase):
    def test_connect(self):
        print('ok')

        # ssh = SSH(host='localhost', password='root')
        # ssh.connect()
        # output, err = ssh.execute_command('ls .')
        # print(output)

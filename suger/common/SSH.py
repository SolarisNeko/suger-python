import paramiko


class SSH:
    def __init__(self, host, username='root', password='root', key_filename=None, port=22):
        """
        :param host: SSH 主机名或 IP
        :param username: SSH 用户名
        :param password: SSH 密码
        :param key_filename: SSH 密钥文件路径 (一般 '~/.ssh/id_rsa')
        :param port: SSH 端口，默认为 22
        """
        self.host = host
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.port = port
        self.ssh = None

    def connect(self):
        """连接 SSH 主机"""
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if self.password:
            self.ssh.connect(self.host, port=self.port, username=self.username, password=self.password)
        elif self.key_filename:
            key = paramiko.RSAKey.from_private_key_file(self.key_filename)
            self.ssh.connect(self.host, port=self.port, username=self.username, pkey=key)

    def disconnect(self):
        """断开 SSH 连接"""
        self.ssh.close()

    def execute_command(self, command):
        """执行命令"""
        stdin, stdout, stderr = self.ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        return output, error

    def upload_file(self, local_file_path, remote_file_path):
        """上传文件"""
        sftp = self.ssh.open_sftp()
        sftp.put(local_file_path, remote_file_path)
        sftp.close()

    def download_file(self, remote_file_path, local_file_path):
        """下载文件"""
        sftp = self.ssh.open_sftp()
        sftp.get(remote_file_path, local_file_path)
        sftp.close()

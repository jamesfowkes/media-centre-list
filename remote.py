import sys

import paramiko

class Remote:
	def __init__(self, ip, username, password):
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(ip, username=username, password=password)

	def get_directory(self, remote_dir):
		stdin, stdout, stderr = self.ssh.exec_command("ls " + remote_dir) 
		return [l.strip() for l in stdout.readlines()]

if __name__ == "__main__":

	(ip, remote_dir, username, password) = sys.argv[1:5]

	remote = Remote(ip, username, password)
	print(remote.get_directory(remote_dir))

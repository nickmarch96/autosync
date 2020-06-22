#!/usr/bin/env python3
import sys
if sys.version_info<(3,5,0):
  sys.stderr.write("You need python 3.5 or later to run this script\n")
  exit(1)

import paramiko

class SFTPClient:

	def __init__(self, verbose=False):
		if verbose:
			print("Starting SFTPClient...")

		self.username = ""
		self.password = ""
		self.key = None
		self.addr = None
		self.transport = None
		self.sftp = None

		self.verbose = verbose

		
	def set_credentials(self, username, password):
		if self.verbose:
			print("SFTPClient:::Credentials set for {}.".format(username))

		self.username = username
		self.password = password


	def connect(self, addr):
		if self.verbose:
			print("SFTPClient:::Connecting to {}@{}".format(self.username, addr[0], addr[1]))
		
		if type(addr) != tuple and len(addr) != 2:
			raise Exception("Invalid address {}. Expected socket form (host, port)".format(addr))
		
		self.addr = addr

		
		try:
			self.transport = paramiko.Transport(self.addr)

			self.transport.connect(None, self.username, self.password, self.key)

			self.sftp = paramiko.SFTPClient.from_transport(self.transport)

		except Exception as e:
			if self.sftp:
				self.sftp.close()
			if self.transport:
				self.transport.close()
			raise e


	def put(self, localpath, remotepath):
		if self.verbose:
			print("SFTPClient:::Executing sftp -P {} {} {}@{}:{}".format(self.addr[1], localpath, self.username, self.addr[0], remotepath))

		self.sftp.put(localpath, remotepath)


	def get(self, remotepath, localpath):
		if self.verbose:
			print("SFTPClient:::Executing sftp -P {} {}@{}:{} {}".format(self.addr[1], self.username, self.addr[0], remotepath, localpath))

		self.sftp.put(remotepath, localpath)












if __name__ == '__main__':
	host = "127.0.0.1"
	port = 22

	client = SFTPClient(verbose = True)
	client.set_credentials("hxr", input("Password >:".strip()))
	client.connect((host, port))

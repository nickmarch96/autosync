import os
import sys
import socket

def test_connection(host, port, max_tries=3):
	print("Testing connection to server {}:{}...".format(host, port))
	for i in range(max_tries):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		connected = False
		try:
			s.connect((host, port))
			connected = True
			print("Established.")
			return True
		except:
			print("Connection Failed. Trying again...")
			time.sleep(1)
		finally:
			if connected:
				s.shutdown(socket.SHUT_RDWR)
			s.close()
	return False



def validate_server(server):
	if server.count("@") != 1:
		print("Syntax for remote host {} is invalid!".format(server))
		return False
	user, host = server.split("@")

	if ":" in host:
		if host.count(":") != 1:
			print("Syntax for remote host {} is invalid!".format(host))
			return False
		host, port = host.split(":")

		if not port.isdigit():
			print("Port '{}' is invalid!".format(port))
			return False
		port = int(port)

		if port <= 0 or port > 65535:
			print("Port '{}' is out of range!".format(port))
			return False
	else:
		port = 22

	if not test_connection(host, port):
		print("Failed to establish connection to {}:{}.".format(host, port))
		return False

	if len(user) == 0:
		print("Username '{}' for {} is invalid!".format(user, server))
		return False

	return True



def validate_path(path, must_exist=False):
	if must_exist:
		if not os.path.exists(path):
			print("Path {} does not exist!".format(path))
			return False

	return True

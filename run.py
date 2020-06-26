#!/usr/bin/env python3
import sys
import autosync
import socket
import time


def help(var_name):
	print(autosync.extras.__dict__[var_name.upper()])
	sys.exit()



def main():
	args = [s for s in sys.argv]
	if len(args) == 1:
		help("help_root")

	fun = args[1].lower().strip()

	if fun == "about":
		help("about")

	elif fun == "status":
		print("This is a status")

	elif fun == "add":
		if len(args) == 2:
			help("help_add")

		f_type = args[2].lower().strip()

		if f_type in autosync.extras.ADD_LFILE_ALIAS:
			if len(args) != 6 or args[3] == "help":
				help("help_add_lfile")
			lpath, rpath, server = args[3:]

			print("Validating paths...")
			if not autosync.functions.validate_path(lpath, must_exist=True):
				print("Local path failed to validate...")
				return

			if not autosync.functions.validate_path(rpath):
				print("Remote path failed to validate...")
				return
			print("Validated.")

			print("Validating Server...")
			if not autosync.functions.validate_server(server):
				print("Server failed to validate...")
				return
		else:
			help("help_add")

		

	elif fun == "remove":
		pass

	else:
		help("help_root")



if __name__ == '__main__':
	main()
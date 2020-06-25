#!/usr/bin/env python3

import PySimpleGUI as sg
#import autosync
import autosync_extras
import os
from time import sleep

sg.theme("Light Grey 1")


error_len = 30

def add_layout():
	title_text = sg.Text("AutoSYNC GUI Wrapper for AutoSYNC {}".format(autosync_extras.__dict__["VER_NUM"]))

	lpath_text = sg.Text("Local Path")
	local_path = sg.InputText(key="local_path", enable_events=True, tooltip="The path to the local file to be synced.")
	browse = sg.FileBrowse(target="local_path")
	lpath_error = sg.Text(size=(error_len, 1), text_color="red", key="lpath_error", visible=False)

	rpath_text = sg.Text("Remote Path")
	remote_path = sg.InputText(key="remote_path", tooltip="The path to the remote file or folder to be synced.")
	rpath_error = sg.Text(size=(error_len, 1), text_color="red", key="rpath_error", visible=False)
	
	remote_check = sg.Checkbox("Pull from remote", key="remote_check", enable_events=True, tooltip="Check to pull remote file to local path before syncing. Uncheck to sync future local file changes to remote path.")
	
	user_text = sg.Text("User name")
	user_name = sg.InputText(key="user_name", tooltip="The user to use when syncing.")
	uname_error = sg.Text(size=(error_len, 1), text_color="red", key="uname_error", visible=False)
	
	password_text = sg.Text("Password")
	password = sg.InputText(key="password", password_char="*", tooltip="Password to authenticate with.")
	password_check = sg.Checkbox("Save credentials", key="password_check", enable_events=True, tooltip="Enable saving credentials to prevent requireing the password upon every sync attempt.")
	password_error = sg.Text(size=(error_len, 1), text_color="red", key="password_error", visible=False)

	con_password_text = sg.Text("Confirm Password")
	confirm_password = sg.InputText(key="confirm_password", password_char="*", tooltip="Safety mechanism")
	
	con_password_error = sg.Text(size=(error_len, 1), text_color="red", key="con_password_error", visible=False)
	
	server_text = sg.Text("Server")
	server_name = sg.InputText(key="server_name", tooltip="The address of the server.")
	sname_error = sg.Text(size=(error_len, 1), text_color="red", key="sname_error", visible=False)
	
	port_text = sg.Text("Port")
	port_override = sg.InputText(key="port_override", disabled=True, tooltip="The port used to access sftp on the server.")
	port_override_check = sg.Checkbox("Non-standard port", key="port_override_check", enable_events=True, tooltip="Check to enable specifying a non-standard ssh port to use.")
	port_error = sg.Text(size=(error_len,1), text_color="red", key="port_error", visible=False)

	sync = sg.Button("Sync", key="sync")

	status = sg.Text("Status: Waiting for user input...", key="status")

	return [
		[title_text],
		[lpath_text],
		[local_path, browse],
		[lpath_error],
		[rpath_text],
		[remote_path, remote_check],
		[rpath_error],
		[user_text],
		[user_name],
		[uname_error],
		[password_text],
		[password, password_check],
		[password_error],
		[con_password_text],
		[confirm_password],
		[con_password_error],
		[server_text],
		[server_name],
		[sname_error],
		[port_text],
		[port_override, port_override_check],
		[port_error],
		[sync],
		[status]
		]

def set_error(elem, err):
	elem.Update(value=err)
	elem.Update(visible=True)

def clear_error(elem):
	elem.Update(value="")
	elem.Update(visible=False)


def check_errors(w):
	local_file = w["local_path"].Get()
	remote_file = w["remote_path"].Get()
	remote_check = w["remote_check"].Get()
	user_name = w["user_name"].Get()
	password = w["password"].Get()
	confirm_password = w["confirm_password"].Get()
	port_override_check = w["port_override_check"].Get()
	port_override = w["port_override"].Get()
	server_name = w["server_name"].Get()
	
	if local_file == "":
		set_error(w["lpath_error"], "No local path set!")
		return True
	elif not os.path.exists(local_file):
		set_error(w["lpath_error"], "Local path does not exist!")
		return True
	else:
		clear_error(w["lpath_error"])
		
	if remote_file == "":
			set_error(w["rpath_error"], "No remote path set!")
			return True
	else:
		clear_error(w["rpath_error"])
			
	if user_name == "":
		set_error(w["uname_error"], "No user supplied!")
		return True
	else:
		clear_error(w["uname_error"])
		
	if password == "":
		set_error(w["password_error"], "No password supplied!")
		return True
	else:
		clear_error(w["password_error"])

	if password != confirm_password:
		set_error(w["con_password_error"], "Passwords do not match!")
		return True
	else:
		clear_error(w["con_password_error"])

	if not server_name.strip('.').isnumeric():
		set_error(w["sname_error"], "Server name not valid!")
		return True
	else:
		clear_error(w["sname_error"])

	if port_override_check:
		if not port_override.isnumeric():
			set_error(w["port_error"], "Specified port is not a number!")
			return True
		elif int(port_override) < 0 or int(port_override) > 65535:
			set_error(w["port_error"], "Specified port is not a valid port!")
			return True
		else:
			clear_error(w["port_error"])
	else:
		clear_error(w["port_error"])

	return False



w = sg.Window(title="AutoSYNC", layout=add_layout())

while True:
	event, val = w.Read()

	if event == "port_override_check":
		if val["port_override_check"]:
			w["port_override"].Update(disabled=False)
		else:
			w["port_override"].Update(disabled=True)
			w["port_override"].Update(value="Port")
		w.Refresh()

	elif event == "local_path":
		filename = os.path.basename(os.path.normpath(val["local_path"]))
		w["remote_path"].Update(value="~/".join(filename))

	elif event == "sync":
		local_file = w["local_path"].Get()
		pwd = w["password"].Get()
		remote_file = w["remote_path"].Get()
		user = w["user_name"].Get()
		server = w["server_name"].Get()
		port_override_check = w["port_override_check"].Get()
		if port_override_check:
			port = w["port_override"].Get()
		else:
			port = "22"
		password_check = w["password_check"].Get()

		w["status"].Update(value="Status: Validating inputs...")
		if check_errors(w):
			w["status"].Update(value="Status: Waiting for user input...")
			w.Refresh()
			continue

		if password_check:
			w["status"].Update(value="Status: Saving credentials...")
			sleep(1)
			
		w["status"].Update(value="Status: Done.")

	elif event == sg.WIN_CLOSED:
		break

	else:
		print(event, val)
		
w.close()
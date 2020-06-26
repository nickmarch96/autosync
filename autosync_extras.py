
VER_NUM = 1.0

ABOUT = """AutoSYNC is a tool to ease file management. AutoSYNC is currently in version {}.
AutoSYNC is partially inspired by git and MobaXTerm. AutoSYNC syncs files across
networks and can automatically or manually send changes of a file to the remote
host. AutoSYNC can not automatically detect changes of a remote file but will
detect a change if it attempts to send data. This tool is meant for server 
management tasks such as wanting to change configuration files with a gui on a
guiless server. This tool can also be used as a rudementary backup system,
however I would not reccomend this tool as a backup solution. There are many
tools that do this and plugins for applications such as sublime. I have
encountered issues with them working properly or just being clunky in design. I
want to take the ease of use from git and apply it to easing the burden of
remote server management.""".format(VER_NUM)

HELP_ROOT = """AutoSYNC Version {}
autosync status
	Check status of AutoSYNC and the files it is watching.
autosync add
	Add a new entity for AutoSYNC to manage.
autosync remove
	Removes an entity from AutoSYNC. Does not delete the file!
autosync help
	Display this information. help can be added to any of the above commands
	for more information on how to use that particular function.
autosync about
	Displays information about autosync.""".format(VER_NUM)

HELP_ADD = """autosync add [type] [credentials server localpath remotepath]
type can be one of three types: localfile, remotefile, credentials.

autosync add localfile localpath remotepath server
	Adds a localfile to AutoSYNC. Any changes made to this file will be sent to
	the remote server.
	Aliases for localfile: [localfile, lfile, file]
	Example:
		autosync add lfile ./file.txt ~/file.txt user@127.0.0.1

autosync add remotefile localpath remotepath server
	Download a remote file from the server to local path. Any changes made to
	the local copy will be sent to the remote server.
	Aliases for remotefile: [remotefile, rfile]
	Example:
		autosync add rfile ./file.txt ~/file.txt user@127.0.0.1

autosync add credentials [password] server
	Adds a set of credentials to use for authentication. This is optional
	but not doing this will result in AutoSYNC asking for credentials
	upon every sync. Supplying a password in the commandline is also
	optional. If not then it will be prompted for.
	Aliases for credentials: [credentials, creds, cred]
	Example:
		autosync add creds password123 user@127.0.0.1
		autosync add credentials user@127.0.0.1

If the server is on a non standard port then the port can always be
specified by appending a colon and then the port number.
	Example:
		autosync add rfile ./file.txt ~/file.txt user@127.0.0.1:2222
"""


ADD_LFILE_ALIAS = ["localfile", "lfile", "file"]
ADD_RFILE_ALIAS = ["remotefile", "rfile"]
ADD_CRED_ALIAS = ["credentials", "creds", "cred"]
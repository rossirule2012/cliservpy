import socket
import sys
import os

#---Command Line Arguments-------#
filename=sys.argv[1]
host=sys.argv[2]
port=sys.argv[3]
buffer=int(sys.argv[3])
#-------------------------------#

#--------System vars------------#
#port=9011
#host=
#buffer=
#-------------------------------#

dim=os.path.getsize(filename)
outgoing=open(filename,'rb')
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,int(port)))
strf=filename+'/'  #Preparing filename string to send#

for a in strf:     #sending filename one charater at time#
	print(a)
	sock.sendall(bytes(a,'UTF-8'))

print('Sending file: '+filename)
i=0
while 1:
 data=outgoing.read(buffer)
 print('Uploaded % (Bytes): ',i*buffer,' of ',dim)
 if not data: break
 sock.sendall(data)
 i+=1
	
outgoing.close()
sock.close()

import socket
import sys
import os

filename=''
HST=''
PRT=9011
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Server created')
server.bind((HST,PRT))
print('Server bind complete')
server.listen(10)
print('Server listening for clients')
print('PORT=',PRT,'    IP=',socket.gethostbyname(socket.gethostname()))
print('HOST=',socket.gethostname())

while 1:
	s, addr=server.accept()
	while 1:
		ck=s.recv(1)
		if ck.decode('UTF-8')=='/': break
		filename+=ck.decode('UTF-8')
	print('Receiving file: '+filename)
	fil=open(filename,'wb')
	while 1:
			data=s.recv(1024)
			if not data: break
			fil.write(data)
	print('File downloaded: '+filename+' ',os.path.getsize(filename)/1024,' kb')
	fil.close()
	filename=''

s.close()
server.close()
sys.exit
	

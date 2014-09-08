from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import threading
import string
import socket
import sys
import os

def upload():
        filename=filedialog.askopenfilename()
        port=int(port_val.get())
        host=str(host_val.get())
        print(port)
        print(host)
        print(filename)
        print(os.path.getsize(filename))
        splitted=filename.split('/')
        name=splitted[-1]
        connthread=Connectsend(port,host,filename)
        connthread.start()
        
class Connectsend(threading.Thread):

	def __init__(self,port,host,filename):
		threading.Thread.__init__(self)
		self.port=port
		self.host=host
		self.filename=filename
		
	def run(self):
		dim=os.path.getsize(self.filename)
		outgoing=open(self.filename,'rb')
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((self.host,self.port))
		splitted=self.filename.split('/')
		name=splitted[-1]
		strf=name+'/'

		for a in strf:  sock.sendall(bytes(a,'UTF-8'))
		       

		print('Sending file: '+self.filename)
		i=0
		while 1:
		  i+=1
		  data=outgoing.read(4096)
		  if not data: break
		  sock.sendall(data)
		  perc=round((100*i*4096)/(dim),0)
		  pb['value']=perc
		  progress['text']=perc,'%'
		 
		  
		  
		
		outgoing.close()
		sock.close()
		pb['value']=0
		progress['text']=0
		messagebox.showinfo("Uploader","Completed")
        
        


root=Tk()
root.title('Uploader')
root.geometry('400x200')
inputs=Frame(root)
buttons=Frame(root)

port_lab=Label(inputs,text='Port')
host_lab=Label(inputs,text='Host')
port_val=Entry(inputs)
host_val=Entry(inputs)
port_lab.grid(row=0,column=0)
host_lab.grid(row=1,column=0)
port_val.grid(row=0,column=1)
host_val.grid(row=1,column=1)

pb=ttk.Progressbar(buttons,mode='determinate',maximum=100)
progress=Label(buttons,text='o%')

upload=Button(buttons,text='Upload',command=upload)
upload.pack(side=LEFT)
progress.pack(side=RIGHT)
pb.pack(side=RIGHT)
inputs.pack(side=TOP)
buttons.pack(side=BOTTOM)
root.mainloop()

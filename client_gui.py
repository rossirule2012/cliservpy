from tkinter import *
from tkinter import filedialog
from tkinter import ttk
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
        connectsend(port,host,filename)
        
def connectsend(port,host,filename):
        dim=os.path.getsize(filename)
        outgoing=open(filename,'rb')
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((host,port))
        splitted=filename.split('/')
        name=splitted[-1]
        strf=name+'/'

        for a in strf:     #sending filename one charater at time#
                print(a)
                sock.sendall(bytes(a,'UTF-8'))

        print('Sending file: '+filename)
        i=0
        while 1:
          data=outgoing.read(4096)
          if not data: break
          sock.sendall(data)
          perc=round(100*i*4096/dim,0)
          pb['value']=perc
          i+=1
	
        outgoing.close()
        sock.close()
        messagebox.showinfo("Uploader","Completed")
        
        


root=Tk()
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
upload=Button(buttons,text='Upload',command=upload)
upload.pack(side=LEFT)
pb.pack(side=RIGHT)
r
inputs.pack(side=TOP)
buttons.pack(side=BOTTOM)
root.mainloop()

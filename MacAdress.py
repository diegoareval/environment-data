from uuid import getnode as get_mac
import subprocess
import sys
import os
from tkinter import *

def format_mac_adress():
  mac = get_mac()
  return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

def get_path():
  return '{0}\\test.bat'.format(os.path.dirname(os.path.abspath(__file__)))


def execute_bat():
  fullpath = get_path()
  test = subprocess.call([r'{0}'.format(fullpath)])

def clear(): 
  execute_bat()

if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 
	gui.configure(background="light green") 
	gui.title("{0}".format(format_mac_adress())) 
	gui.geometry("270x150") 
	equation = StringVar() 
	expression_field = Entry(gui, textvariable=equation) 
	expression_field.grid(columnspan=4, ipadx=70) 
	equation.set('Execute your bat file') 
	clear = Button(gui, text='Execute Bat', fg='white', bg='black', 
				command=clear, height=1, width=7) 
	clear.grid(row=5, column='1') 


	# start the GUI 
	gui.mainloop() 




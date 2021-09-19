# importing whole module 
from tkinter import *
from tkinter.ttk import *

# importing strftime function to 
# retrieve system's time 
from time import strftime

# creating tkinter window 
root = Tk() 
root.title('Clock') 

# This function is used to 
# display time on the label 
def date(): 
	string = strftime('%Y/%m/%d \n %A') #%p for am/pm
	lbl.config(text = string) 
	lbl.after(1000, date) 


# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(root, font = ('calibri', 40, 'bold'), 
			background = 'red',
			foreground = 'yellow') 

# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center') 
date() 

root.resizable(0,0) # to fix the frame size or fix geometry
mainloop()

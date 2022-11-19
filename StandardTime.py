from tkinter import * 
from tkinter.ttk import *  
from time import strftime 

root = Tk() 
root.title('Clock') 

# This function is used to display time on the label 
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

  
# Styling the label widget.

lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'blue', 
            foreground = 'white') 

# Placing clock at the centre
lbl.pack(anchor = 'center') 
time() 

mainloop() 
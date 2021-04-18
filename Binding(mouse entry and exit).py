from tkinter import *
from tkinter.ttk import *
import datetime
from datetime import datetime 

root = Tk()
root.geometry('1500x750')
 
MouseList=[]
def enter(event):
    Save=open("Mouse Hacking.txt","a")
    print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))
    Save.write(f"Entry at X-> {event.x}   Y-> {event.y}                         @  {datetime.now()}\n")
    Save.close()
 

def exit0(event):
    Save=open("Mouse Hacking.txt","a")
    print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))
    Save.write(f"Exit at X-> {event.x}   Y-> {event.y}                           @  {datetime.now()}\n")
    Save.close()
 
def currentcoordenates(event):
    Save=open("Mouse Hacking.txt","a")
    x, y = event.x, event.y
    print(f"X -->{x}  :  Y --> {y}") 
    Save.write(f"X -->{x}  :  Y --> {y}                           @  {datetime.now()}\n")
    Save.close()

frame1 = Frame(root, height = 750, width = 1500)
 
frame1.bind('<Enter>', enter)
frame1.bind('<Leave>', exit0)
frame1.bind("<Motion>",currentcoordenates)
frame1.pack()
 
root.attributes("-alpha",0.01)

mainloop()

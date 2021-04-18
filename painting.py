from tkinter import*

canvas_width = 600
canvas_height = 400



def paint(event):
    color = colorvar.get()
    x1,y1=(event.x-5),(event.y-5)
    x2,y2=(event.x+5),(event.y+5)
    can_obj.create_oval(x1,y1,x2,y2,fill=color)

def clearall():
    can_obj.delete("all")

def colchange():
    color=colorvar.get()

main=Tk()
main.title("Painting")

colorvar=StringVar()
colorvar.set("lightgrey")
color = colorvar.get()

colorbuttons1=Radiobutton(main,text="Black",value="Black",variable=colorvar,indicatoron=False,command=colchange)
colorbuttons1.pack(anchor=N)
colorbuttons2=Radiobutton(main,text="Red",value="Red",variable=colorvar,indicatoron=False,command=colchange)
colorbuttons2.pack(anchor=N)
colorbuttons3=Radiobutton(main,text="Green",value="Green",variable=colorvar,indicatoron=False,command=colchange)
colorbuttons3.pack(anchor=N)
colorbuttons4=Radiobutton(main,text="Blue",value="Blue",variable=colorvar,indicatoron=False,command=colchange)
colorbuttons4.pack(anchor=N)


can_obj = Canvas(main,width=600,height=400)
can_obj.pack(expand=YES,fill=BOTH)
can_obj.bind("<B1-Motion>",paint)

message = Label(main,text="press mouse to paint")
message.pack(side=BOTTOM)

button=Button(main,text="Clear",command=clearall)
button.pack(side=BOTTOM)




mainloop()
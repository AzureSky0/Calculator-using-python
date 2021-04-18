from tkinter import*

main=Tk()
main.geometry("520x520")
main.title("Simple Calculator")

#frames:
DisplayFrame = Frame(main,width=500,height=100,bg="BLUE",relief=GROOVE,borderwidth=5)
DisplayFrame.grid(padx=10,column=0,row=0)

InputFrame = Frame(main,width=500,height=400,bg="Aqua",relief=GROOVE,borderwidth=3)
InputFrame.grid(padx=10,column=0,row=1,ipadx=1,ipady=2)

NumInputbuttons = [7,8,9,4,5,6,1,2,3,0]

OperationInputButton = ["/","*","-","+"]

Numvariable=IntVar()
Numvariable.set(10)
Operationvariable=StringVar()
Operationvariable.set("<>")
vara=0
varb=0
var="a"
A=0
B=0
def changeOnHover(button, colorOnHover, colorOnLeave): 
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover)) 
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))


def NumDisplay():
    global var 

    if var=="a":
        global A
        print(f"pressed Number is {Numvariable.get()} and identifier is {var}")
        vara=Numvariable.get()
        A=vara 
        var="b" 
        print(f"A={vara}")
          
    elif var=="b":
        global B
        print(f"pressed Number is {Numvariable.get()} and identifier is {var}")
        varb=Numvariable.get()
        B=varb
        var="a"
        print(f"B={varb}") 
         
    

def OperationDisplay():
    pass    

DisplayLable=Label(DisplayFrame,text=f"{A}  {Operationvariable.get()}  {B}",font=(8),width=40,height=2)
DisplayLable.grid(row=0,column=0)

def EventDisplay():
    global DisplayLable1
    DisplayLable1=Label(DisplayFrame,text=f"{A}  {Operationvariable.get()}  {B}",font=(8),width=40,height=2)
    DisplayLable1.grid(row=0,column=0)

def SubmitDisplay():
    global DisplayLable1
    Op=Operationvariable.get()

    if Op == "/":
        result=A/B
        print(result)
    elif Op == "*":
        result=A*B
        print(result) 
    elif Op == "-":
        result=A-B
        print(result) 
    elif Op == "+":
        result=A+B
        print(result)
    else:
        result="Error..."
    Displayresult=f"""{A}  {Operationvariable.get()}  {B}   =>  {result}"""
    DisplayLable1=Label(DisplayFrame,text=Displayresult,font=(8),width=40,height=2)
    DisplayLable1.grid(row=0,column=0)


    
    


col=0
rows=0
for i in NumInputbuttons:
    
    button=Radiobutton(InputFrame,text=i,variable=Numvariable,value=i,command=lambda:[NumDisplay(),EventDisplay()],indicatoron=False,width=16,height=4,bg="lightGrey")
    button.grid(column=col,row=rows,columnspan=1)
    col+=1
    changeOnHover(button, "grey", "lightGrey")
    if col==3:
        rows+=1
        col=0
    
    if i ==0:
        button.configure(width=51,height=4)
        button.grid_configure(columnspan=3)
    else:
        button.grid_configure(columnspan=1)
rows=0
for i in OperationInputButton:
    
    button=Radiobutton(InputFrame,text=i,variable=Operationvariable,value=i,command=lambda:[OperationDisplay(),EventDisplay()],indicatoron=False,width=16,height=4,bg="white")
    button.grid(column=4,row=rows)
    rows+=1
    changeOnHover(button, "lightBlue", "white")
    
def ResetDisplay():
    global var 
    Numvariable.set(10)
    Operationvariable.set("<>")
    var="a"
    DisplayLable1.configure(text="_______________________________")
    
    





submitbutton=Button(InputFrame,command=SubmitDisplay,text="Submit",width=68,height=4)
submitbutton.grid(row=4,column=0,columnspan=5,padx=2,pady=4)
changeOnHover(submitbutton, "lightgreen", "white")

ResetButton = Button(DisplayFrame,command=ResetDisplay,text="Reset",width=16,height=4)
ResetButton.grid(row=0,column=1,columnspan=2,rowspan=2)
changeOnHover(ResetButton, "Red", "white")


mainloop()

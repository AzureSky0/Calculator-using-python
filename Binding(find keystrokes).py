from tkinter import*
from tkinter import messagebox
main=Tk()
main.geometry("400x400")
main.title("Binding")



def msg():
    messagebox.showinfo( "Just a message box", "Press any key on the keyboard")

button = Button( main, text='Click me for next step', background = 'lightgrey', fg = 'blue', command = msg,width=40,height=5)
button.pack(padx=10,pady=20)


def Keyboardpress( key):
    key_char = key.char
    print( key_char, 'key button is pressed on the keyboard')
    val=f'{key_char}, key button is pressed on the keyboard'
    lable=Label(main,text=val)
    lable.pack(side=TOP,expand=True)
main.bind( '<Key>', lambda i : Keyboardpress(i))


mainloop()
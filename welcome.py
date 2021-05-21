from tkinter import *
from tkinter import messagebox

    
    
def imformation():
    messagebox.showinfo("imformation", "my name is Kamran. And l created this game alone.")
welcome = Tk()

def xesas():
    welcome.mainloop()
   
img = PhotoImage(file = "reklam.png")
welcome.geometry("380x800")
welcome.title("welcome XOgame")
label = Label(welcome, image = img).place(x =0.0 , y = 0.0)
button1 = Button(welcome, text = "Start", command = xesas).place(x = 100, y =300)
button2 = Button(welcome, text = "About us", command = imformation).place(x = 200, y =300,)

welcome.mainloop()
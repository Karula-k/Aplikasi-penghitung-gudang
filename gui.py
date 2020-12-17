from tkinter import *
import tkinter.messagebox

class GUI:
    pass
class main_gui(GUI):
    def __init__(self,root):
        self.root =root
        self.root.title("Aplikasi penghitung gudang")
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="Lime")
        mainframe = Frame(self.root)
        mainframe.grid()
        border = LabelFrame(text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        border.grid(row=1,column=2)
        l1 = Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        l1.grid(row=1, column=2)
        B1 = Button(border, text="Submit", font=("Arial", 15), command=lambda :  (login_gui(self.root)))
        self.root.mainloop()

class login_gui(GUI):
    def __init__(self,root):
        self.root =root
        self.root.title("Aplikasi penghitung gudang")
        self.root.geometry("400x400+0+0")
        self.root.config(bg="Magenta")
        mainframe = Frame(self.root)
        mainframe.grid()
        border = LabelFrame(text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        border.grid(row=1,column=2)
        l1 = Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        l1.grid(row=1, column=2)
        B1 = Button(border, text="Submit", font=("Arial", 15), command=lambda :  (main_gui(self.root)))
        B1.grid(row=3, column=1)
        self.root.mainloop()

root = Tk()
aang =login_gui(root)
aang
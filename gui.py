import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sql import *
from main import *
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="DarkOliveGreen1")

        label = tk.Label(self)
        label.place(x=0,y=0)
        
        border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width = 30, bd = 5)
        T1.place(x=180, y=20)
        
        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width = 30, show='*', bd = 5)
        T2.place(x=180, y=80)
        
        def verify():
            try:
                sign = 0
                for i in uy.Call_data():
                    if i[1].strip()==T1.get() and i[2].strip()==T2.get():
                        controller.show_frame(SecondPage)
                        sign=1
                if sign==0:
                    messagebox.showinfo("error","your account not registered yet")

            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")
         
        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)
        B2 = tk.Button(border, text="Register", bg = "Bisque3", font=("Arial",15), command=lambda: controller.show_frame(ThirdPage))
        B2.place(x=50, y=115)
        
class SecondPage(tk.Frame):
    count=None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="cadet blue")
        mainframe = tk.Frame(self)
        mainframe.grid()
        
        tree_frame = tk.Frame(mainframe)
        tree_frame.grid(row=0,column=3,sticky='s')
        style = ttk.Style(mainframe)
        style.configure('page2.Treeview', rowheight=45)
        tree_scroll = tk.Scrollbar(tree_frame)
        tree_scroll.pack(side='right', fill='y')
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended",style='page2.Treeview')
        my_tree.pack(fill='both')
        tree_scroll.config(command=my_tree.yview)
        my_tree['columns'] = ("id","Name", "Supplier", "harga","Tanggal Masuk")
        my_tree.column("#0", width=0, stretch='no')
        my_tree.column("id", anchor='w', width=120)
        my_tree.column("Name", anchor='w', width=130)
        my_tree.column("Supplier", anchor='center', width=130)
        my_tree.column("harga", anchor='w', width=130)
        my_tree.column("Tanggal Masuk", anchor='w', width=130)
        def orderby(c1):
            data1 = ayam.order_by(c1)
            for i in data1:
                my_tree.insert(parent='', index='end', text="", values=(i[0],i[1], i[2], i[3],i[4]))

        # Create Headings 
        my_tree.heading("#0", text="", anchor='w')
        my_tree.heading("id", text="ID", anchor='center')
        my_tree.heading("Name", text="Name", anchor='center')#,command = orderby("Name"))
        my_tree.heading("Supplier", text="Supplier", anchor='center')
        my_tree.heading("harga", text="harga", anchor='center')
        my_tree.heading("Tanggal Masuk", text="Tanggal Masuk", anchor='center')
        add_frame = tk.Frame(mainframe)
        add_frame.grid(row=5,column=3)
        #Entry boxes
        idstr = tk.StringVar()
        id_str = tk.Entry(add_frame,text = idstr,state=tk.DISABLED,width=25)
        id_str.grid(row =0 ,column =0,sticky='w')
        name_str = tk.Entry(add_frame)
        name_str.grid(row=0, column=1)

        Spp_str = tk.Entry(add_frame)
        Spp_str.grid(row=0, column=2)

        hargaint = tk.Entry(add_frame)
        hargaint.grid(row=0, column=3)
        tgl_str = tk.Entry(add_frame)
        tgl_str.grid(row=0,column=4)
        def remove_all():
        	for record in my_tree.get_children():
		        my_tree.delete(record)
        def view():
            remove_all()
            data = ayam.viewData()
            for record in data:
                my_tree.insert(parent='', index='end', text="", values=(record[0],record[1], record[2], record[3],record[4]))
     
        def add_values():
            ayam.add_items(name_str.get(),Spp_str.get(),hargaint.get(),tgl_str.get())
            remove_all()
            view()
            idstr.set("")
            name_str.delete(0, tk.END)
            Spp_str.delete(0, tk.END)
            hargaint.delete(0, tk.END)
            tgl_str.delete(0,tk.END)
        def remove_many():
            x = my_tree.selection()
            #y = my_tree.item(my_tree.selection())["name"]
            print(x)
            for record in x:
                remove_all()
                ayam.delete_items(id_str.get())
                view()
            idstr.set("")
            name_str.delete(0, tk.END)
            Spp_str.delete(0, tk.END)
            hargaint.delete(0, tk.END)
            tgl_str.delete(0,tk.END)

        def select_case():
            idstr.set("")
            name_str.delete(0, tk.END)
            Spp_str.delete(0, tk.END)
            hargaint.delete(0, tk.END)
            tgl_str.delete(0,tk.END)
            selected = my_tree.focus()
            values = my_tree.item(selected, 'values')
            print(values)
            idstr.set(values[0])
            name_str.insert(0, values[1])
            Spp_str.insert(0, values[2])
            hargaint.insert(0, values[3])
            tgl_str.insert(0, values[4])
        def update():
            selected = my_tree.focus()
            ayam.Data_Update(name_str.get(),Spp_str.get(),hargaint.get(),tgl_str.get(),id_str.get())
            remove_all()
            view()
            idstr.set("")
            name_str.delete(0, tk.END)
            Spp_str.delete(0, tk.END)
            hargaint.delete(0, tk.END)
            tgl_str.delete(0,tk.END)

        def selectItem(e):
            select_case()
        btn_plc = tk.Frame(mainframe)
        btn_plc.grid(column=0,row=0)
        view_btn = tk.Button(btn_plc, text="View", font=("Arial", 15),relief='ridge' ,width=10, command= view)
        view_btn.pack(pady=20,padx=10)
        insert_btn = tk.Button(btn_plc, text="Insert", font=("Arial", 15),relief='ridge' ,width=10, command= add_values)
        insert_btn.pack(pady=20,padx=10)
        Log_outbtn = tk.Button(btn_plc, text="Back", font=("Arial", 15),relief='ridge',width=10, command=lambda: controller.show_frame(FirstPage))
        Log_outbtn.pack(pady=20,padx=10)
        del_btn = tk.Button(btn_plc, text="Delete", font=("Arial", 15),relief='ridge',width=10, command=lambda: remove_many())
        del_btn.pack(pady=20,padx=10)
        Update_btn = tk.Button(btn_plc, text="Update", font=("Arial", 15),relief='ridge',width=10, command=lambda: update() )
        Update_btn.pack(pady=20,padx=10)
        my_tree.bind("<ButtonRelease-1>", selectItem)
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='Tomato')
        #variable
        signnbdr = tk.LabelFrame(self, text='Sign Up', bg='ivory', bd = 10, font=("Arial", 20))
        signnbdr.pack(side='left',expand='yes',fill='both')
        signnbdr.place(x=200,y=80,width=400,height=300)
        usernamelb = tk.Label(signnbdr, text="Username",font=("Arial Bold", 15), bg='ivory')
        usernamelb.place(x=20, y=20)
        usernament = tk.Entry(signnbdr, width = 30, bd = 5)
        usernament.place(x=160, y=20)
        
        passwordlb = tk.Label(signnbdr,anchor='w' ,text="Password",font=("Arial Bold", 15), bg='ivory')
        passwordlb.place(x=20, y=80)
        passworden = tk.Entry(signnbdr, width = 30, show='*', bd = 5)
        passworden .place(x=160, y=80)

        repasswordlb = tk.Label(signnbdr, text="Re Password", font=("Arial Bold", 15), bg='ivory')
        repasswordlb.place(x=20, y=140)
        repassworden = tk.Entry(signnbdr, width = 30, show='*', bd = 5)
        repassworden.place(x=160, y=140)  
        
        log_out_btn = tk.Button(signnbdr, text="Log in", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        log_out_btn.place(x=10, y=200)
        def submit():
            if usernament.get() !="" and passworden.get() !="" and repassworden.get() != "":
                if passworden.get() == repassworden.get():
                    user=usernament.get()
                    pas=passworden.get()
                    ayam2.Data_Pengguna(user,pas)
                else:
                    messagebox.showinfo("error","password not match")
            else:
                messagebox.showinfo("error","pls fill all of the entry")
        Button = tk.Button(signnbdr, text="Submit", font=("Arial", 15), command=submit)
        Button.place(x=280, y=200)
        
        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")
            
app = Application()
app.maxsize(800,500)
app.mainloop()
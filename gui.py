import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sql import *
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        global db
        tk.Frame.__init__(self, parent)
        self.configure(bg="DarkOliveGreen1")
        
        border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx = 150, pady=150)
        border.place(x=170,y=140,width=500,height=200)
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
                for i in db[1].Call_data():
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

        global db
        mainframe.grid()
        
        tree_frame = tk.Frame(mainframe)
        tree_frame.grid(row=0,column=3,sticky='n')
        style = ttk.Style(mainframe)
        style.configure('page2.Treeview', rowheight=36)
        xtree_scroll = tk.Scrollbar(tree_frame,orient='horizontal')
        xtree_scroll.pack(side='bottom',fill='x')
        tree_scroll = tk.Scrollbar(tree_frame)
        tree_scroll.pack(side='right', fill='y')
        my_tree = ttk.Treeview(tree_frame,xscrollcommand = xtree_scroll.set, yscrollcommand=tree_scroll.set, selectmode="browse",style='page2.Treeview')
        my_tree.pack(fill='both')
        tree_scroll.config(command=my_tree.yview)
        xtree_scroll.config(command=my_tree.xview)
        my_tree['columns'] = ("id","Name", "Supplier", "harga","Tanggal Masuk","Rak","type","Dimensi","Expire_cair")
        my_tree.column("#0", width=0, stretch='no')
        my_tree.column("id", anchor='w', width=60,minwidth=120)
        my_tree.column("Name", anchor='w', width=70,minwidth=120)
        my_tree.column("Supplier", anchor='center', width=70,minwidth=120)
        my_tree.column("harga", anchor='w', width=70,minwidth=120)
        my_tree.column("Tanggal Masuk", anchor='w', width=80,minwidth=130)
        my_tree.column("Rak", anchor='w', width=70,minwidth=120)
        my_tree.column("type", anchor='w', width=70,minwidth=120)
        my_tree.column("Dimensi", anchor='w', width=80,minwidth=130)
        my_tree.column("Expire_cair", anchor='w', width=70,minwidth=120)
        # Create Headings 
        my_tree.heading("#0", text="", anchor='w')
        my_tree.heading("id", text="ID", anchor='center')
        my_tree.heading("Name", text="Name", anchor='center')#,command = orderby("Name"))
        my_tree.heading("Supplier", text="Supplier", anchor='center')
        my_tree.heading("harga", text="harga", anchor='center')
        my_tree.heading("Tanggal Masuk", text="Tanggal Masuk", anchor='center')
        my_tree.heading("Rak", text="Rak", anchor='center')
        my_tree.heading("type", text="Type Benda", anchor='center')
        my_tree.heading("Dimensi", text="Dimensi Benda", anchor='center')
        my_tree.heading("Expire_cair", text="Expire kode kimia", anchor='center')
        add_frame = tk.Frame(mainframe)
        add_frame.grid(row=1,column=3)
        #label boxes
        idstr = tk.StringVar()
        idlbl = tk.Label(add_frame,text="ID")
        idlbl.grid(row=0,column=0)
        namelbl = tk.Label(add_frame,text="Nama")
        namelbl.grid(row=0,column=1)
        Spplbl = tk.Label(add_frame,text="Supplier")
        Spplbl.grid(row=0,column=2)
        hargalbl = tk.Label(add_frame,text="Harga")
        hargalbl.grid(row=0,column=3)
        tgllbl = tk.Label(add_frame,text="Tanggal")
        tgllbl.grid(row=0,column=4)
        raklbl = tk.Label(add_frame,text="Rak")
        raklbl.grid(row=2,column=1)
        typelbl = tk.Label(add_frame,text="Type")
        typelbl.grid(row=2,column=2)
        Dmnlbl = tk.Label(add_frame,text="Dimensi")
        Dmnlbl.grid(row=2,column=3)
        Expirelbl = tk.Label(add_frame,text="Expired")
        Expirelbl.grid(row=2,column=4)
        
        #entry boxes
        id_str = tk.Entry(add_frame,text = idstr,state=tk.DISABLED)
        id_str.grid(row =1 ,column =0,sticky='w',pady=5)
        name_str = tk.Entry(add_frame)
        name_str.grid(row=1, column=1,pady=5,sticky='w')

        Spp_str = tk.Entry(add_frame)
        Spp_str.grid(row=1, column=2,pady=5,sticky='w')

        hargaint = tk.Entry(add_frame)
        hargaint.grid(row=1, column=3,pady=5,sticky='w')
        tgl_str = tk.Entry(add_frame)
        tgl_str.grid(row=1,column=4,pady=5,sticky='w')
        rak_str = tk.Entry(add_frame)
        rak_str.grid(row=3,column=1,pady=5)
        type_str = tk.Entry(add_frame)
        type_str.grid(row=3,column=2,pady=5)
        dimensi_str=tk.Entry(add_frame)
        dimensi_str.grid(row=3,column=3,pady=5)
        expire_str = tk.Entry(add_frame)
        expire_str.grid(row=3,column=4,pady=5)
        def remove_all():
        	for record in my_tree.get_children():
		        my_tree.delete(record)
        def view():
            remove_all()
            data = db[0].viewData()
            for record in data:
                my_tree.insert(parent='', index='end', text="", values=(record[0],record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8]))
        def add_values():
            if name_str.get()!="" and Spp_str.get()!="" and hargaint.get()!="" and tgl_str.get()!="" and\
                 rak_str.get() !="" and type_str.get()!="" :
                dn.add_br(name_str.get(),Spp_str.get(),hargaint.get(),tgl_str.get(),rak_str.get(),type_str.get(),
                dimensi_str.get(),expire_str.get())
            else:
                messagebox.showinfo('Error',"please fill the entry")
            remove_all()
            view()
            idstr.set("")
            name_str.delete(0, tk.END)
            Spp_str.delete(0, tk.END)
            hargaint.delete(0, tk.END)
            tgl_str.delete(0,tk.END)
            rak_str.delete(0,tk.END)
            type_str.delete(0,tk.END)
            dimensi_str.delete(0,tk.END)
            expire_str.delete(0,tk.END)
        def remove_many():
            x = my_tree.selection()
            #y = my_tree.item(my_tree.selection())["name"]
            print(x)
            for record in x:
                remove_all()
                db[0].delete_items(id_str.get())
                view()
            idstr.set("")
            name_str.delete(0, tk.END)
            Spp_str.delete(0, tk.END)
            hargaint.delete(0, tk.END)
            tgl_str.delete(0,tk.END)
            rak_str.delete(0,tk.END)
            type_str.delete(0,tk.END)
            dimensi_str.delete(0,tk.END)
            expire_str.delete(0,tk.END)

        def select_case():
            idstr.set("")
            name_str.delete(0, tk.END)
            Spp_str.delete(0, tk.END)
            hargaint.delete(0, tk.END)
            tgl_str.delete(0,tk.END)
            rak_str.delete(0,tk.END)
            type_str.delete(0,tk.END)
            dimensi_str.delete(0,tk.END)
            expire_str.delete(0,tk.END)
            selected = my_tree.focus()
            values = my_tree.item(selected, 'values')
            print(values)
            idstr.set(values[0])
            name_str.insert(0, values[1])
            Spp_str.insert(0, values[2])
            hargaint.insert(0, values[3])
            tgl_str.insert(0, values[4])
            rak_str.insert(0,values[5])
            type_str.insert(0,values[6])
            dimensi_str.insert(0,values[7])
            expire_str.insert(0,values[8])
        def update():
            selected = my_tree.focus()
            db[0].update(name_str.get(),Spp_str.get(),hargaint.get(),tgl_str.get(),rak_str.get(),type_str.get(),
            dimensi_str.get(),expire_str.get(),id_str.get())
            remove_all()
            view()
            idstr.set("")
            name_str.delete(0, tk.END)
            Spp_str.delete(0, tk.END)
            hargaint.delete(0, tk.END)
            tgl_str.delete(0,tk.END)
            rak_str.delete(0,tk.END)
            type_str.delete(0,tk.END)
            dimensi_str.delete(0,tk.END)
            expire_str.delete(0,tk.END)
        def search():
            remove_all()
            data = db[0].Search_Data(name_str.get(),Spp_str.get(),hargaint.get(),tgl_str.get(),rak_str.get(),type_str.get(),
            dimensi_str.get(),expire_str.get())
            for record in data:
                my_tree.insert(parent='', index='end', text="", values=(record[0],record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8]))
            idstr.set("")
            name_str.delete(0, tk.END)
            Spp_str.delete(0, tk.END)
            hargaint.delete(0, tk.END)
            tgl_str.delete(0,tk.END)
            rak_str.delete(0,tk.END)
            type_str.delete(0,tk.END)
            dimensi_str.delete(0,tk.END)
            expire_str.delete(0,tk.END)
        def selectItem(e):
            select_case()
        def on_double_click(e):
            region =my_tree.identify_column(e.x)
            region = int(region.strip('#'))-1
            print(region)
            my_column= ["id","Name", "Supplier", "harga","Tanggal Masuk","Rak","type","Dimensi","Expire_cair"]
            data = db[0].order_by(my_column[region])
            remove_all()
            for record in data:
                my_tree.insert(parent='', index='end', text="", values=(record[0],record[1], record[2], record[3],record[4],record[5],record[6],record[7],record[8]))
        #button
        btn_plc = tk.Frame(mainframe)
        btn_plc.grid(column=0,row=0)
        view_btn = tk.Button(btn_plc, text="View", font=("Arial", 15),relief='ridge' ,width=10, command= view)
        view_btn.pack(pady=5,padx=10)
        insert_btn = tk.Button(btn_plc, text="Insert", font=("Arial", 15),relief='ridge' ,width=10, command= add_values)
        insert_btn.pack(pady=5,padx=10)
        Log_outbtn = tk.Button(btn_plc, text="Back", font=("Arial", 15),relief='ridge',width=10, command=lambda: controller.show_frame(FirstPage))
        Log_outbtn.pack(pady=5,padx=10)
        del_btn = tk.Button(btn_plc, text="Delete", font=("Arial", 15),relief='ridge',width=10, command=lambda: remove_many())
        del_btn.pack(pady=5,padx=10)
        Update_btn = tk.Button(btn_plc, text="Update", font=("Arial", 15),relief='ridge',width=10, command=lambda: update() )
        Update_btn.pack(pady=5,padx=10)
        Search_btn = tk.Button(btn_plc, text="Search", font=("Arial", 15),relief='ridge',width=10, command=lambda: search() )
        Search_btn.pack(pady=5,padx=10)
        my_tree.bind("<ButtonRelease-1>", selectItem)
        my_tree.bind("<Double-1>",on_double_click)
class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global db
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
                    for i in db[1].Call_data():
                        if i[1].strip()==usernament.get() and i[2].strip()==passworden.get():
                            messagebox.showinfo("Error","Data Already taken")
                            break
                    else:
                        user=usernament.get()
                        pas=passworden.get()
                        db[1].Data_Pengguna(user,pas)
                        messagebox.showinfo("Succes","your account has registed")
                        controller.show_frame(FirstPage)
                else:
                    messagebox.showinfo("error","password not match")
            else:
                messagebox.showinfo("error","pls fill all of the entry")
        Button = tk.Button(signnbdr, text="Submit", font=("Arial", 15), command=submit)
        Button.place(x=280, y=200)
        
        
class Application(tk.Tk):
    def __init__(self,db_name,table_name, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global db
        db =[Data_source(db_name,table_name),login_call(db_name)]
        #creating a window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize =500)
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

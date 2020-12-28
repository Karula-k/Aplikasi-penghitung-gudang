import sqlite3
class Data_source:
    def __init__(self,db_name,table_name="stockGudang"):
        self.db_name =db_name+".db"
        self.table_name = table_name
        con =sqlite3.connect(self.db_name)
        cur=con.cursor()
        create_text ="create table if not exists "+self.table_name+" (id integer primary key,name text, \
            Supplier text, harga integer,tanggal_masuk date)"
        cur.execute(create_text)
        con.commit()
        con.close()

    def add_items(self,name,Supplier,harga,tanggal_masuk):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("insert into "+self.table_name+" values (NULL,?,?,?,?)",(name,Supplier,harga,tanggal_masuk))
        con.commit()
        con.close()
    def viewData(self):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("Select * From "+self.table_name)
        rows =cur.fetchall()
        con.close()
        return rows

    def delete_items(self,id):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("DELETE FROM "+self.table_name+" Where id=?",(id,))
        con.commit()
        con.close()

    def Search_Data(self,name="",Supplier="",harga="",tanggal_masuk=""):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        text ="Select * From "+self.table_name+" where name=? or Supplier=? or harga=? or tanggal_masuk=?"
        cur.execute(text,(name,Supplier,harga,tanggal_masuk))
        rows =cur.fetchall()
        con.close()
        return rows

    def Data_Update (self,name=None,Supplier=None,harga=None,tanggal_masuk=None,idbr=-1):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        dict_items = {"name":name,"Supplier":Supplier,"harga":harga,"tanggal_masuk":tanggal_masuk}
        text2 = {k: v for k, v in dict_items.items() if v is not None}
        text ="Update "+self.table_name+" Set "+",".join([i+"="+"'"+text2[i]+"'"for i in text2])+" \
            where id="+str(idbr)
        cur.execute(text)
        con.commit()
        con.close()
    def order_by(self,type_cl):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        text ="select * from "+self.table_name+" order by "+type_cl
        cur.execute(text)
        row =cur.fetchall()
        con.commit()
        con.close()
        return row
class Login_syt:
    def __init__(self,db_name,table_name="Datauser"):
        self.db_name =db_name+".db"
        self.data = table_name
        con =sqlite3.connect(self.db_name)
        cur=con.cursor()
        create_text ="create table if not exists "+self.data+" (id integer primary key,username text,Password text)"
        cur.execute(create_text)
        con.commit()
        con.close()
                
    def Data_Pengguna(self, Username, Password):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("insert into "+self.data+" values (NULL,?,?)",(Username,Password))
        con.commit()
        con.close()

ayam = Data_source("ayam","stocks")
ayam2 = Login_syt('ayam')
# ayam2.Data_Pengguna("usop",'pembohong')
# ayam.Data_Update("ayam")

# data1 = Login(input("Masukkan Username : "), input("Masukkan Password : "))
# print(data1.Data_Pengguna())



class login_call(Data_source):
    def __init__(self, db_name, table_name='Datauser'):
        super().__init__(db_name, table_name=table_name)
    
    def Search_Data(self,Username,Password):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("Select * From "+self.table_name+" where username=? and password=?",(Username,Password))
        row = cur.fetchall()
        con.commit()
        con.close()
        return row
    def Call_data(self):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("Select * From "+self.table_name)
        row = cur.fetchall()
        con.commit()
        con.close()
        return row
uy = login_call("ayam")
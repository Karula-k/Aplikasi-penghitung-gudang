import sqlite3
import abc
class barang(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addItems(self):
        pass
    @abc.abstractmethod
    def DataUpdate(self):
        pass
class liquid(barang):
    def addItems(self,name,Supplier,harga,tanggal_masuk,rak,type_benda,dimensi,expire_liquid):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("insert into "+self.table_name+" values (NULL,?,?,?,?,?,?,?,?)",
        (name,Supplier,harga,tanggal_masuk,rak,type_benda,dimensi,expire_liquid))
        con.commit()
        con.close()

    def DataUpdate (self,name=None,Supplier=None,harga=None,tanggal_masuk=None,rak=None,type_benda=None,dimensi=None,expire_liquid=None,idbr=-1):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        dict_items = {"name":name,"Supplier":Supplier,"harga":harga,"tanggal_masuk":tanggal_masuk,"rak":rak,"\
            type_benda":type_benda,"dimensi_benda":dimensi,"expire_liquid":expire_liquid}
        text2 = {k: v for k, v in dict_items.items() if v is not None}
        text ="Update "+self.table_name+" Set "+",".join([i+"="+"'"+text2[i]+"'"for i in text2])+" \
            where id="+str(idbr)
        cur.execute(text)
        con.commit()
        con.close()    
class padatan(barang):
    def addItems(self,name,Supplier,harga,tanggal_masuk,rak,type_benda,dimensi_benda):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("insert into "+self.table_name+" values (NULL,?,?,?,?,?,?,?,NULL)",
        (name,Supplier,harga,tanggal_masuk,rak,type_benda,dimensi_benda))
        con.commit()
        con.close()
    def DataUpdate (self,name=None,Supplier=None,harga=None,tanggal_masuk=None,rak=None,type_benda=None,dimensi=None,idbr=-1):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        dict_items = {"name":name,"Supplier":Supplier,"harga":harga,"tanggal_masuk":tanggal_masuk,"rak":rak,"\
            type_benda":type_benda,"dimensi_benda":dimensi}
        text2 = {k: v for k, v in dict_items.items() if v is not None}
        text ="Update "+self.table_name+" Set "+",".join([i+"="+"'"+text2[i]+"'"for i in text2])+",expire_liquid='None' \
            where id="+str(idbr)
        cur.execute(text)
        con.commit()
        con.close()    

class Data_source():
    def __init__(self,db_name,table_name="stockGudang"):
        self.db_name =db_name+".db"
        self.table_name = table_name
        con =sqlite3.connect(self.db_name)
        cur=con.cursor()
        create_text ="create table if not exists "+self.table_name+" (id integer primary key,name text, \
            Supplier text, harga integer,tanggal_masuk date,rak text,type_benda text,dimensi_benda text,expire_liquid\
                text)"
        cur.execute(create_text)
        con.commit()
        con.close()
    def add_br(self,*args):
        if args[5]=="liquid":
            h = liquid.addItems(self,args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7])
            print(args)
        else:
            h = padatan.addItems(self,args[0],args[1],args[2],args[3],args[4],args[5],args[6])
            print(args)
    def viewData(self):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("Select * From "+self.table_name)
        rows =cur.fetchall()
        con.close()
        return rows
    def update(self,*args):
        if args[5]=="liquid":
            h = liquid.DataUpdate(self,args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8])
            print(args)
        else:
            h = padatan.DataUpdate(self,args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[8])
            print(args)
    def delete_items(self,id):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        cur.execute("DELETE FROM "+self.table_name+" Where id=?",(id,))
        con.commit()
        con.close()
    def Search_Data(self,name="",Supplier="",harga="",tanggal_masuk="",rak="",type_benda="",dimensi_benda="",
        expire_liquid=""):
        con=sqlite3.connect(self.db_name)
        cur =con.cursor()
        text ="Select * From "+self.table_name+" where name=? or Supplier=? or harga=? or tanggal_masuk=? \
            or rak =? or type_benda=? or dimensi_benda=? or expire_liquid=?"
        cur.execute(text,(name,Supplier,harga,tanggal_masuk,rak,type_benda,dimensi_benda,expire_liquid))
        rows =cur.fetchall()
        con.close()
        return rows
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
class login_call(Login_syt):
    def __init__(self, db_name, table_name='Datauser'):
        super().__init__(db_name, table_name=table_name)
        self.table_name = table_name
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


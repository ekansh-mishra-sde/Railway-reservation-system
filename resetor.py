from tkinter import *
from tkinter import messagebox
import mysql.connector as sq
#============================================================>>
root=Tk()
root.title("change your password")
root.geometry('700x400')
#global b
#===========================================================>>
conn = sq.connect(host="localhost",user="root",password="Ekansh@123",database="test2",auth_plugin='mysql_native_password')
cursor = conn.cursor()
#============================================================>>
def executor(a):
    global _para
    _para = a
    Label(root, text=_para).grid(row=9, column=2)



#=============================================================>>
#enter pass

#=============================================================>>
root.mainloop()
#subse thasu module
#no validation from dbms
#it asks to add username,password and confirm password..
#checkbox to agree to terms and conditions of policy
#submit will add username and password to admin table in test2 db
from tkinter import *
from tkinter import messagebox
import mysql.connector as sq

#from ekanshDBMS.venv import signupWindow
root=Tk()
root.title("Generate UserName window")
root.geometry('900x250')
Label(root,text="LOGIN-ID Creation Page",font=('Orbitron',20),fg='red').grid(row=0,column=1)
#====================================================>
conn = sq.connect(host="localhost",user="root",password="Ekansh@123",database="test2",auth_plugin='mysql_native_password')
cursor = conn.cursor()
#====================================================>
def executor(email,username,password):
    #print(email,username,password_check_1)
    values = (username,password,email)
    sql = "INSERT INTO username VALUES(%s,%s,%s)"
    cursor.execute(sql, values)
    conn.commit()
def confirm_check():
    checkbox_value=var.get()
    if(checkbox_value==1):
        global email
        global username
        global password_check_1
        email=e4.get()
        username=e1.get()
        password_check_1=e2.get()
        password_check_2=e3.get()
        if ((password_check_1==password_check_2)and (len(password_check_1))>0):
            executor(email,username,password_check_1)
            messagebox.showinfo("success","All Done..Now Login")
            #from ekanshDBMS.venv import signupWindow
            root.destroy()
        else:
            messagebox.showinfo("Try Again","passwords not matched")
    else:
        messagebox.askretrycancel("Failed","All feilds required")
#====================================================>
var = IntVar()
username=Label(root,text="Username",font="calibri",justify=LEFT).grid(row=1,column=0)
password=Label(root,text="Password",font="calibri",justify=LEFT).grid(row=2,column=0)
confirm=Label(root,text="Confirm Password",font="calibri",justify=LEFT).grid(row=3,column=0)
email=Label(root,text="RE-ENTER EMAIL",font="calibri",justify=LEFT).grid(row=4,column=0)
agreement=Checkbutton(root,text="Do you agree to terms and conditions of our policy*",variable=var,onvalue = 1,offvalue = 0)
agreement.grid(row=5,column=0)
#Label(root,text=var.get()).grid(row=4,column=2)
#====================================================>
b1=Button(root,text="Submit",bg='Light pink',font="sans-serif",width=10,command=confirm_check).grid(row=6,column=1)
#====================================================>
e1=Entry(root,width=40)
e1.grid(row=1,column=3)
e2=Entry(root,width=40)
e2.grid(row=2,column=3)
e3=Entry(root,width=40)
e3.grid(row=3,column=3)
e4=Entry(root,width=40)
e4.grid(row=4,column=3)
#====================================================>
root.mainloop()



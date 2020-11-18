# this page will be added onreset button of trail page which was called from package(main) module
# it will check user's email-id if matched it will allow to reset password
# import sql module and then validate
from tkinter import *
from tkinter import messagebox
import mysql.connector as sq
#========================================================================================>
root = Tk()
root.geometry('800x600')
root.title('RESET PAGE FOR VALID USERS')
Label(root,text='                ').grid(row=0,column=0)
Label(root,text='WELCOME TO RESET PAGE',font='orbitron',fg='red').grid(row=0,column=1)
#=========================================================================================>
conn = sq.connect(host="localhost",user="root",password="Ekansh@123",database="test2",auth_plugin='mysql_native_password')
cursor = conn.cursor()
#===========================================================================================>
# global username1  ekansh.mishra1999@gmail.com
# global email1
# username1=''
# email1=''
def updater(a,b):
    if(a==b):
        cursor.execute("update username set password='{}' where username='{}'".format(a,username))
        conn.commit()
        messagebox.askokcancel("success","Your password has been reseted")
        root.destroy()
        from ekanshDBMS.venv import package
def executor():
    emailId = emailId_input.get()
    #print("emailid"+str(len(emailId))+emailId)
    cursor.execute("select username,email from username where email='{}'".format(emailId))
    items = cursor.fetchall()
    if(items[0][0]):
        global username
        username=str(items[0][0])
        str1="welcome "+str(items[0][0])
        str2="Please Reset ur password here"
        # Label(root,text=str1).grid(row=9,column=1)
        # Label(root, text=str2).grid(row=10, column=1)
        messagebox.askokcancel(str1,str2)
        Label(root,text="New-Password",font=('orbitron',18)).grid(row=11,column=0)
        Label(root, text="RE-Enter New-Password", font=('orbitron', 18)).grid(row=12, column=0)
        e1=Entry(root,width=40)
        e1.grid(row=11,column=1)
        e2=Entry(root,width=40)
        e2.grid(row=12,column=1)
        Button(root,text="Confirm",bg='pink',fg='black',command=lambda: updater(e1.get(),e2.get()),borderwidth=10).grid(row=12,column=3)

#=========================================================================================>
def resetFUnc():
    #username=username_input.get()
    emailId=emailId_input.get()
    if(emailId==''):
        messagebox.showerror("Error","Enter Valid Email")
    else:
        executor()
    #edit here by validatng users from sql
#==========================================================================================>
# Label(root,text=' ').grid(row=1,column=0)
# Label(root,text='OR',font='calibri').grid(row=5,column=1)
# Label(root,text=' ').grid(row=7,column=0)
#enter email id or username you last remember
# username=Label(root,text='Username',font=('arial',15),fg='blue').grid(row=4,column=0)
emailId=Label(root,text="EMAIL_ID",font=('arial',15),fg='blue').grid(row=6,column=0)
# username_input=Entry(root,width=30)
# username_input.grid(row=4,column=1)
emailId_input=Entry(root,width=40)
emailId_input.grid(row=6,column=1)
reset=Button(root,text="CHECK FOR VALIDATIDTY",fg='black',bg='pink',command=resetFUnc,borderwidth=10).grid(row=8,column=1)
#==========================================================================================>
root.mainloop()
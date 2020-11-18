#just creates signup window nothing else
#it is not validating users still now

from tkinter import *
from tkinter import messagebox
import mysql.connector as sq
root=Tk()
root.title("SIGN UP WINDOW")
root.geometry('600x400')
conn = sq.connect(host="localhost", user="root", password="Ekansh@123", database="test2",
                  auth_plugin='mysql_native_password')
cursor = conn.cursor()
#==============================================================================================>
def executor(sql,val):
    print("Vlaues inserted2")
    #cursor.execute(sql,val)
    print("Vlaues inserted3")
    cursor.executemany(sql,val)
    conn.commit()
def value_inserter():
    fname=e1.get()
    last=e2.get()#4,6,8
    email=e4.get()
    city=e5.get()
    pincode=e6.get()
    dob=e7.get()
    gender=e8.get()
    address=e9.get()
    values=(fname,last,email,city,pincode,dob,gender,address)
    sql="INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,values)
    print("Vlaues inserted3")
    conn.commit()
    # print("Vlaues inserted1")
    # print(values)
    # executor(sql,values)
    #items = cursor.fetchall()
def detail_checker():
    fname=e1.get()
    last=e2.get()#4,6,8
    email=e4.get()
    pincode=e6.get()
    gender=e8.get()
    #print(email,pincode,gender)
    if(fname==last):
        messagebox.askretrycancel("Error","Last name is same as First name")
        return 1
    if(pincode==''):
        messagebox.askretrycancel("pincode mandatory","pincode mandatory")
        return 1
    if (gender=='m'or gender=='f'):
        messagebox.askretrycancel("Gender mandatory", "type either M/F")
        return 1
    if (email == ''):
        messagebox.askretrycancel("email mandatory", "email mandatory")
        return 1

    return 0
def submit_button():
    value=detail_checker()
    # if(value==0):
    #
    # else:
    value_inserter()
    root.destroy()
    from ekanshDBMS.venv import generateUsernamePassword

    #pass
    #sign.destroy()
#==============================================================================================>
### sign up page for users
Label(root,text="SIGNUP FOR USERS",fg='red',font='arial').grid(row=1,column=1)
fname=Label(root,text="FIRST NAME",fg='black',font='arial').grid(row=2,column=0)
lname=Label(root,text="LAST NAME",fg='black',font='arial').grid(row=3,column=0)
email=Label(root,text="EMAIL",fg='black',font='arial').grid(row=4,column=0)
city=Label(root,text="CITY",fg='black',font='arial').grid(row=5,column=0)
pincode=Label(root,text="PINCODE",fg='black',font='arial').grid(row=6,column=0)
dob=Label(root,text="Date Of Birth",fg='black',font='arial').grid(row=7,column=0)
gender=Label(root,text="GENDER(M/F)",fg='black',font='arial').grid(row=8,column=0)
address=Label(root,text="ADDRESS",fg='black',font='arial').grid(row=9,column=0)


e1=Entry(root,width=40)
e1.grid(row=2,column=3)
e2=Entry(root,width=40)
e2.grid(row=3,column=3)
# e3=Entry(root,width=40)
# e3.grid(row=3,column=3)
e4=Entry(root,width=40)
e4.grid(row=4,column=3)
e5=Entry(root,width=40)
e5.grid(row=5,column=3)
e6=Entry(root,width=40)
e6.grid(row=6,column=3)
e7=Entry(root,width=40)
e7.grid(row=7,column=3)
e8=Entry(root,width=4)
e8.grid(row=8,column=3)
e9=Entry(root,width=40)
e9.grid(row=9,column=3)
btn=Button(root,text="Submit detail",command=submit_button).grid(row=12,column=1)
root.mainloop()

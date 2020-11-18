#fetch details only
import mysql.connector
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("PNR ENQUIRY")
root.geometry('700x570')
my_connect = mysql.connector.connect(
    host="localhost",user="root",password="Ekansh@123",database="test2")
my_conn=my_connect.cursor()
#==============================================================================================>>>
my_img = ImageTk.PhotoImage(ImageTk.Image.open("images\\my-account.png"))
img=Label(image=my_img)
img.place(x= 130,y= 0)
global det
det=['FIRST NAME','LAST NAME','EMAIL','CITY','PINCODE','DOB','GENDER','ADDRESS']
##########################################33333
def fetch_detail():
    email=email_entry.get()
    #print('var1')
    my_conn.execute("select * from users where email='{}'".format(email))
    fetched_table =my_conn.fetchone()
    #print(fetched_table)
    rw=180
    for j in det:
        Label(root,text=j,font='orbitron',fg='black').grid(row=rw,column=1)
        rw+=1
    rw=180
    for i in fetched_table:
        #Label(root,text=j,font='orbitron').grid(row=rw,column=1)
        Label(root,text=i,font='orbitron',fg='red').grid(row=rw,column=2)
        rw+=1
    #my_str=set("output")
    # my_str.set()
    # e=Label(root,text=fetched_table).grid(row=40,column=13)
    #e=Entry(root,width=40,fg="blue")
    #e.grid(row=20,column=3)
    #e.insert(END,fetched_table)

    # for details in t:
    #     for j in range(len(train)):
    #         if (a == train[2]):
    #             if (b == train[3]):
    #                 e = Entry(root, width=40, fg="blue")
    #                 e.grid(row=i, column=j)
    #                 e.insert(END, train[j])
    #root.destroy()
def back():
    root.destroy()
    from ekanshDBMS.venv import AfterLoginSuccess
def update():
    root.destroy()
#==============================================================================================>>>
back=Button(root,text="Back",command=back,bg='yellow').grid(row=11,column=1)
email=Label(root,text="email",font='orbitron').grid(row=17,column=1)
email_entry=Entry(root,width=40)
email_entry.grid(row=17,column=2)
fetch=Button(root,text="FETCH",command=fetch_detail,bg='Green',borderwidth=10).grid(row=18,column=5)
#update=Button(root,text="UPDATE",command=update,bg='Green',borderwidth=10).grid(row=120,column=5)
#==============================================================================================>>>
#==============================================================================================>>>

#vertical spacing trick
dateLabel=Label(root,text="   ",font=('courier')).grid(row=0,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=1)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=2)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=3)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=4)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=5)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=6)

dateLabel=Label(root,text="   ",font=('courier')).grid(row=8,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=9,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=11,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=12,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=0)

#==============================================================================================>>>
root.mainloop()

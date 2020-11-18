#this page will book tickets for you and return pnr
import mysql.connector
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title("MY BOOKING INFO PAGE")
root.geometry('1000x570')
#========================================================================================>>
my_connect = mysql.connector.connect(
    host="localhost",user="root",password="Ekansh@123",database="test2")
my_conn=my_connect.cursor()
#========================================================================================>>
# def new_func():
#     my_conn.execute("select status from ticket_detail where train_no='{}' and class='{}'".format(train_no, Class))
#     a = my_conn.fetchone()
def booking():
    train_no=e1.get()
    Class=e2.get()
    doj=e3.get()
    if(train_no==''or Class==''or doj==''):
        messagebox.askretrycancel("Error","Fill All Details")
    # elif(Class!='AC1' or Class!='AC1' or Class!='SLP'):
    #     messagebox.askretrycancel("Error","Class Entry is Invalid")
    else:
        #print(train_no,Class,doj)
        # cursor = conn.cursor()
        my_conn.execute("select status from tbs where train_no='{}' and class='{}'".format(train_no,Class))
        a=my_conn.fetchone()
        status=str(a[0])
        #for i in a:
            #status=i
        #print(status)
        sql="insert into ticket_detail(doj,train_no,class,status) values(%s,%s,%s,%s)"
        values=(doj,train_no,Class,status)
        my_conn.execute(sql,values)
        my_connect.commit()
        messagebox.showinfo("seat booked", "SEAT HAS BEEN BOOKED")
        a=my_conn.getlastrowid()
        messagebox.askokcancel("NOTE CAREFULLY ","your pnr is "+str(a))
        #print(a)
        #new_func()

        # # print(a)


#========================================================================================>>
my_img = ImageTk.PhotoImage(ImageTk.Image.open("images\\MY-BOOKING-INFO.png"))
img=Label(image=my_img)
img.place(x= 130,y= 0)

#train_no=Label(root,text="Enter train no to seat")
book_seats=Label(root,text="BOOK SEATS--------",font=('calibri',18),fg='red').grid(row=6,column=1)
Label(root,text="ENTER TRAIN NO").grid(row=7,column=2)
Label(root,text="CLASS (AC1,AC2,SLP)").grid(row=8,column=2)
Label(root,text="ENTER DATE OF JOURNEY (dd/mm/yy)").grid(row=9,column=2)
#Label(root,text="ENTER NO OF TICKETS")
e1=Entry(root,width=10)
e1.grid(row=7,column=3)
e2=Entry(root,width=10)
e2.grid(row=8,column=3)
e3=Entry(root,width=20)
e3.grid(row=9,column=3)
#e4=Entry(root,width=5)
b1=Button(root,text="Book Seat",borderwidth=10,fg='blue',command=booking).grid(row=8,column=7)
#tickets=Label(root,text="Tickets",font=('calibri',18),fg='red').grid(row=11,column=1)

#==============================================================================================>>>

hori=Label(root,text="                ",font='calibri',fg='red').grid(row=0,column=0)
hori=Label(root,text="                ",font='calibri',fg='red').grid(row=1,column=0)
hori=Label(root,text="                ",font='calibri',fg='red').grid(row=2,column=0)
hori=Label(root,text="                ",font='calibri',fg='red').grid(row=3,column=0)
hori=Label(root,text="                ",font='calibri',fg='red').grid(row=4,column=0)

hori=Label(root,text="                ",font='calibri',fg='red').grid(row=5,column=0)
hori=Label(root,text="                ",font='calibri',fg='red').grid(row=6,column=0)
hori=Label(root,text="                ",font='calibri',fg='red').grid(row=7,column=0)
hori=Label(root,text="                ",font='calibri',fg='red').grid(row=8,column=0)
hori=Label(root,text="                ",font='calibri',fg='red').grid(row=9,column=0)
















root.mainloop()
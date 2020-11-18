#complete pnr check button functionality
import mysql.connector
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("PNR ENQUIRY")
root.geometry('1000x700')
my_connect = mysql.connector.connect(
    host="localhost",user="root",password="Ekansh@123",database="test2")
my_conn=my_connect.cursor()
#==============================================================================================>>>
my_img = ImageTk.PhotoImage(ImageTk.Image.open("images\\PNR-ENQUIRY.png"))
img=Label(image=my_img)
img.place(x= 150,y= 0)

##########################################33333
#==============================================================================================>>>
global heading
global j
heading=['PNR','date of journey','Train_no','class','status','train_name']
def check_pnr():
    pnr = pnr_e1.get()
    my_conn.execute("select ticket_detail.pnr,ticket_detail.doj,ticket_detail.train_no,ticket_detail.class,ticket_detail.status,train.train_name from ticket_detail LEFT JOIN train using(train_no) where pnr='{}'".format(pnr))
    a = my_conn.fetchall()
    j=0
    row1=20
    row2=19
    col1=2
    col2=3
    heading = ['PNR', 'date of journey', 'Train_no', 'class', 'status', 'train_name']
    for i in a:
        for k in i:
            Label(root,text=heading[j],font=('Arial',18),fg='red').grid(row=row2,column=col2)
            Label(root, text=k, font=('calibri', 18),fg='blue').grid(row=row1, column=col2)
            j+=1
            col2+=1
        row1 += 1
    # root.destroy()
def back():
    root.destroy()
    from ekanshDBMS.venv import AfterLoginSuccess

#==============================================================================================>>>#==============================================================================================>>>
pnr=Label(root,text="PNR NUMBER",fg='black').grid(row=15,column=4)
pnr_e1=Entry(root,width=20)
pnr_e1.grid(row=15,column=6)
check=Button(root,text="CHECK PNR STATUS",bg='red',fg='green',borderwidth=10,command=check_pnr).grid(row=15,column=8)
return_button=Button(root,text="Back",command=back,bg='cyan').grid(row=3,column=0)

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




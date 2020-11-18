#cancel ticket
#use canc table in database test2
import mysql.connector
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title("PNR ENQUIRY")
root.geometry('700x400')
my_connect = mysql.connector.connect(
    host="localhost",user="root",password="Ekansh@123",database="test2")
my_conn=my_connect.cursor()
#==============================================================================================>>>
my_img = ImageTk.PhotoImage(ImageTk.Image.open("images\\cancel_ticket.png"))
img=Label(image=my_img)
img.place(x= 150,y= 0)

##########################################33333
def confirm():
    pnr=e1.get()
    my_conn.execute("update ticket_detail set status='canc' where pnr='{}'".format(pnr))
    #a = my_conn.fetchall()
    my_connect.commit()
    messagebox.showinfo("canceled","ticket has been canceled")
#==============================================================================================>>>
enter_pnr=Label(root,text="ENTER PNR",font="arial").grid(row=15,column=2)
e1=Entry(root,width=20)
e1.grid(row=15,column=4)
b1=Button(root,text="Cancel Ticket",borderwidth=10,bg='red',command=confirm).grid(row=17,column=3)
# enter_email=(root,text="")

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




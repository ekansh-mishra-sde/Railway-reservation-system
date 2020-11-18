#fetch details only
import mysql.connector
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("PNR ENQUIRY")
root.geometry('700x400')
my_connect = mysql.connector.connect(
    host="localhost",user="root",password="Ekansh@123",database="test2")
my_conn=my_connect.cursor()
#==============================================================================================>>>

# i = 20
# for train in my_conn:
#     for j in range(len(train)):
#         if (a == train[2]):
#             if (b == train[3]):
#                 e = Entry(root, width=40, fg="blue")
#                 e.grid(row=i, column=j)
#                 e.insert(END, train[j])
#     i = i + 1
# i = 20
#==============================================================================================>>>
my_img = ImageTk.PhotoImage(ImageTk.Image.open("images\\rail-money.png"))
img=Label(image=my_img)
img.place(x= 150,y= 0)

##########################################33333
def fetch_detail():
    fetch_money = Label(root, text="----Your Rail Account has rs", font=('orbitron', 18), fg='blue').grid(row=18,column=1)
    username1=entry1.get()
    my_conn.execute("select balance from money where user_name='{}'".format(username1))
    a=my_conn.fetchall()
    for i in a:
        Label(root,text=i,font=('Orbitron',18)).grid(row=18,column=2)
    #root.destroy()
def back():
    root.destroy()
    from ekanshDBMS.venv import AfterLoginSuccess
#==============================================================================================>>>
back=Button(root,text="Back",command=back,bg='yellow').grid(row=14,column=1)

#==============================================================================================>>>
name=Label(root,text="please re enter username",font=('calibri',12),fg='green').grid(row=16,column=0)
entry1=Entry(root,width=20)
entry1.grid(row=16,column=1)
button=Button(root,text="Fetch my details",borderwidth=10,bg='cyan',fg='red',command=fetch_detail).grid(row=16,column=2)

#==============================================================================================>>>

#vertical spacing trick
dateLabel=Label(root,text="    ",font=('courier')).grid(row=0,column=0)
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

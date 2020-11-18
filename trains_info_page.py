# it will import on basis of train source
# add more trains data
from tkinter import *
import mysql.connector as sq
from PIL import ImageTk,Image
root=Tk()
root.title("Trains Info Page")
root.geometry('1900x1900')
#============================================================>
global station_name,station_id
station_name=[]
station_id = []
#==========================================================>
conn = sq.connect(host="localhost",user="root",password="Ekansh@123",database="test2",auth_plugin='mysql_native_password')
#print(conn)
cursor = conn.cursor()
c=cursor.execute("select * from station")
items = cursor.fetchall()
for i,j in items:
    station_name.append(j)
    station_id.append(i)
#print(station_id)
#==========================================================>
#============================================================>
#add mysql and other options here
t=cursor.execute("select * from train")
fetched_table= cursor.fetchall()
#==========================================================>
#============================================================>
#functions
global column
column=["TRAIN NO","TRAIN NAME","SOURCE STATION","DESTINATION STATION","ACTIVE DAYS"]
def label_writer():
    rw=19
    col=0
    for i in column:
        e = Entry(root,width=40,fg='red')
        e.grid(row=rw,column=col)
        e.insert(END,i)
        col+=1
    return
def search_train_fun():
    print_records = ''
    a=clicked1.get()
    b=clicked2.get()
    my_conn=conn.cursor()
    if(a!=b):
        my_conn.execute("select * from train")
        i = 20
        for train in my_conn:
            for j in range(len(train)):
                if(a==train[2]):
                    if(b==train[3]):
                        e = Entry(root, width=40, fg="blue")
                        e.grid(row=i, column=j)
                        e.insert(END, train[j])
            i = i + 1
        i=20
                #print(train[2],end=" ")
                #print(train[3])

def back_button():
    root.destroy()
    from ekanshDBMS.venv import AfterLoginSuccess
#============================================================>
#heading for the window
img=PhotoImage(file="images\\PLAN-YOUR-JOURNEY.png")
l2 = Label(root,image= img,bg='#044A8F')
l2.place(x=300,y=6)
label_writer()
#Label(root,text='                                                                                      ').grid(row=0,column=0)
#heading=Label(root,text='Trains Detail',font=('Orbitron',25),fg='red').grid(row=0,column=1)
#=============================================================>
# dropdown1
clicked1 = StringVar()
clicked1.set(station_name[0])
subheading1=Label(root,text="Source Station",font="courier ",fg='blue',borderwidth=10).grid(row=5,column=0)
drop1 = OptionMenu(root,clicked1,*station_name)
drop1.grid(row=6,column=0)
#=============================================================>
# dropdown2
clicked2 = StringVar()
clicked2.set(station_name[1])
subheading2=Label(root,text="Destination Station",font="courier ",fg='blue',borderwidth=10).grid(row=5,column=42)
drop2 = OptionMenu(root,clicked2,*station_name)
drop2.grid(row=6,column=42)
#==========================================================>
# select date.moth.year
# dateLabel1=Label(root,text="Enter Date",font=('courier'),fg='blue').grid(row=5,column=0)
# dateText1=Entry(root,width=10)
# dateText1.grid(row=5,column=1)
# dateLabel2=Label(root,text="Enter Month",font=('courier'),fg='blue').grid(row=6,column=0)
# dateText2=Entry(root,width=10)
# dateText2.grid(row=6,column=1)
# dateLabel3=Label(root,text="Enter Year(optional)",font=('courier'),fg='blue').grid(row=7,column=0)
# dateText3=Entry(root,width=10)
# dateText3.grid(row=7,column=1)
#==========================================================>
# go button
search_train= Button(root,text="Search Train",bg='pink',fg='green',command=search_train_fun,borderwidth=10).grid(row=10,column=2)
#==========================================================>
# if possible add background photo
#my_img = ImageTk.PhotoImage(Image.open("codemy.ico"))

#==========================================================>
#back button
back=Button(root,text="Back to Homescreen",command=back_button,fg='red',bg='cyan',borderwidth=10,anchor=S).grid(row=400,column=1)
#==========================================================>
#labels for trains bw stations row=1
#==========================================================>
#vertical spacing trick
dateLabel=Label(root,text="   ",font=('courier')).grid(row=0,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=11,column=1)
# dateLabel=Label(root,text="   ",font=('courier')).grid(row=2,column=2)
# dateLabel=Label(root,text="   ",font=('courier')).grid(row=3,column=3)
# dateLabel=Label(root,text="   ",font=('courier')).grid(row=3,column=4)

dateLabel=Label(root,text="   ",font=('courier')).grid(row=3,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=4,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=8,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=9,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=11,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=12,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=0)
#==========================================================>
#==========================================================>
#==========================================================>
root.mainloop()
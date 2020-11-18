#creates login page layout.. first window to be shown but it doesnot validates users
#it has been imported in package.py to validate and do other stuffs like signup and reset
from tkinter import *
root = Tk()
#root.iconbitmap('codemy.ico')
root.title("LOGIN FOR USERS")
Label(root,text="LOGIN PAGE",font=('Orbitron',18),fg='Navy blue').grid(row=1,column=1)
root.geometry('450x200')

def get_button():
    global username
    global password
    username= e1.get()
    password = e2.get()
    root.destroy()
    # l1=Label(root,text=e1.get()+" hello "+e2.get()).grid(row=15,column=1)
    # #l1.pack()

def get_button1():
    root.destroy()
    from ekanshDBMS.venv import ResetButtonPage
    #reset btton

def get_button2():
    root.destroy()
    from ekanshDBMS.venv import signupWindow
    #signupwindow

def get_button3():
    root.destroy()
    from ekanshDBMS.venv import adminstrative_page
    #admin page

#e1=Entry(root)
username=Label(root,text="USERNAME").grid(row=2,column=0)
password=Label(root,text="PASSWORD").grid(row=3,column=0)
e1=Entry(root,width=20)
e1.grid(row=2,column=3)
e2=Entry(root,width=20,show="*")
e2.grid(row=3,column=3)
b1=Button(root,text="Submit",bg='light pink',fg='white',command=get_button,highlightthickness=6,borderwidth=10).grid(row=12,column=1)
b2=Button(root,text="Reset",command=get_button1,highlightthickness=1,borderwidth=10,bg='red').grid(row=13,column=0)
b3=Button(root,text="SignUp",command=get_button2,highlightthickness=1,borderwidth=10,bg='green').grid(row=13,column=3)
#b3=Button(root,text="Admin",command=get_button3,highlightthickness=1,borderwidth=10,bg='cyan').grid(row=13,column=2)
root.mainloop()

#
# entryBox = Entry(root, width=60)
# entryBox.grid(row=2, column=1, sticky=W)


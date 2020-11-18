from PIL import ImageTk,Image
from tkinter import *
root=Tk()
root.title('MAIN OPTION MENU')
root.geometry('1800x1800')
#================================================================================>>
#define functions over here
def plan_my_journey():
    root.destroy()
    from ekanshDBMS.venv import trains_info_page
def cancel():
    root.destroy()
def mybookings():
    root.destroy()
    from ekanshDBMS.venv import myBooking
def cancel_ticket():
    root.destroy()
    from ekanshDBMS.venv import cancel_ticket
def pnr_checker():
    root.destroy()
    from ekanshDBMS.venv import pnrEnquiry
def railmoney():
    root.destroy()
    from ekanshDBMS.venv import railmoney
def myaccount():
    root.destroy()
    from ekanshDBMS.venv import my_account
#================================================================================>>
# load = Image.open("images\\bg.jpg")#mage.open('images\\bg.jpg')
# render = ImageTk.PhotoImage(load)
# img = Label(root,image = render)
my_img = ImageTk.PhotoImage(ImageTk.Image.open("images\\bg1.jpg"))
img=Label(image=my_img)
img.place(x= 0,y= 0)
#================================================================================>>
img=PhotoImage(file="images\\Welcome-to-SwiftRail.png")
l2 = Label(root,image= img,bg='#044A8F')
l2.place(x=300,y=68)
#================================================================================>>
#button 1 down
img1=PhotoImage(file="images\\planyourjourney.png")
b1=Button(root,image=img1,command=plan_my_journey,bd=0,bg='#224D59')
b1.place(x=250,y=230)
#button 2 down
img2=PhotoImage(file="images\\mybooking.png")
b2=Button(root,image=img2,command=mybookings,bd=0,bg='#09384B')
b2.place(x=250,y=350)
#button3
img3=PhotoImage(file="images\\myaccount.png")
b3=Button(root,image=img3,bd=0,command=myaccount,bg='#71A3BC',activebackground='#3F7EA6')
b3.place(x=250,y=470)
#button4
img4=PhotoImage(file="images\\pnr.png")
b4=Button(root,image=img4,command=pnr_checker,bd=0,bg='#256C9C')
b4.place(x=950,y=230)
#button5
img5=PhotoImage(file="images\\railmoney.png")
b5=Button(root,image=img5,command=railmoney,bd=0,bg='#126699')
b5.place(x=950,y=350)
#button6
img6=PhotoImage(file="images\\cancel.png")
b6=Button(root,image=img6,bd=0,command=cancel_ticket,bg='#589DD8')
b6.place(x=950,y=470)
#button7
img7=PhotoImage(file="images\\exit.png")
b7=Button(root,image=img7,bd=0,command=cancel,bg='#3D7AB2')
b7.place(x=675,y=630)
#=================================================================================================>>
root.mainloop()
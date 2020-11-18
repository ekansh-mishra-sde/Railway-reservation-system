
import mysql.connector
from tkinter import *
root=Tk()
root.geometry('1700x1200')
my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ekansh@123",
    database="test2"
)
my_conn=my_connect.cursor()

root.mainloop()
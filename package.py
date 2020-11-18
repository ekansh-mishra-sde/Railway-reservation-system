#run this package First...it call trail module whose signup button calls signup page and generaUsernamePassword
#submit button will be calling new page full of options to do like irctc
#
from ekanshDBMS import trial
from tkinter import messagebox
import mysql.connector as sq
#====================================================================>
conn = sq.connect(host="localhost",user="root",password="Ekansh@123",database="test2",auth_plugin='mysql_native_password')
# catch(ModuleNotFoundError):
#     print("Handeled")
#=====================================================================>
def login_in(username,password):
    cursor = conn.cursor()
    cursor.execute("select * from username where username='{}'".format(username))
    items = cursor.fetchall()
    for nm,pasd,email in items:
        nm=str(nm)
        pasd=str(pasd)
        # print(type(pasd))
        if(nm==username and pasd == password):
            from ekanshDBMS.venv import AfterLoginSuccess
            #messagebox.showinfo("Success","Successful Login To YOUR ACCOUNT")
            #trial.root.destroy()
            #messagebox.showinfo("success", "All Done..Now Login")
        else:
            m2 = messagebox.askokcancel("failure", "Try Again")
            #trial.root.mainloop()

# c=login_in(trial.username,trial.password)
# print(c)
conn.commit()
conn.close
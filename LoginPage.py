from tkinter import *
#import sqlite3
from connectSRX.ssh_firewall_SRX_threads import exportConfig_SRX

hostIP_SRX = ['172.30.66.11', '172.31.66.11', '172.30.66.13', '172.31.66.13']
hostName_SRX = ['DC6_PUB_C01', 'DC7_PUB_C01', 'DC6_PUB_E01', 'DC7_PUB_E01']


root = Tk()
root.title("Login Firewall Device")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


USERNAME = StringVar()
PASSWORD = StringVar()
class Login:
    def Login(event=None):
        #Database()
        #print(hostIP)
        #print(hostName)
        #print(str(USERNAME.get()))
        #print(str(PASSWORD.get()))
        #exportConfig_SSG(hostIP_SSG, hostName_SSG, str(USERNAME.get()), str(PASSWORD.get()))
        exportConfig_SRX(hostIP_SRX, hostName_SRX, str(USERNAME.get()), str(PASSWORD.get()))
        
        quit()
    #==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
 
#==============================LABELS=========================================
lbl_title = Label(Top, text = "Login Firewall Device", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)
 
#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
 
#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login.Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)
    
        




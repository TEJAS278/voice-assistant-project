from tkinter import *
from tkinter import filedialog,messagebox
import mysql.connector
import sqlite3
import os
mydb=mysql.connector.connect(host="localhost",user="root",password="tejas278",database="photo",auth_plugin='mysql_native_password')
cursor=mydb.cursor()
con=sqlite3.connect('D:\\python_code\\project\\python project main\\test\\data1.db')
print('connected...')
cursor=mydb.cursor()

def savedata():
    fn=filedialog.askopenfilename(title="Select file",filetypes=(("Image file","*.jpg"),("All files","*.*")))
    with open(fn, "rb") as f:
        data=f.read()
    sql="INSERT into files(id,file_data,date) values(NULL, %s, NOW())"
    cursor.execute(sql, (data,))
    mydb.commit()
    messagebox.showinfo("Success", "Your file has been saved")
    cursor.close()


def readdata():
    fn=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Select file",filetypes=(("Image file","*.jpg"),("All files","*.*")))
    sql="select file_data from files limit 1"
    cursor.execute(sql)
    r=cursor.fetchall()
    for i in r:
        data=i[0]
    with open(fn, "wb") as f:
        f.write(data)
    f.close()
    messagebox.showinfo("Success", "Your file has been saved")








win=Tk()




Button(win,text="save to database",command=savedata).pack()
Button(win,text="read to database",command=readdata).pack()

win.config(background="Red")
win.geometry("300x300")
win.iconbitmap(r'D:\python_code\project\python project main\main\eva1.ico')
win.title("data")
win.mainloop()
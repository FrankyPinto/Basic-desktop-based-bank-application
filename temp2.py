import tkinter as tk
import mysql.connector
from tkinter import messagebox

mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pyguidb"
        )
mycursor = mydb.cursor()

def create():
    win5=tk.Tk()
    win5.title("Create account frame")
    k=tk.Frame(win5)
    k.place(height=5000,width=5000)
    lab1=tk.Label(k, text="USER ID")
    lab1.place(x=10,y=10)
    ent1=tk.Entry(k)
    ent1.place(x=80,y=10,height=20,width=100)
    lab2=tk.Label(k, text="NAME")
    lab2.place(x=10,y=40)
    ent2=tk.Entry(k)
    ent2.place(x=80,y=40,height=20,width=100)
    lab3=tk.Label(k, text="POSITION")
    lab3.place(x=10,y=70)
    def procd():
        try:
            use=ent1.get()
            nam=ent2.get()
            pos=ent21.get()
            bal=int(ent4.get())
            pas=ent5.get()
            pos=pos.upper()
            if use=="" or nam=="" or pos=="" or bal=="" or pas=="":
                messagebox.showerror("ERROR","FILL IN ALL FIELDS")
            elif nam.isalpha()==False:
                messagebox.showerror("ERROR","NAME FIELD CAN CONTAIN CHARACYERS ONLY")
            elif bal<1000:
                messagebox.showerror("ERROR","MINIMUM BALANCE 1000 REQUIRED")
            elif len(pas)<8:
                messagebox.showerror("ERROR","PASSWORD MUST BE MINIMUM 8 CHARACTERS LONG")
            elif pos.isalpha()==False:
                messagebox.showerror("ERROR","POSITION FIELD CAN CONTAIN CHARACYERS ONLY")
            else:
                if (pos=="EMPLOYEE" or pos=="CUSTOMER"):
                    sql=f"select user_id from bapp where user_id='{use}'"
                    mycursor.execute(sql)
                    myresult=mycursor.fetchall()
                    if myresult==[]:
                        try:
                            sql = "INSERT INTO BAPP (USER_ID, FIRST_NAME, POSITION, PASSWORD, BALANCE) VALUES (%s, %s, %s, %s, %s)"
                            val= (f"{use}",f"{nam}",f"{pos}",f"{pas}",f"{bal}")
                            mycursor.execute(sql, val)
                            mydb.commit()
                            messagebox.showinfo("BANK","USER ID CREATED")
                        except:
                            messagebox.showerror("ERROR","OPERATION FAILED")
                    else:
                        messagebox.showerror("ERROR","USER ID ALREADY EXIST")
                else:
                    messagebox.showerror("ERROR","POSITION CAN BE EMPLOYEE OR CUSTOMER ONLY")
        except ValueError:
            messagebox.showerror("ERROR","BALANCE MUST BE INTEGER ONLY!")
    ent21=tk.Entry(k)
    ent21.place(x=80,y=70,height=20,width=100)
    lab4=tk.Label(k, text="BALANCE")
    lab4.place(x=10,y=100)
    ent4=tk.Entry(k)
    ent4.place(x=80,y=100,height=20,width=100)
    lab5=tk.Label(k, text="PASSWORD")
    lab5.place(x=10,y=130)
    ent5=tk.Entry(k)
    ent5.place(x=80,y=130,height=20,width=100)
    b1=tk.Button(k, text="PROCEED",command=procd)
    b1.place(x=40,y=160)
    def quit2():
        win5.destroy()
    b2=tk.Button(k, text="QUIT",command=quit2,fg='red')
    b2.place(x=110,y=160)
    win5.mainloop()    
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from temp2 import create

mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pyguidb"
        )
mycursor = mydb.cursor()


def customer(u):
    win2=tk.Tk()
    win2.title("Customer level frame")
    k=tk.Frame(win2)
    k.place(height=10000,width=2500)
    def credit():
        win3=tk.Tk()
        win3.title("Credit frame")
        k=tk.Frame(win3)
        k.place(height=2000,width=2000)
        lab2=tk.Label(k, text="AMOUNT")
        lab2.place(x=25,y=80)
        ent2=tk.Entry(k)
        ent2.place(x=80,y=80,height=20,width=100)
        def crtran():
            amt=ent2.get()
            if amt=="":
                messagebox.showerror("ERROR","ENTER AMOUNT")
            elif amt.isdigit()==False:
                messagebox.showerror("ERROR","AMOUNT MUST BE INTEGER ONLY")
            else:
                amt=int(amt)
                sql = f"UPDATE BAPP SET BALANCE = BALANCE+ {amt} WHERE USER_ID = '{u}'"
                mycursor.execute(sql)
                mydb.commit()
                messagebox.showinfo("INFO","CREDIT SUCCESSFUL")
        b1=tk.Button(k,text="PROCEED",command=crtran)
        b1.place(x=40,y=150)
        def quit1():
            win3.destroy()
        but2=tk.Button(k, text="QUIT", fg="red",command=quit1)
        but2.place(x=130,y=150)
        win3.mainloop()
    b1=tk.Button(k, text="CREDIT",command=credit)
    b1.place(x=50,y=5,height=20,width=100)
    def debit():
        win3=tk.Tk()
        win3.title("Debit frame")
        k=tk.Frame(win3)
        k.place(height=2000,width=2000)
        lab2=tk.Label(k, text="AMOUNT")
        lab2.place(x=25,y=80)
        ent2=tk.Entry(k)
        ent2.place(x=80,y=80,height=20,width=100)
        def debamt():
            amt2=ent2.get()
            if amt2=="":
                messagebox.showerror("ERROR","ENTER AMOUNT")
            elif amt2.isdigit()==False:
                messagebox.showerror("ERROR","AMOUNT MUST BE INTEGER ONLY")
            else:
                sql=f"SELECT BALANCE FROM BAPP WHERE USER_ID='{u}'"
                mycursor.execute(sql)
                myresult=mycursor.fetchall()
                amt2=int(amt2)
                print(myresult[0][0])
                if myresult[0][0]-amt2>1000:
                    sql=f"UPDATE BAPP SET BALANCE=BALANCE-{amt2} WHERE USER_ID='{u}'"
                    mycursor.execute(sql)
                    mydb.commit()
                    messagebox.showinfo("","Debit Succesful")
                else:
                    messagebox.showerror("Error","Insufficient Balance")
        b1=tk.Button(k, text="PROCEED",command=debamt)
        b1.place(x=40,y=150)
        def quit1():
            win3.destroy()
        but2=tk.Button(k, text="QUIT", fg="red",command=quit1)
        but2.place(x=130,y=150)
        win3.mainloop()
    b2=tk.Button(k, text="DEBIT",command=debit)
    b2.place(x=50,y=35,height=20,width=100)
    def updt():
        mf=tk.Tk()
        mf.title("Update frame")
        cf=tk.Frame(mf)
        cf.place(height=2000,width=2000)
        def upname():
            un=tk.Tk()
            un.title("Update Name")
            uname=tk.Frame(un)
            uname.place(height=2000,width=2000)
            lab1=tk.Label(uname, text="OLD NAME")
            lab1.place(x=10,y=10)
            ent1=tk.Entry(uname)
            ent1.place(x=80,y=10,width=100)
            lab2=tk.Label(uname, text="NEW NAME")
            lab2.place(x=10,y=40)
            ent2=tk.Entry(uname)
            ent2.place(x=80,y=40,width=100)
            def validate2():
                oname=ent1.get()
                nname=ent2.get()
                if nname=="":
                    messagebox.showerror("ERROR","ENTER NEW NAME")
                elif nname.isalpha()==False:
                    messagebox.showerror("ERROR","NEW NAME MUST BE CHARACTER ONLY")
                else:
                    sql=f"SELECT FIRST_NAME FROM BAPP WHERE FIRST_NAME='{oname}' AND USER_ID='{u}'"
                    mycursor.execute(sql)
                    myresult=mycursor.fetchall()
                    try:
                        if myresult[0][0]==oname:
                            sql=f"UPDATE BAPP SET FIRST_NAME='{nname}' WHERE FIRST_NAME='{oname}' AND USER_ID='{u}'"
                            mycursor.execute(sql)
                            mydb.commit()
                            messagebox.showinfo("Bank","UPDATION SUCCESSFUL")
                        else:
                            messagebox.showerror("Bank","ENTER OLD NAME CORRECTLY")
                    except:
                        messagebox.showerror("ERROR","NAME DOES NOT EXIST!")
            but7=tk.Button(uname, text="PROCEED",command=validate2)
            but7.place(x=40,y=80)
            def quit05():
                un.destroy()
            but2=tk.Button(uname, text="QUIT",fg="red",command=quit05)
            but2.place(x=120,y=80)
            un.mainloop()
        but1=tk.Button(cf, text="UPDATE NAME",command=upname)
        but1.place(x=50,y=40)
        def uppasswd():
            up=tk.Tk()
            up.title("Update Password")
            upass=tk.Frame(up)
            upass.place(height=2000,width=2000)
            lab81=tk.Label(upass, text="OLD PASS")
            lab81.place(x=10,y=10)
            ent81=tk.Entry(upass)
            ent81.place(x=80,y=10,width=100)
            lab91=tk.Label(upass, text="NEW PASS")
            lab91.place(x=10,y=40)
            ent91=tk.Entry(upass)
            ent91.place(x=80,y=40,width=100)
            def validate1():
                opass=ent81.get()
                npass=ent91.get()
                if len(npass)<8:
                    messagebox.showerror("ERROR","PASSWORD MUST BE MINIMUM 8 CHARACTERS LONG")
                else:
                    sql=f"SELECT PASSWORD FROM BAPP WHERE PASSWORD='{opass}' AND USER_ID='{u}'"
                    mycursor.execute(sql)
                    myresult=mycursor.fetchall()
                    try:
                        if myresult[0][0]==opass:
                            sql=f"UPDATE BAPP SET PASSWORD='{npass}' WHERE PASSWORD='{opass}' AND USER_ID='{u}'"
                            mycursor.execute(sql)
                            mydb.commit()
                            messagebox.showinfo("Bank","UPDATION SUCCESSFUL")
                    except:
                        messagebox.showerror("ERROR","PASSWORD INCORRECT!")
            but2=tk.Button(upass, text="PROCEED",command=validate1)
            but2.place(x=40,y=80)
            def quit66():
                up.destroy()
            but2=tk.Button(upass, text="QUIT",fg="red",command=quit66)
            but2.place(x=120,y=80)
            up.mainloop()
        but1=tk.Button(cf, text="UPDATE PASSWORD",command=uppasswd)
        but1.place(x=35,y=80)
        def quit06():
            mf.destroy()
        but2=tk.Button(cf, text="QUIT",fg="red",command=quit06)
        but2.place(x=75,y=120)
        mf.mainloop()
    b4=tk.Button(k, text="UPDATE",command=updt)
    b4.place(x=50,y=65,height=20,width=100)
    def infodet():
        info = tk.Tk()
        info.title("YOUR DETAILS")
        k=tk.Frame(info)
        k.place(height= 70000, width= 10000)
        lab1=tk.Label(k,text="USER ID")
        lab1.place(x=37,y=10)
        lab2=tk.Label(k,text=u)
        lab2.place(x=120,y=10)
        lab3=tk.Label(k,text="PASSWORD")
        lab3.place(x=28,y=50)
        sql=f"SELECT PASSWORD from BAPP WHERE USER_ID='{u}'"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        lab9=tk.Label(k,text=myresult)
        lab9.place(x=120,y=50)
        sql=f"SELECT FIRST_NAME from BAPP WHERE USER_ID='{u}'"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        lab5=tk.Label(k,text="NAME")
        lab5.place(x=40,y=90)
        lab6=tk.Label(k,text= myresult[0][0])
        lab6.place(x=120,y=90)
        lab7=tk.Label(k,text="BALANCE")
        lab7.place(x=32,y=130)
        sql=f"SELECT BALANCE from BAPP WHERE USER_ID='{u}'"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        lab8=tk.Label(k,text=myresult)
        lab8.place(x=120,y=130)
        def quit3():
            info.destroy()
        d1=tk.Button(info,text="BACK",command=quit3)
        d1.place(x=75,y=160,height=25,width=50)
        info.mainloop()
    b3=tk.Button(k, text="VIEW INFO",command=infodet)
    b3.place(x=50,y=95,height=20,width=100)
    def transfer():
        win4=tk.Tk()
        win4.title("Transfer frame")
        k=tk.Frame(win4)
        k.place(height=2000,width=2000)
        lab1=tk.Label(k, text="USER ID")
        lab1.place(x=25,y=50)
        ent1=tk.Entry(k)
        ent1.place(x=80,y=50,height=20,width=100)
        lab2=tk.Label(k, text="AMOUNT")
        lab2.place(x=25,y=80)
        ent2=tk.Entry(k)
        ent2.place(x=80,y=80,height=20,width=100)
        def trans():
            amt3=ent2.get()
            ud=ent1.get()
            if ud=="":
                messagebox.showerror("ERROR","ENTER USERID")
            elif ud!="":
                sql=f"SELECT user_id FROM BAPP WHERE USER_ID='{ud}'"
                mycursor.execute(sql)
                myresult=mycursor.fetchall()
                try:
                    if myresult[0]=="":
                        messagebox.showerror("ERROR","ENTER USERID")
                    else:
                        try:
                            sql=f"SELECT BALANCE FROM BAPP WHERE USER_ID='{u}'"
                            mycursor.execute(sql)
                            myresult=mycursor.fetchall()
                            amt3=int(amt3)
                            if myresult[0][0]-amt3>1000:
                                sql=f"UPDATE BAPP SET BALANCE=BALANCE-{amt3} WHERE USER_ID='{u}'"
                                mycursor.execute(sql)
                                mydb.commit()
                                sql=f"UPDATE BAPP SET BALANCE=BALANCE+{amt3} WHERE USER_ID='{ud}'"
                                mycursor.execute(sql)
                                mydb.commit()
                                messagebox.showinfo("BANK","Transfer Succesful")
                            else:
                                messagebox.showerror("Error","Insufficient Balance")
                        except ValueError:
                            messagebox.showerror("ERROR","ENTER AMOUNT")
                        except:
                            messagebox.showerror("ERROR","USER DOESNT EXIST")
                except:
                    messagebox.showerror("ERROR","USER DOESNT EXIST")
        b1=tk.Button(k, text="PROCEED",command=trans)
        b1.place(x=30,y=120)
        def quit04():
            win4.destroy()
        b2=tk.Button(k, text="QUIT",fg="red",command=quit04)
        b2.place(x=100,y=120)
        win4.mainloop()
    b4=tk.Button(k, text="TRANSFER",command=transfer)
    b4.place(x=50,y=125,height=20,width=100)
    def quit02():
        win2.destroy()
    b5=tk.Button(k, text="QUIT",fg="red",command=quit02)
    b5.place(x=50,y=155,height=20,width=100)
    win2.mainloop()
 
def EMPLOYEE():
    win2=tk.Tk()
    win2.title("EMPLOYEE level frame")
    k=tk.Frame(win2)
    k.place(height=2000,width=2000)
    b1=tk.Button(k, text="CREATE",command=create)
    b1.place(x=50,y=50,height=30,width=100)
    stmt = "SHOW TABLES LIKE 'BAPP'"
    mycursor.execute(stmt)
    result=mycursor.fetchone()
    if result:
        print()
    else:
        mycursor.execute ( "CREATE TABLE BAPP (USER_ID VARCHAR(10) NOT NULL, FIRST_NAME VARCHAR(20) NOT NULL, POSITION VARCHAR(20), PASSWORD VARCHAR(10), BALANCE FLOAT)")
    def quit2():
        win2.destroy()
    b4=tk.Button(k, text="QUIT",command=quit2,fg='red')
    b4.place(x=80,y=150)
    win2.mainloop()

#MAINFRAME
mframe=tk.Tk()
mframe.title("Main GUI Frame")
coolFrame=tk.Frame(mframe)
coolFrame.place(height=2000,width=2000)
lab1=tk.Label(coolFrame, text="USER ID")
lab1.place(x=10,y=10)
ent1=tk.Entry(coolFrame)
ent1.place(x=80,y=10,width=100)
lab2=tk.Label(coolFrame, text="PASSWORD")
lab2.place(x=10,y=50)
ent2=tk.Entry(coolFrame, show="*")
ent2.place(x=80,y=50,width=100)
def getinput():
    try:
        uid=ent1.get()
        paswd=ent2.get()
        sql= f"SELECT POSITION FROM BAPP WHERE USER_ID='{uid}' AND PASSWORD='{paswd}'"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        for x in myresult:
            print()
        if x[0]=='EMPLOYEE':
            mag=EMPLOYEE()
        elif x[0]=='CUSTOMER':
            customer(uid)
    except:
        messagebox.showerror("Error","Please try again")
but1=tk.Button(coolFrame, text="SUBMIT",command=getinput)
but1.place(x=50,y=90)
def quit01():
    mframe.destroy()
but2=tk.Button(coolFrame, text="QUIT", fg="red",command=quit01)
but2.place(x=120,y=90)
mframe.mainloop()
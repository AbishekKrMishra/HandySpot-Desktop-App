from tkinter import*
from tkinter import messagebox
import pymysql
root=Tk()
class signup:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x550+150+50")
        self.root.title("SIGN-UP")
        self.root.resizable(False,False)
        self.root.config(bg="#81D4FA")

        f1=Frame(self.root,bg="#1565C0")
        f1.place(x=100,y=75,width=400,height=400)

        f2=Frame(self.root,bg="white")
        f2.place(x=500,y=75,width=400,height=400)

        name = Label(self.root, text="HandySpot", bd=0, bg="#81D4FA", fg="#4C4646",
                     font=("times new roman", 38, "bold")).place(x=380, y=10)

        title=Label(f1,text="INFORMATION",bd=0,bg="#1565C0",fg="white",font=("times new roman",16,"bold")).place(x=20,y=40)

        info=Label(f1,text="Handy tools assisting in a Handy Work.\nDesigned and Developed by:\nYaman Goyal and Abishek Kumar Mishra\nAmity University.",bd=0,bg="#1565C0",fg="white",font=("times new roman",12)).place(x=20,y=100,width=350)

        have_an_account=Button(f1,text="Have An Account",width=15,height=2,bd=0,fg="black",bg="white",font=("ariel",10,"bold"),cursor="hand2",command=self.login_window).place(x=20,y=300)

        register_lbl=Label(f2,text="REGISTRATION FORM",bd=0,bg="white",fg="#1565C0",font=("times new roman",16,"bold")).place(x=20,y=40)

        name_lbl=Label(f2,text="First Name\t\tLast Name",bd=0,bg="white",fg="black",font=("times new roman",12)).place(x=20,y=80)

        
        self.firstname_txt=Entry(f2,width=25,bd=3,relief=RIDGE,bg="lightgray")
        self.firstname_txt.place(x=20,y=100,height=30)

        self.lastname_txt=Entry(f2,width=25,bd=3,relief=RIDGE,bg="lightgray")
        self.lastname_txt.place(x=211,y=100,height=30)

        email_lbl=Label(f2,text="Your Email",bd=0,bg="white",fg="black",font=("times new roman",12)).place(x=20,y=150)

        
        self.email_txt=Entry(f2,width=57,bd=3,relief=RIDGE,bg="lightgray")
        self.email_txt.place(x=20,y=170,height=30)

        password_lbl=Label(f2,text="Password\t\t\tConfirm Password",bd=0,bg="white",fg="black",font=("times new roman",12)).place(x=20,y=220)

        self.password_txt=Entry(f2,width=22,bd=3,relief=RIDGE,show="*",font=("times new roman",10,"bold"),bg="lightgray")
        self.password_txt.place(x=20,y=240,height=30)

        self.confirm_password_txt=Entry(f2,width=22,bd=3,relief=RIDGE,show="*",font=("times new roman",10,"bold"),bg="lightgray")
        self.confirm_password_txt.place(x=211,y=240,height=30)

        register_btn=Button(f2,text="Register",width=15,height=2,bd=0,fg="white",bg="#1565C0",font=("ariel",10,"bold"),command=self.register_data,cursor="hand2").place(x=20,y=300)


    def clear(self):
        self.firstname_txt.delete(0,END)
        self.lastname_txt.delete(0,END)
        self.email_txt.delete(0,END)
        self.password_txt.delete(0,END)
        self.confirm_password_txt.delete(0,END)
    
    def login_window(self):
        self.root.destroy()
        import SIGNIN_PAGE

    def register_data(self):
        if self.firstname_txt.get()=="" or self.email_txt.get()=="" or self.password_txt.get()=="" or self.confirm_password_txt.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.password_txt.get()!=self.confirm_password_txt.get():
            messagebox.showerror("Error","Password and Confirm Password should be same.",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                c=con.cursor()
                c.execute("select * from people where email=%s",self.email_txt.get())
                col=c.fetchone()
                if col!=None:
                    messagebox.showerror("Error","User already exist,please use another emailid.",parent=self.root)
                else:
                    c.execute("insert into people (first_name,last_name,email,password) values(%s,%s,%s,%s)",
                    (self.firstname_txt.get(),
                    self.lastname_txt.get(),
                    self.email_txt.get(),
                    self.password_txt.get()
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","Registered Successfully",parent=self.root)
                    self.clear()
                    self.root.destroy()
                    import SIGNIN_PAGE
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)


sign_up=signup(root)
mainloop()

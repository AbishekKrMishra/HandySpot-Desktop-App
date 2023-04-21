from tkinter import*
from tkinter import messagebox
import pymysql
root=Tk()
class signin:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x550+150+50")
        self.root.title("SIGN-IN")
        self.root.resizable(False,False)
        self.root.config(bg="#BBDEFB")

        f1=Frame(self.root,bg="#5C6BC0")
        f1.place(x=100,y=75,width=400,height=400)

        f2=Frame(self.root,bg="white")
        f2.place(x=500,y=75,width=400,height=400)

        name = Label(self.root, text="HandySpot", bd=0,bg="#BBDEFB", fg="#4C4646",
                      font=("times new roman", 38, "bold")).place(x=380, y=10)

        title=Label(f1,text="INFORMATION",bd=0,bg="#5C6BC0",fg="white",font=("times new roman",18,"bold")).place(x=20,y=40)

        info=Label(f1,text="Handy tools assisting in a Handy Work.\nDesigned and Developed by:\nYaman Goyal and Abishek Kumar Mishra\nAmity University.",bd=0,bg="#5C6BC0",fg="white",font=("times new roman",12)).place(x=20,y=100,width=350)

        register_here=Button(f1,text="Register Now",width=15,height=2,bd=0,fg="black",bg="white",font=("ariel",10,"bold"),cursor="hand2",command=self.register_window).place(x=20,y=300)

        login_lbl=Label(f2,text="LOG-IN",bd=0,bg="white",fg="#5C6BC0",font=("times new roman",18,"bold")).place(x=20,y=40)

        email_lbl=Label(f2,text="Your Email",bd=0,bg="white",fg="black",font=("times new roman",14)).place(x=20,y=100)

        self.email_txt=Entry(f2,width=50,bd=3,relief=RIDGE,bg="lightgray")
        self.email_txt.place(x=20,y=130,height=30)

        password_lbl=Label(f2,text="Password",bd=0,bg="white",fg="black",font=("times new roman",14)).place(x=20,y=190)

        self.password_txt=Entry(f2,width=43,bd=3,relief=RIDGE,show="*",font=("times new roman",10,"bold"),bg="lightgray")
        self.password_txt.place(x=20,y=220,height=30)

        login_btn=Button(f2,text="Login",width=15,height=2,bd=0,fg="white",bg="#5C6BC0",font=("ariel",10,"bold"),cursor="hand2",command=self.login).place(x=20,y=300)

    def register_window(self):
        self.root.destroy()
        import SIGNUP_PAGE

    def login(self):
        if self.email_txt.get()=="" or self.password_txt.get()=="":
            messagebox.showerror("Error","All Fields are Required.",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                c=con.cursor()
                c.execute("select * from people where email=%s and password=%s",(self.email_txt.get(),self.password_txt.get()))
                col=c.fetchone()
                if col==None:
                    messagebox.showerror("Error","Invalid Username Or Password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import DASHBOARD
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

sign_in=signin(root)
mainloop()
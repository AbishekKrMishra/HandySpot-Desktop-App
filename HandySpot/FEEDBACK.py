from tkinter import*
from tkinter import messagebox
import pymysql
root=Tk()
class feedback:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x550+150+50")
        self.root.title("FEEDBACK")
        self.root.resizable(0,0)

        #---FRAMES---
        f1=Frame(self.root,bg="white")
        f1.place(x=0,y=0,relwidth=1,height=200)

        f2=Frame(self.root,bg="#1565C0")
        f2.place(x=0,y=180,relwidth=1,relheight=1)

        #---FRAME in f1---
        f1_1=Frame(f1,bg="#1565C0")
        f1_1.place(x=0,y=100,relwidth=1,height=80)

        #---FRAME in f2---
        f2_1=Frame(f2,bg="white")
        f2_1.place(x=100,y=0,width=800,height=300)


        #---WIDGITS in f1---
        title_lbl=Label(f1,text="Feedback",bg="white",fg="#1565C0",font=("times new roman",48,"bold"))
        title_lbl.place(x=290,y=10,width=400,height=60)

        #---WIDGITS in f1_1---
        f1_1_txt_lbl=Label(f1_1,text="Send us your feedback!",bg="#1565C0",fg="white",font=("times new roman",30,"bold"))
        f1_1_txt_lbl.place(x=110,y=0,width=780,relheight=1)

        #---WIDGITS in f2_1---
        self.feed_txt=Text(f2_1,bg="#FFFDE7",fg="black",font=("times new roman",16,"bold"))
        self.feed_txt.place(x=10,y=10,width=780,height=220)

        clr_btn=Button(f2_1,bg="#1565C0",fg="white",text="Clear",font=("times new roman",16,"bold"),activebackground="#1565C0",activeforeground="white",command=self.clear_btn)
        clr_btn.place(x=570,y=240,width=100,height=50)

        send_btn=Button(f2_1,bg="#1565C0",fg="white",text="Submit",font=("times new roman",16,"bold"),activebackground="#1565C0",activeforeground="white",command=self.submit_btn)
        send_btn.place(x=690,y=240,width=100,height=50)

        info_lbl=Label(f2,text="Developed by Yaman Goyal & Abishek Kumar Mishra",bg="#1565C0",fg="black",font=("calibri",11,"bold"))
        info_lbl.place(x=120,y=320,width=780,height=30)

       
    def clear_btn(self):
        self.feed_txt.delete(1.0,END)

    def submit_btn(self):
        #self.comment=self.feed_txt.get(1.0,END)
        if self.feed_txt.get(1.0,END)=="":
            messagebox.showerror("Error","Enter some feedback.",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                c=con.cursor()
                c.execute("insert into feeds (feedback) values(%s)",
                (
                    self.feed_txt.get(1.0,END)
                ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Feedback Submitted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)





feed=feedback(root)
mainloop()

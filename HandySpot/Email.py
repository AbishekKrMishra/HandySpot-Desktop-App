from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,filedialog
import os
import pandas as pd
import mailsfunction
import xlrd
import time
root = Tk()

class mul_mails:
    def __init__(self,root):
        self.root=root
        self.root.title("Mail Gateway")
        self.root.geometry("1000x550+150+50")
        self.root.resizable(False,False)
        self.root.config(bg="#0055E3")
        f1 = Frame(self.root, bg="white")
        f1.place(x=40, y=22, width=920, height=510)

        #------ICONS-----
        self.setting_icon = ImageTk.PhotoImage(file="images/setting.png")

        #---------TITLE----------

        title = Label(f1,text="Email Gateway",font=("Times New Roman",30,"bold"),bg="white",fg="#004ED0").place(x=30,y=27)

        line = Label(f1, text=" ", bg="yellow", anchor="w")
        line.place(x=0, y=85,width=350,height=3)

        #---------SETTING--------

        btn_icon = Button(f1, image=self.setting_icon, bd=0, bg="white",cursor="hand2",command=self.setting).place(x=845,y=25)


        #------OPTIONS--------
        self.var_choice = StringVar()
        single_btn = Radiobutton(f1, text="Single Mail", value="single", variable=self.var_choice,
                                 font=("Times new roman", 18, "bold"), bg="white", activebackground="white",command=self.singleORmultiple).place(x=30, y=120)
        multiple_btn = Radiobutton(f1, text="Multiple Mails", value="multiple", variable=self.var_choice,
                                   font=("Times new roman", 18, "bold"), bg="white",activebackground="white",command=self.singleORmultiple).place(x=300, y=120)
        self.var_choice.set("single")

        line2 = Label(f1, text=" ", bg="yellow", anchor="w")
        line2.place(x=0, y=185, width=80, height=3)

        # ------MAIL DETAILS------
        to = Label(f1, text="To:", font=("times new roman", 15), bg="white").place(x=30, y=230)
        sub = Label(f1, text="Subject:", font=("times new roman", 15), bg="white").place(x=30, y=280)
        message = Label(f1, text="Message:", font=("times new roman", 15), bg="white").place(x=30, y=330)

        self.txt_to = Entry(f1, font=("times new roman", 12), bg="#FEFFE9")
        self.txt_to.place(x=160, y=230, width=300, height=27)

        #--------DETAILS OF MULTIPLE FILES---------

        self.lbl_total = Label(f1, font=("times new roman", 14), bg="white",fg="black")
        self.lbl_total.place(x=600, y=227)
        self.lbl_sent = Label(f1, font=("times new roman", 12), bg="white", fg="black")
        self.lbl_sent.place(x=515,y=490)
        self.lbl_left = Label(f1, font=("times new roman", 12), bg="white", fg="black")
        self.lbl_left.place(x=585,y=490)
        self.lbl_failed = Label(f1, font=("times new roman", 12), bg="white", fg="black")
        self.lbl_failed.place(x=655,y=490)

        #---------BROWSE-----------

        self.btn_browse = Button(f1, text="Browse", command=self.browse_file,font=("Times new roman", 12, "bold"), bg="#0055E3", fg="white",
                           cursor="hand2",state=DISABLED)
        self.btn_browse.place(x=490, y=225, width=100)

        #-------------------------


        self.txt_sub = Entry(f1, font=("times new roman", 12), bg="#FEFFE9")
        self.txt_sub.place(x=160, y=280, width=432, height=27)

        self.txt_mesz = Text(f1, font=("times new roman", 12), bg="#FEFFE9")
        self.txt_mesz.place(x=160, y=330, width=550, height=100)

        #-------------CLEAR AND SEND-----------

        btn_clear = Button(f1, text="Clear",command=self.clear1, font=("Times new roman", 12, "bold"), bg="#0055E3", fg="white",cursor="hand2").place(x=480,y=447,width=100)
        btn_send = Button(f1,text="Send",command=self.send_mail,font=("Times new roman",12,"bold"), bg="#0055E3",fg="white",cursor="hand2").place(x=610, y=447,width=100)
        self.check_user_file()

        #----------------------------------------

    ###########----------BROWSE BUTTON------##########

    def browse_file(self):
        op=filedialog.askopenfile(initialdir='C:/Users/Yaman Goyal/PycharmProjects/Mycode/InternProjects',title="Select Recipients File",filetype=(("All Files","*.*"),("Excel Files",".xlsx")))
        if op!=None:
            data = pd.read_excel(op.name)
            if 'User Email' in data.columns:
                self.emails = list(data['User Email'])
                c = []
                for i in self.emails:
                    if pd.isnull(i) == False:
                        c.append(i)
                self.emails = c
                if len(self.emails)>0:
                    self.txt_to.config(state=NORMAL)
                    self.txt_to.delete(0,END)
                    self.txt_to.insert(0,str(op.name.split("/")[-1]))
                    self.txt_to.config(state='readonly')
                    self.lbl_total.config(text="Total IDs : "+str(len(self.emails)))
                    self.lbl_sent.config(text="Sent: ")
                    self.lbl_left.config(text="Left: ")
                    self.lbl_failed.config(text="Failed: ")



                else:
                    messagebox.showerror("Error","This file doesn't has Email IDs",parent=self.root)
            else:
                messagebox.showerror("Error","Please select a valid Recipient File",parent=self.root)

    ###########-------SEND BUTTON---------############
    def send_mail(self):
        x = len(self.txt_mesz.get('1.0',END))
        if self.txt_to.get()=="" or self.txt_sub.get()=="" or x==1:
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            if self.var_choice.get()=="single":
                status=mailsfunction.email_sender(self.txt_to.get(),self.txt_sub.get(),self.txt_mesz.get('1.0',END),self.from_,self.pass_)
                if status=="s":
                    messagebox.showinfo("Success", "Mail has been sent", parent=self.root)
                if status=="f":
                    messagebox.showerror("Failed", "Mail not sent, Try again", parent=self.root)
            if self.var_choice.get() == "multiple":
                self.failed=[]
                self.s_count=0
                self.f_count=0
                for x in self.emails:
                    status=mailsfunction.email_sender(x, self.txt_sub.get(), self.txt_mesz.get('1.0', END),self.from_, self.pass_)
                    if status=="s":
                        self.s_count+=1
                    if status=="f":
                        self.f_count+=1
                    self.mail_status()
                messagebox.showinfo("success", "Mail has been sent", parent=self.root)



    def mail_status(self):
        self.lbl_total.config(text="Status : " + str(len(self.emails)))
        self.lbl_sent.config(text="Sent: "+str(self.s_count))
        self.lbl_left.config(text="Left: "+str(len(self.emails)-(self.s_count+self.f_count)))
        self.lbl_failed.config(text="Failed: "+str(self.f_count))
        self.lbl_total.update()
        self.lbl_sent.update()
        self.lbl_left.update()
        self.lbl_failed.update()


    ###########-------OPTION BUTTONS---------############

    def singleORmultiple(self):
        if self.var_choice.get()=="single":
            self.btn_browse.config(state=DISABLED)
            self.txt_to.config(state=NORMAL)
            self.txt_to.delete(0,END)
            self.clear1()
        if self.var_choice.get()=="multiple":
            self.btn_browse.config(state=NORMAL)
            self.txt_to.delete(0, END)
            self.txt_to.config(state='readonly')

    ###########-------CLEAR BUTTON 1---------############

    def clear1(self):
        self.txt_to.config(state=NORMAL)
        self.txt_to.delete(0,END)
        self.txt_sub.delete(0, END)
        self.txt_mesz.delete('1.0', END)
        self.var_choice.set("single")
        self.btn_browse.config(state=DISABLED)
        self.lbl_total.config(text="")
        self.lbl_sent.config(text="")
        self.lbl_left.config(text="")
        self.lbl_failed.config(text="")


    ###########-------SETTING BUTTON---------############
    def setting(self):
        self.check_user_file()
        self.root2=Toplevel()
        self.root2.title("Settings")
        self.root2.geometry("550x300+390+150")
        self.root2.resizable(False,False)
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.config(bg="#0055E3")


        #-------TITLE------

        title_setting = Label(self.root2, text="Credentials Settings", font=("Times New Roman", 26, "bold"), bg="black", fg="white").place(x=0, y=0,width=550,height=88)
        line3 = Label(self.root2, text=" ", bg="yellow", anchor="w")
        line3.place(x=0, y=85, relwidth=1, height=3)

        #------FROM DETAILS-------

        from_ = Label(self.root2, text="Email ID:", font=("times new roman", 15), bg="#0055E3").place(x=30, y=130)
        pass_ = Label(self.root2, text="Password:", font=("times new roman", 15), bg="#0055E3").place(x=30, y=180)

        self.txt_from = Entry(self.root2, font=("times new roman", 12), bg="white")
        self.txt_from.place(x=160, y=130, width=300, height=27)

        self.txt_pass= Entry(self.root2, font=("times new roman", 12), bg="white",show="*")
        self.txt_pass.place(x=160, y=180, width=300, height=27)

        btn_clear2 = Button(self.root2, text="Clear",command=self.clear_setting, font=("Times new roman", 12, "bold"), bg="white", fg="#0055E3",
                           cursor="hand2").place(x=250, y=250, width=100)
        btn_save = Button(self.root2, text="Save",command=self.save_setting, font=("Times new roman", 12, "bold"), bg="white", fg="#0055E3",
                          cursor="hand2").place(x=360, y=250, width=100)
        self.txt_from.insert(0,self.from_)
        self.txt_pass.insert(0,self.pass_)

    def check_user_file(self):
        if os.path.exists("Sender_mail.txt")==False:
            f = open('Sender_mail.txt', 'w')
            f.write(",")
            f.close()
        f2=open("Sender_mail.txt")
        self.credentials=[]
        for i in f2:
            self.credentials.append([i.split(",")[0],i.split(",")[1]])
        self.from_=self.credentials[0][0]
        self.pass_=self.credentials[0][1]



    ###########-------SAVE SETTING BUTTON---------############

    def save_setting(self):
        if self.txt_from.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            f=open('Sender_mail.txt','w')
            f.write(self.txt_from.get()+","+self.txt_pass.get())
            f.close()
            messagebox.showinfo("Hey User", "Your mail ID has been saved as Sender mail.", parent=self.root2)
            self.check_user_file()

    ###########-------CLEAR SETTING BUTTON---------############
    def clear_setting(self):
        self.txt_from.delete(0,END)
        self.txt_pass.delete(0,END)

email = mul_mails(root)
mainloop()
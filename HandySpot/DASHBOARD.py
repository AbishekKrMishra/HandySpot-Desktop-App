from tkinter import*
import os
from PIL import ImageTk
root=Tk()
class dashboard:
    def  __init__(self,root):
        self.root=root
        self.root.title("DASHBOARD")
        self.root.geometry("1000x550+150+50")
        self.root.resizable(0,0)
        self.root.config(bg="white")

        #---Frames---
        f1=Frame(self.root,bg="white",bd=0)
        f1.place(x=10,y=10,width=980,height=120)

        f2 = Frame(self.root, bg="white", bd=0)
        f2.place(x=20, y=145, width=300, height=170)

        f3 = Frame(self.root, bg="white", bd=0)
        f3.place(x=350, y=145, width=300, height=170)

        f4 = Frame(self.root, bg="white", bd=0)
        f4.place(x=675, y=145, width=300, height=170)

        f5 = Frame(self.root, bg="white", bd=0)
        f5.place(x=20, y=340, width=300, height=170)

        f6 = Frame(self.root, bg="white", bd=0)
        f6.place(x=350, y=340, width=300, height=170)

        f7 = Frame(self.root, bg="white", bd=0)
        f7.place(x=675, y=340, width=300, height=170)


        #---TITLE---
        self.dashbord_img=PhotoImage(file="images/Dashboard.png")
        titlt_lbl=Label(f1,image=self.dashbord_img)
        titlt_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #-----Images---

        self.s2t_icon = ImageTk.PhotoImage(file="images/Speech2Text.png")
        self.t2s_icon = ImageTk.PhotoImage(file="images/Text2Speech.png")
        self.mgate_icon = ImageTk.PhotoImage(file="images/Mail Gateway.png")
        self.i2t_icon = ImageTk.PhotoImage(file="images/Image2Text.png")
        self.mp_icon = ImageTk.PhotoImage(file="images/Music Player.png")
        self.fb_icon = ImageTk.PhotoImage(file="images/Feedback.png")
        self.cal_icon = ImageTk.PhotoImage(file="images/cal.png")
        self.note_icon = ImageTk.PhotoImage(file="images/note.png")


        #----Buttons-----

        cal_btn = Button(self.root,image=self.cal_icon, bd=0, bg="white", cursor="hand2", activeforeground="red",
                                 activebackground="white",command=self.cal).place(x=646, y=310)
        note_btn = Button(self.root, image=self.note_icon, bd=0, bg="white", cursor="hand2", activeforeground="red",
                         activebackground="white", command=self.note).place(x=317, y=308)
        speech2text_btn = Button(f2,image=self.s2t_icon,bd=0, bg="white",cursor="hand2", activeforeground="red",activebackground="white",command=self.s2t).place(x=0,y=0)
        image2text_btn = Button(f3, image=self.i2t_icon, bd=0, bg="white", cursor="hand2", activebackground="white",command=self.i2t).place(x=0, y=0)
        mail_btn = Button(f4, image=self.mgate_icon, bd=0, bg="white", cursor="hand2", activebackground="white",command=self.mail).place(x=0, y=0)
        text2speech_btn = Button(f5, image=self.t2s_icon, bd=0, bg="white", cursor="hand2", activebackground="white",command=self.t2s).place(x=0, y=0)
        mp3_btn = Button(f6, image=self.mp_icon, bd=0, bg="white", cursor="hand2", activebackground="white",command=self.mp3).place(x=0, y=0)
        feedback_btn = Button(f7, image=self.fb_icon, bd=0, bg="white", cursor="hand2", activebackground="white",command=self.feed).place(x=0, y=0)

        #---Linking---

    def cal(self):
        self.filename0 = 'CALCULATOR.py'
        os.system(self.filename0)

    def note(self):
        self.filename01 = 'NOTEPAD.py'
        os.system(self.filename01)

    def s2t(self):
        self.filename = 'Speech2Text.py'
        os.system(self.filename)

    def t2s(self):
        self.filename2 = 'Text2Speech.py'
        os.system(self.filename2)

    def i2t(self):
        self.filename3 = 'IMAGE_TO_TEXT.py'
        os.system(self.filename3)

    def mail(self):
        self.filename4 = 'Email.py'
        os.system(self.filename4)

    def mp3(self):
        self.filename5 = 'mp3.py'
        os.system(self.filename5)

    def feed(self):
        self.filename6 = 'FEEDBACK.py'
        os.system(self.filename6)

dash=dashboard(root)
mainloop()
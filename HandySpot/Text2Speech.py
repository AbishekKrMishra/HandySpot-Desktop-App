from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile, asksaveasfilename
import pyttsx3
import pandas as pd
from PIL import ImageTk
root = Tk()

class txt2speech:
    def __init__(self,root):
        self.root=root
        self.root.title("Text-to-Speech")
        self.root.geometry("1000x550+150+50")
        self.root.resizable(False,False)
        self.root.config(bg="#0055E3")
        self.mic_on = ImageTk.PhotoImage(file="images/speak.png")

    #---------Frame-------

        f1 = Frame(self.root, bg="white")
        f1.place(x=50,y=140, width=900, height=360)

        # ------TITLE-------

        line = Label(self.root, text=" ", bg="yellow", anchor="w")
        line.place(x=52, y=67, width=893, height=5)

        title = Label(self.root, text="Text-to-Speech",font=("Times New Roman", 40, "bold"), bg="#0055E3", fg="white")
        title.place(x=90, y=33)

        line = Label(self.root, text=" ", bg="yellow", anchor="w")
        line.place(x=60, y=80, width=30, height=5)

        line = Label(self.root, text=" ", bg="yellow", anchor="w")
        line.place(x=438, y=80, width=490, height=5)

        #----------Design------

        self.btn1 = Button(f1, image=self.mic_on,command=self.talk, bd=0, bg="white", cursor="hand2", activebackground="white")
        self.btn1.place(x=620, y=140, width=100, height=100)

        title2 = Label(f1, text="Click down here to Convert", font=("Times New Roman", 15, "bold"), bg="white", fg="#0055E3")
        title2.place(x=560, y=80)

        line = Label(f1, text=" ", bg="#3F8DFF", anchor="w")
        line.place(x=522, y=180, width=100, height=5)

        line = Label(f1, text=" ", bg="#3F8DFF", anchor="w")
        line.place(x=450, y=190, width=170, height=5)

        line = Label(f1, text=" ", bg="#3F8DFF", anchor="w")
        line.place(x=522, y=200, width=100, height=5)

        line = Label(f1, text=" ", bg="#3F8DFF", anchor="w")
        line.place(x=718, y=180, width=100, height=5)

        line = Label(f1, text=" ", bg="#3F8DFF", anchor="w")
        line.place(x=720, y=190, width=180, height=5)

        line = Label(f1, text=" ", bg="#3F8DFF", anchor="w")
        line.place(x=718, y=200, width=100, height=5)


        #-----Browse File--------

        self.file = Text(f1, font=("times new roman", 12), bg="#FEFFF1",state=DISABLED)
        self.file.place(x=20, y=20, width=300, height=27)

        self.btn_browse = Button(f1, text="Browse", command=self.browse_file,font=("Times new roman", 12, "bold"),
                                 bg="#0055E3", fg="white",
                                 cursor="hand2")
        self.btn_browse.place(x=350, y=20, width=100, height=26)

        #------Text Area-------

        self.txt = Text(f1, font=("times new roman", 12), bg="#FEFFF1")
        self.txt.place(x=20, y=80, width=430, height=230)

        #--------Buttons--------

        btn_clear = Button(f1, text="Clear", command=self.clear,font=("Times new roman", 12, "bold"), bg="#0055E3",
                          fg="white", cursor="hand2").place(x=350, y=320, width=100)


    def clear(self):
        self.txt.delete('0.0',END)
        self.file.delete('0.0',END)

    def talk(self):
        engine = pyttsx3.init()
        engine.say(self.txt.get('0.0', END))
        engine.runAndWait()

    def browse_file(self):
        op = filedialog.askopenfile(initialdir='/',
                                    title="Select",
                                    filetype=(("All Files", "*.*"), ("Text Files", ".txt")))
        data = op.read()
        c = []
        c.append(data)
        self.txt2 = c
        if len(self.txt2) > 0:
            self.file.config(state=NORMAL)
            self.file.delete('1.0', END)
            self.file.insert('1.0', str(op.name.split("/")[-1]))
        self.txt.insert('1.0',data)


Txt2speech = txt2speech(root)
mainloop()
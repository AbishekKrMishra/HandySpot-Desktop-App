from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,filedialog
root = Tk()

running=True

class window:
    def __init__(self,root):
        self.root=root
        self.root.title("Speech 2 Text")
        self.root.geometry("1000x550+150+50")
        self.root.resizable(False,False)
        self.root.config(bg="#0055E3")


        #---TITLE----

        title = Label(self.root, text="Speech-to-Text", font=("Times New Roman", 30, "bold"), bg="#0055E3", fg="white")
        title.place(x=35, y=27)


        #--------Creating Frame-------

        f1 = Frame(self.root, bg="white")
        f1.place(x=40, y=100, width=920, height=360)

        #--------Inserting Images----

        self.mic_on = ImageTk.PhotoImage(file="images/mic2.png")
        self.mic_off = ImageTk.PhotoImage(file="images/mic3.png")

        #--------label-----

        title2 = Label(f1, text="Click to Convert", font=("Times New Roman", 15, "bold"), bg="white",
                       fg="#0055E3")
        title2.place(x=60, y=80)

        #-------Buttons------

        self.btn1 = Button(f1,image=self.mic_on,command=self.listen,bd=0, bg="white",cursor="hand2",activebackground="white").place(x=77,y=120,width=100,height=100)

        btn_clear = Button(f1, text="Clear", command=self.clear,font=("Times new roman", 12, "bold"), bg="#217CFF",
                          fg="white", cursor="hand2").place(x=810, y=30, width=100)
        btn_copy = Button(f1, text="Copy", command=self.copy,font=("Times new roman", 12, "bold"), bg="#217CFF",
                           fg="white", cursor="hand2").place(x=810, y=260, width=100)
        btn_save = Button(f1, text="Save",command=self.save, font=("Times new roman", 12, "bold"), bg="#217CFF",
                          fg="white", cursor="hand2").place(x=810, y=297, width=100)

        # -----Txt AREA------

        self.txt = Text(f1, font=("times new roman", 12), bg="#FEFFE9")
        self.txt.place(x=300, y=30, width=500, height=300)

    #----------Function Defination-------

    def clear(self):
        self.txt.delete('0.0',END)

    def copy(self):
        root.clipboard_clear()
        txt = self.txt.get('0.0', END)
        root.clipboard_append(txt)

    def save(self):
        files = [('All Files', '*.*'),
                 ('Text Files', '*txt')]
        save_text_as = filedialog.asksaveasfile(filetype=files,mode='w', defaultextension='.txt')
        if save_text_as:
            text_to_save = self.txt.get('1.0', END)
            save_text_as.write(text_to_save)
            save_text_as.close()
        else:
            messagebox.showinfo("Error", "Cancelled")


    def listen(self):
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio_text = r.listen(source)
            try:
                text = r.recognize_google(audio_text)+" "
                self.txt.insert(END,text)
            except:
                messagebox.showerror("Error","Could not hear you, Try Again.",parent=self.root)

S2T = window(root)
mainloop()
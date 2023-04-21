from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Users\Abhishek\AppData\Local\Tesseract-OCR\tesseract.exe'
root=Tk()
class image_to_text:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x550+150+50")
        self.root.title("IMAGE TO TEXT")
        self.root.resizable(0,0)
        self.root.config(bg="#1565C0")

        #Top Frame

        f1=Frame(self.root,bg="white",bd=2,relief=RAISED)
        f1.place(x=0,y=0,relwidth=1,height=80)

        title_lbl=Label(f1,text="Image-to-Text",bg="white",fg="#1565C0",font=("times new roman",40,"bold"))
        title_lbl.pack()

        #Frames

        f2=Frame(self.root,bg="white",bd=0,relief=RAISED)
        f2.place(x=10,y=90,width=480,height=50)


        f3=Frame(self.root,bg="skyblue",bd=0,relief=RAISED)
        f3.place(x=10,y=150,width=480,height=390)

        f4=Frame(self.root,bg="#1565C0",bd=0,relief=RAISED)
        f4.place(x=510,y=90,width=480,height=390)


        f5=Frame(self.root,bg="white",bd=0,relief=RAISED)
        f5.place(x=510,y=490,width=480,height=50)

        #Frame 2
        self.v=StringVar()
        self.file_name_lbl=Label(f2,text="",font=("times new roman",8),bg="#5DADE2",fg="white",bd=2,relief=RAISED,textvariable=self.v)
        self.file_name_lbl.place(x=10,y=10,width=380,height=30)

        browse_btn=Button(f2,text="Browse",border=2,bg="#AAB7B8",cursor="hand2",font=("times new roman",12,"bold"),command=self.open_file,activebackground="#AAB7B8",activeforeground="black")
        browse_btn.place(x=400,y=10,width=70,height=30)

        #Frame 5
        clear_btn=Button(f5,text="Clear",font=("times new roman",14,"bold"),bd=2,bg="#1565C0",fg="white",cursor="hand2",command=self.clear_data,activebackground="#1565C0",activeforeground="white")
        clear_btn.place(x=10,y=5,width=140,height=40)

        copy_btn=Button(f5,text="Copy",font=("times new roman",14,"bold"),bd=2,bg="#1565C0",fg="white",cursor="hand2",command=self.copy_data,activebackground="#1565C0",activeforeground="white")
        copy_btn.place(x=170,y=5,width=140,height=40)

        generate_btn=Button(f5,text="Generate",font=("times new roman",14,"bold"),bd=2,bg="#1565C0",fg="white",cursor="hand2",command=self.generate,activebackground="#1565C0",activeforeground="white")
        generate_btn.place(x=330,y=5,width=140,height=40)

        #Frame 3
        self.image_lbl=Label(f3,bg="white")
        self.image_lbl.place(x=10,y=10,width=460,height=370)
        
        #Frame 4
        text_lbl=Label(f4,text="Text Area",bg="#1565C0",fg="white",font=("times new roman",30,"bold"))
        text_lbl.pack(fill=X,pady=5)

        #Frame 4        
        scroll_y=Scrollbar(f4,orient=VERTICAL)
        self.txtarea=Text(f4,yscrollcommand=scroll_y.set,bg="white",fg="black")
        self.txtarea.place(x=10,y=100,width=460,height=320)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

   
    #Frame 2 Browse Button
        
    def open_file(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("PNG File","*.png"),("JPG File","*.jpg"),("All Files","*")))
        self.v.set(fln)
        img=Image.open(fln)
        self.img_text=tess.image_to_string(img)
        img.thumbnail((450,350))
        img=ImageTk.PhotoImage(img)
        self.image_lbl.configure(image=img)
        self.image_lbl.image=img
        

    #Frame 5 GENERATE btn
    def generate(self):
        if self.v.get()=="":
            messagebox.showerror("Error","Please select an Image.")
        else: 
            self.txtarea.insert(END,self.img_text)
    
    #Frame 5 CLEAR btn
    def clear_data(self):
        self.txtarea.delete(1.0,END)

    #Frame 5 COPY btn
    def copy_data(self):
        if self.v.get()=="":
            messagebox.showerror("Error","Please select a Image.")
        else:
            root.clipboard_clear()
            txt = self.txtarea.get('1.0',END)
            root.clipboard_append(txt)
            messagebox.showinfo("Success","Content Copied.",parent=self.root)
        
object=image_to_text(root)
mainloop()

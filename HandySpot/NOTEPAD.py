from tkinter import*
from tkinter import messagebox
import pymysql
root=Tk()
class note:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x550+150+50")
        self.root.title("NOTE")
        self.root.resizable(0,0)
        self.root.config(bg="#9D0037")

        #---FRAMES---
        f1=Frame(self.root,bg="#9D0037",bd=2)
        f1.place(x=5,y=10,width=485,height=50)

        f2=Frame(self.root,bg="#9D0037",bd=2)
        f2.place(x=510,y=10,width=485,height=50)

        f3=Frame(self.root,bg="#9D0037",bd=5)
        f3.place(x=500,y=0,width=5,height=70)

        f4=Frame(self.root,bg="#9D0037",bd=2)
        f4.place(x=5,y=70,width=990,height=470)
        
        #---WIDGITS OF FRAMES---
        self.file_name=Text(f1,font=("Courier New",20,"bold"),bd=2,relief=GROOVE,bg="#FEF5E7")
        self.file_name.place(x=2,y=2,width=365,height=40)

        save_btn=Button(f1,text="SAVE",bd=1,relief=RAISED,font=("Courier New",18,"bold"),cursor="hand2",command=self.save_text)
        save_btn.place(x=375,y=3,width=100,height=40)

        self.file_name_open=Text(f2,font=("Courier New",20,"bold"),bd=2,relief=GROOVE,bg="#FEF5E7")
        self.file_name_open.place(x=10,y=2,width=365,height=40)

        open_btn=Button(f2,text="OPEN",bd=1,relief=RAISED,font=("Courier New",18,"bold"),cursor="hand2",command=self.open_file)
        open_btn.place(x=380,y=3,width=100,height=40)


        #---TEXT AREA---
        scroll_y=Scrollbar(f4,orient=VERTICAL)
        self.note_txt=Text(f4,yscrollcommand=scroll_y.set,bg="#FFFDE7",fg="black",font=("Courier New",16,"bold"),bd=2)
        self.note_txt.place(x=5,y=70,width=990,height=470)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.note_txt.yview)
        self.note_txt.pack(fill=BOTH,expand=1)

    #---BUTTON FUNCTIONS---
    def save_text(self):
        if self.file_name.get(1.0,END)=="":
            messagebox.showerror("Error","Enter File name.",parent=self.root)
        elif self.note_txt.get(1.0,END)=="":
            messagebox.showerror("Error","Enter some Data.",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                c=con.cursor()
                c.execute("insert into notes (name,data) values(%s,%s)",
                (
                    self.file_name.get(1.0,END),
                    self.note_txt.get(1.0,END)
                ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","NOTES SAVED.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)


    def open_file(self):
        if self.file_name_open.get('1.0','end')=="":
            messagebox.showerror("Error","Enter name to Open.",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="project")
                c=con.cursor()
                c.execute("select * from notes where name=%s",(self.file_name_open.get('1.0',END)))
                col=c.fetchall()
                if c==None:
                    messagebox.showerror("Error","Invalid File Name.",parent=self.root)
                else:
                    for row in col:
                        data = row[2]
                    self.note_txt.delete('1.0',END)
                    self.note_txt.insert(END,data)
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)




notes=note(root)
mainloop()
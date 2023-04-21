from tkinter import*
root=Tk()
root.title("CALCULATOR")
root.geometry("1000x550+150+50")
root.resizable(0,0)
val=""

#=---FUNCTIONS OF THE BUTTONS---

#---NUMBERS FUNCTIONS---
def number(num):
    global val
    val=val+str(num)
    data.set(val)

#---OPERATIONS FUNCTIONS---
def operator(opr):
    global val
    if val[-1]=='0' or val[-1]=='1' or val[-1]=='2' or val[-1]=='3' or val[-1]=='4' or val[-1]=='5' or val[-1]=='6' or val[-1]=='7' or val[-1]=='8' or val[-1]=='9':
        val=str(eval(val))
        val=val+str(opr)
        data.set(val)
    else:
        val=str(val)
        val=val[0:-1]
        val=val+str(opr)
        data.set(val)    

#---PLUS MINUS SIGN---
def plus_minus():
    global val
    val=str(eval(val))
    val=int(val)
    val=val*(-1)
    val=str(val)
    data.set(val)

#---DELETE FUNCTION---
def del_last():
    global val
    val=str(val)
    val=val[0:-1]
    data.set(val)

#---POWER FUNCTION---
def power():
    global val
    val=val+"**"
    data.set(val)

#---CLEAR BUTTON---
def btn_cleardata():
    global val
    val=""
    data.set(val)

#---EQUAL BUTTON---
def btn_equal_result():
    global val
    val=str(eval(val))
    result=eval(val)
    data.set(result)

#---OUTPUT LABEL---

data=StringVar()
lbl=Label(root,text="",anchor=SE,font=("verdana",36),textvariable=data,bg="white",fg="black")
lbl.pack(expand=True,fill="both")

#---BUTTONS FRAMES---

f1=Frame(root)
f1.pack(expand=True, fill="both")

btn1=Button(f1,text="1",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(1),cursor="hand2",activebackground="gray")
btn1.pack(side=LEFT,expand=True,fill="both")
btn2=Button(f1,text="2",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(2),cursor="hand2",activebackground="gray")
btn2.pack(side=LEFT,expand=True,fill="both")
btn3=Button(f1,text="3",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(3),cursor="hand2",activebackground="gray")
btn3.pack(side=LEFT,expand=True,fill="both")
btn_add=Button(f1,text="+",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda:operator('+'),cursor="hand2",activebackground="gray")
btn_add.pack(side=LEFT,expand=True,fill="both")
btn3=Button(f1,text="DEL",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,cursor="hand2",activebackground="gray",command=del_last)
btn3.pack(side=LEFT,expand=True,fill="both")
        
f2=Frame(root)
f2.pack(expand=True, fill="both")

btn4=Button(f2,text="4",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(4),cursor="hand2",activebackground="gray")
btn4.pack(side=LEFT,expand=True,fill="both")
btn5=Button(f2,text="5",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(5),cursor="hand2",activebackground="gray")
btn5.pack(side=LEFT,expand=True,fill="both")
btn6=Button(f2,text="6",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(6),cursor="hand2",activebackground="gray")
btn6.pack(side=LEFT,expand=True,fill="both")
btn_sub=Button(f2,text="-",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda:operator('-'),cursor="hand2",activebackground="gray")
btn_sub.pack(side=LEFT,expand=True,fill="both")
btn3=Button(f2,text="^",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,cursor="hand2",activebackground="gray",command=power)
btn3.pack(side=LEFT,expand=True,fill="both")

        
f3=Frame(root)
f3.pack(expand=True, fill="both")

btn7=Button(f3,text="7",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(7),cursor="hand2",activebackground="gray")
btn7.pack(side=LEFT,expand=True,fill="both")
btn8=Button(f3,text="8",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(8),cursor="hand2",activebackground="gray")
btn8.pack(side=LEFT,expand=True,fill="both")
btn9=Button(f3,text="9",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(9),cursor="hand2",activebackground="gray")
btn9.pack(side=LEFT,expand=True,fill="both")
btn_mul=Button(f3,text="*",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda:operator('*'),cursor="hand2",activebackground="gray")
btn_mul.pack(side=LEFT,expand=True,fill="both")
btn3=Button(f3,text="+/-",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,cursor="hand2",activebackground="gray",command=plus_minus)
btn3.pack(side=LEFT,expand=True,fill="both")

        
f4=Frame(root)
f4.pack(expand=True, fill="both")

btn_clear=Button(f4,text="C",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=btn_cleardata,cursor="hand2",activebackground="gray")
btn_clear.pack(side=LEFT,expand=True,fill="both")
btn0=Button(f4,text="0",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number(0),cursor="hand2",activebackground="gray")
btn0.pack(side=LEFT,expand=True,fill="both")
btn3=Button(f4,text=".",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda : number('.'),cursor="hand2",activebackground="gray")
btn3.pack(side=LEFT,expand=True,fill="both")
btn_div=Button(f4,text="/",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=lambda:operator('/'),cursor="hand2",activebackground="gray")
btn_div.pack(side=LEFT,expand=True,fill="both")
btn_equal=Button(f4,text="=",font=("verdana",22,"bold"),width=2,height=1,bd=0,relief=GROOVE,command=btn_equal_result,cursor="hand2",activebackground="gray")
btn_equal.pack(side=LEFT,expand=True,fill="both")


mainloop()
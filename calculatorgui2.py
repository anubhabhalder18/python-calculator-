'''
Created on 27-10-2022 at 14:16 hrs

Author- anubhabanubhab92
'''



from tkinter import *

root=Tk()
root.title("Calculator")


def b1():
    e.insert(1000,"1")
    
def b2():
    e.insert(1000,"2")

def b3():
    e.insert(1000,"3")

def b4():
    e.insert(1000,"4")

def b5():
    e.insert(1000,"5")
    
def b6():
    e.insert(1000,"6")

def b7():
    e.insert(1000,"7")

def b8():
    e.insert(1000,"8")

def b9():
    e.insert(1000,"9")
    
def b10():
    e.insert(1000,"0")

def b11():
    e.insert(1000,"+")

def b12():
    e.insert(1000,"-")

def b13():
    e.insert(1000,"*")
    
def b14():
    e.insert(1000,"/")

def b15():
    try:
        t=e.get()
        t=eval(t)
        e.delete(0,END)
        e.insert(0,str(t))
    except:
        e.delete(0,END)
        e.insert(0,"ERROR")
def b16():
    e.insert(1000,"(")
    
def b17():
    e.insert(1000,")")

def bclr():
    e.delete(0,END)

def b18():
    e.insert(1000,".")
    
#r=Entry(root,text="Ans",bg="light yellow",fg="black",font='Arial 20').grid(row=6,columnspan=4)

e=Entry(root,fg="black",bg="light blue",font=('Arial 20'),width=16)
e.grid(columnspan=4,row=0)
e.get()



B1=Button(root,text="1",fg="green",bg="black",command=b1,pady=20,padx=20,font='Arial 14').grid(row=1,column=0)
B2=Button(root,text="2",fg="green",bg="black",command=b2,pady=20,padx=20,font='Arial 14').grid(row=1,column=1)
B3=Button(root,text="3",fg="green",bg="black",command=b3,pady=20,padx=20,font='Arial 14').grid(row=1,column=2)

B4=Button(root,text="4",fg="green",bg="black",command=b4,pady=20,padx=20,font='Arial 14').grid(row=2,column=0)
B5=Button(root,text="5",fg="green",bg="black",command=b5,pady=20,padx=20,font='Arial 14').grid(row=2,column=1)
B6=Button(root,text="6",fg="green",bg="black",command=b6,pady=20,padx=20,font='Arial 14').grid(row=2,column=2)

B7=Button(root,text="7",fg="green",bg="black",command=b7,pady=20,padx=20,font='Arial 14').grid(row=3,column=0)
B8=Button(root,text="8",fg="green",bg="black",command=b8,pady=20,padx=20,font='Arial 14').grid(row=3,column=1)
B9=Button(root,text="9",fg="green",bg="black",command=b9,pady=20,padx=20,font='Arial 14').grid(row=3,column=2)

B10=Button(root,text="0",fg="green",bg="black",command=b10,pady=20,padx=20,font='Arial 14').grid(row=4,column=0)

B11=Button(root,text="+",fg="black",bg="yellow",command=b11,pady=20,padx=20,font='Arial 14').grid(row=1,column=3)
B12=Button(root,text="-",fg="black",bg="yellow",command=b12,pady=20,padx=20,font='Arial 14').grid(row=2,column=3)
B13=Button(root,text="*",fg="black",bg="yellow",command=b13,pady=20,padx=20,font='Arial 14').grid(row=3,column=3)
B14=Button(root,text="/",fg="black",bg="yellow",command=b14,pady=20,padx=20,font='Arial 14').grid(row=4,column=3)

B15=Button(root,text="=",fg="white",bg="red",command=b15,pady=20,padx=20,font='Arial 14').grid(row=5,column=2)

B16=Button(root,text="(",fg="white",bg="red",command=b16,pady=20,padx=20,font='Arial 14').grid(row=5,column=0)
B17=Button(root,text=")",fg="white",bg="red",command=b17,pady=20,padx=20,font='Arial 14').grid(row=5,column=1)
Bc=Button(root,text="CLR",fg="Red",bg="black",command=bclr,pady=20,padx=40,font='Arial 14').grid(row=4,column=1,columnspan=2)

B18=Button(root,text=".",fg="white",bg="red",command=b18,pady=20,padx=20,font='Arial 14').grid(row=5,column=3)




root.mainloop()

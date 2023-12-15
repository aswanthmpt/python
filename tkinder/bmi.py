from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()

def bmi():
    num1=float(e1.get())
    num2=float(e2.get())
    ht=num1/100
    bm=num2/(ht*ht)
    res.set(bm)
    if bm>=30:
        red.set("obesity")
    elif bm>=25:
        red.set("over weight")
    elif bm>=18.5:
        red.set("normal weight")
    elif bm<18:
        red.set("under weight")
    
l1=Label(frame,text="enter height in cm",bg="green",fg="white")
e1=Entry(frame)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)

l2=Label(frame,text="enter weight in  kg",bg="green",fg="white")
e2=Entry(frame)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)

l3=Label(frame,text="enter your age",bg="green",fg="white")
e3=Entry(frame)
l3.grid(row=2,column=0)
e3.grid(row=2,column=1)


fr=Frame(root)
fr.pack()
bt=Button(fr,text="submit",command=bmi,bg="red",fg="white")
bt.grid(row=0,column=0)

res=StringVar()
res.set("BMI is")
l3=Label(root,textvariable=res)
l3.pack()

red=StringVar()
red.set("result")
l4=Label(root,textvariable=red)
l4.pack()



root.mainloop()
from tkinter import *
root=Tk()
l1=Label(root,text="username")
e1=Entry(root)
l2=Label(root,text="mobile")
e2=Entry(root)
l3=Label(root,text="email")
e3=Entry(root)
l4=Label(root,text="age")
e4=Entry(root)
l5=Label(root,text="password")
e5=Entry(root)
l6=Label(root,text="confirm password")
e6=Entry(root)
bt=Button(root,text="login",bg="green")
bt1=Button(root,text="cancel",bg="red")
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
l3.grid(row=2,column=0)
e3.grid(row=2,column=1)
l4.grid(row=3,column=0)
e4.grid(row=3,column=1)
l5.grid(row=4,column=0)
e5.grid(row=4,column=1)
l6.grid(row=5,column=0)
e6.grid(row=5,column=1)
bt.grid(row=6,column=0)
bt1.grid(row=6,column=1)



root.mainloop()
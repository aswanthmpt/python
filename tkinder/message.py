# from tkinter import *
# from tkinter import messagebox
# root=Tk()
# def asd():
#     # messagebox.showinfo("Delete","are you sure to delete")
#     # messagebox.showerror("Delete","are you sure to delete")
#     # messagebox.showwarning("Delete","are you sure to delete")
#     # messagebox.askokcancel("Delete","are you sure to delete")
#     # messagebox.askquestion("Delete","are you sure to delete")
#     # messagebox.askretrycancel("Delete","are you sure to delete")
#     #   messagebox.askyesno("Delete","are you sure to delete")
#      messagebox.askyesnocancel("Delete","are you sure to delete")
# Button(root,text="ok",command=asd).pack()



# root.mainloop()

from tkinter import *
# from tkinter import messagebox
root=Tk()
l1=Label(root,text="enter first number")
e1=Entry(root)
l1.pack()
e1.pack()
l2=Label(root,text="enter second number")
e2=Entry(root)
l2.pack()
e2.pack()
# def asd():
#    messagebox.askquestion("Delete","are you sure to quite")
bt2=Button(root,text="add")
# bti=Button(root,text="exit")
# bt2.grid(row=0,column=0)
bt2.pack()
# bti.grid(row=0,column=1)

root.mainloop()
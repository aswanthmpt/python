from tkinder import *
root=Tk()
root.title("Calcualtor")
root.geometry("312x324")
frame=Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", 
highlightthickness = 1 )
frame.pack(side = TOP)

def click(item):
   global expression
   expression=expression+str(item)
   e1.set(expression)
    
res=StringVar()
e1=Entry(frame, font = ('arial', 18, 'bold'),textvariable= res, bg = "white",width=24,  bd = 0, 
justify = RIGHT)
e1.grid(row=0,column=0)

f1 = Frame(root,width = 312, height = 272.5, bg = "grey") 
f1.pack() 



c = Button(f1, text = "C", fg = "black", width = 
32, height = 3, bd = 0, bg = "grey", cursor = "hand2")
c.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1) 

d = Button(f1, text = "/", fg = "black", width = 
10, height = 3, bd = 0, bg = "green", cursor = "hand2")
d.grid(row = 0, column = 3, 
padx = 1, pady = 1) 

seven = Button(f1, text = "7",command=lambda:click("7"), fg = "black", width = 
10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
seven.grid(row = 1, column = 0, padx = 1, pady = 1 ) 

eight = Button(f1, text = "8", fg = "black", width = 
10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
eight.grid(row = 1, column = 1, padx = 1, pady = 1) 

nine = Button(f1, text = "9", fg = "black", width = 
10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
nine.grid(row = 1, column = 2, padx = 1, pady = 1) 

mul = Button(f1, text = "*", fg = "black", width = 
10, height = 3, bd = 0, bg = "green", cursor = "hand2")
mul.grid(row = 1, column = 3, padx = 1, pady = 1) 



four = Button(f1, text = "4", fg = "black", width = 
10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
four.grid(row = 2, column = 0, padx = 1, pady = 1) 

five = Button(f1, text = "5", fg = "black", width = 
10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
five.grid(row = 2, column = 1, padx = 1, pady = 1) 

six = Button(f1, text = "6", fg = "black", width = 
10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
six.grid(row = 2, column = 2, padx = 1, pady = 1) 

sub = Button(f1, text = "-", fg = "black", width = 
10, height = 3, bd = 0, bg = "green", cursor = "hand2")
sub.grid(row = 2, column = 3, padx = 1, pady = 1) 



one = Button(f1, text = "1", fg = "black", width = 
10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
one.grid(row = 3, column = 0, padx = 1, pady = 1) 

two = Button(f1, text = "2", fg = "black", width = 
10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
two.grid(row = 3, column = 1, padx = 1, pady = 1) 

three = Button(f1, text = "3", fg = "black", width = 
10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
three.grid(row = 3, column = 2, padx = 1, pady = 1) 

add = Button(f1, text = "+", fg = "black", width = 
10, height = 3, bd = 0, bg = "green", cursor = "hand2")
add.grid(row = 3, column = 3, padx = 1, pady = 1) 


zero = Button(f1, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1) 


point = Button(f1, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2")
point.grid(row = 4, column = 2, padx = 1, pady = 1) 


equals = Button(f1, text = "=", fg = "black", width = 
10, height = 3, bd = 0, bg = "green", cursor = "hand2")
equals.grid(row = 4, column = 3, padx = 1, pady = 1) 






root.mainloop()
from tkinter import *
class myclass:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.btn=Button(frame,text="ok",command=self.oks)
        self.btn.pack()
        self.bt1=Button(frame,text="quit",command=frame.quit)
        self.bt1.pack()

def oks(self):
    print("hello")

root=Tk()
obj= myclass(root)



root.mainloop()
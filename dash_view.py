from Tkinter import *
class Pot:
    def __init__ (self,master):
        frame=Frame(master)
        frame.pack()

        self.label=Label(master,text='pot position', padx=5, pady=5, relief=RIDGE)
        self.label.pack(side=LEFT, padx=10, pady=10)

class Accel:
    def __init__ (self,master):
        frame=Frame(master)
        frame.pack()

        self.label=Label(frame,text='Accel position',padx=5, pady=5, relief=RIDGE)
        self.label.pack(side=LEFT, padx=10, pady=10)

root=Tk()

pot=Pot(root)
accel=Accel(root)

root.mainloop()

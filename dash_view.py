from Tkinter import *
import datetime
from time import sleep
class View:
    def __init__ (self,master):
        frame=Frame(master)
        frame.pack()

        self.pot_value=StringVar()
        self.pot_value.set('not workin')

        self.accel_value=StringVar()
        self.accel_value.set('Fuckity fuck fuck')

        self.label=Label(master,textvar=self.pot_value, padx=5, pady=5, relief=RIDGE)
        self.label.pack(side=LEFT, padx=10, pady=10)


        self.label=Label(frame,textvar=self.accel_value,padx=5, pady=5, relief=RIDGE)
        self.label.pack(side=LEFT, padx=10, pady=10)

    def display_pot(self, master, datatuple):
        time=datatuple[0]
        data=datatuple[1]

        self.pot_value.set('potentiometer: %g at %s'%(data,str(time)))
        master.update_idletasks()

    def display_accel(self, master,datatuple):
        time=datatuple[0]
        data=datatuple[1]

        x=data[0]
        y=data[1]
        z=data[2]

        self.accel_value.set('X: %g \t Y: %g \t Z: %g at %s' %(x,y,z,str(time)))
        master.update_idletasks()






time=datetime.datetime.today()


     
root=Tk()
view=View(root)
tup=(time,1.0,'potentiometer')
view.display_pot(root, tup)
sleep(2)
tup=(time,5.0,'potentiometer')
tup2=(time,[1,2,3],'accel')
view.display_pot(root, tup)
view.display_accel(root,tup2)
root.mainloop()
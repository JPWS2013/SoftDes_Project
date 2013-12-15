from Tkinter import *
import datetime
from time import sleep
import random
import math

class View:
    def __init__ (self,master,model):
        self.model=model

        self.pot_value=StringVar()
        self.pot_value.set('not workin')

        self.accel_value=StringVar()
        self.accel_value.set('Fuckity fuck fuck')

        self.now=StringVar()
        self.now.set('fuckin fuck')

        self.steering=Label(master,textvar=self.pot_value, width=50, padx=5, pady=5, relief=RIDGE,font=('Helvetica',16))
        self.steering.grid(row=0)

        self.accel=Label(master,textvar=self.accel_value, width=50, padx=5, pady=5, relief=RIDGE, font=('Helvetica',16))
        self.accel.grid(row=1)

        self.gaspedal=Canvas(master,width=250,height=250)
        self.gaspedal.grid(row=0,column=1, rowspan=4)
        self.brakepedal=Canvas(master,width=250,height=250)
        self.brakepedal.grid(row=0,column=2, rowspan=4)

        self.timer=Label(master,textvar=self.now, padx=5,pady=5,font=('Helvetica,16'))
        self.timer.grid(row=2)

        self.quit=Button(master,text='QUIT', command=master.quit, font=('Helvetica,12'))
        self.quit.grid(row=0, column=3)

        self.speed=Label


        self.update()
        master.mainloop()

    def update(self):
        self.display_pot(random.random())
        self.display_accel((random.random(),random.random(),random.random()))
        self.display_gaspedal()
        self.display_brakepedal(random.random())
        self.display_time(datetime.datetime.today())
        root.after(200,self.update)


    def display_pot(self, data):
        self.pot_value.set('potentiometer: %g'%(data))


    def display_accel(self,datatuple):
        x=datatuple[0]
        y=datatuple[1]
        z=datatuple[2]
        self.accel_value.set('X: %g \t Y: %g \t Z: %g' %(x,y,z))


    def display_gaspedal(self):
        senseid='Potentiometer0'
        data=self.model.sensedict[senseid][self.model.sensedict[senseid].keys()[-1]]
        self.gaspedal.delete(ALL)
        self.gaspedal.create_rectangle(0,0,250,250,fill='blue')
        length=250
        pot=data
        height=length*math.sin(math.pi*pot/4+math.pi/6)
        base=length*math.cos(math.pi*pot/4+math.pi/6)
        self.gaspedal.create_line(0,0,base,height, width=20)
        self.gaspedal.create_text(200,75,text='Gas Pedal', font='Helvetica,12')

    def display_brakepedal(self,data):
        self.brakepedal.delete(ALL)
        self.brakepedal.create_rectangle(0,0,250,250,fill='red')
        length=250
        pot=data
        height=length*math.sin(math.pi*pot/4+math.pi/6)
        base=length*math.cos(math.pi*pot/4+math.pi/6)
        self.brakepedal.create_line(0,0,base,height, width=20)
        self.brakepedal.create_text(200,75,text='Brake Pedal', font='Helvetica,12')


    def display_time(self,datetime):
        self.now.set(datetime)

     
if __name__ == '__main__':
     
    root=Tk()
    view=View(root)
    
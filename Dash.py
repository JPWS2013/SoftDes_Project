from Tkinter import *
import datetime
from time import sleep
import random
import math
import modelclassdef as model
import serial
from PIL import Image, ImageTk

class View:
    def __init__ (self,master,model):
        self.model=model
        self.master=master
        # model.view=self

        self.now=StringVar()
        self.now.set('Time')

        self.gaspedal=Canvas(master,width=250,height=250)
        self.gaspedal.grid(row=0,column=1)
        self.brakepedal=Canvas(master,width=250,height=250)
        self.brakepedal.grid(row=0,column=2)

        self.timer=Label(master,textvar=self.now, padx=5,pady=5,font=('Helvetica,16'))
        self.timer.grid(row=2, column=0)

        self.accel=Canvas(master, width=500, height=350)
        self.accel.grid(row=1,column=1, columnspan=3)

        self.quit=Button(master,text='QUIT', command=master.quit, font=('Helvetica,12'))
        self.quit.grid(row=0, column=3)

        self.speedo=Canvas(master, width=500, height=250)
        self.speedo.grid(row=0,column=0)
        image = Image.open("speedo.png")
        photo = ImageTk.PhotoImage(image)
        self.speedo.image=photo
        self.speedo.create_image(300,125,image=photo)

        self.tach=Canvas(master, width=500, height=250)
        self.tach.grid(row=1,column=0)


        ser=serial.Serial('/dev/ttyACM0', 9600) #Defines the serial port to use

        ser.close()
        ser.open()

        if ser.isOpen():
            print "Database ready to receive data" 
        self.update(ser)
        master.mainloop()
        

    def update(self, ser):

        while True:
            raw_message=ser.readline()

            if raw_message[:2]=='&&':
                break
        
        message=raw_message.strip()
        command=message[2]
        data=message[4:]
        datalist=data.split(',')

        if command=='1':
            self.model.store_sensor(datalist[0], datalist[1], datalist[2])
            # model.print_loc()

        if command=='2':
            self.model.store_data_pot(datalist[0], datalist[1], datalist[2])


        if command=='3':
            self.model.store_data_accel(datalist[0], datalist[1], datalist[2])

        if command=='4':
            self.model.store_data_halleffect(datalist[0], datalist[1], datalist[2])
            
        self.display_gaspedal()
        self.display_brakepedal()
        self.display_time(datetime.datetime.today())
        self.display_speed()
        self.master.after(100,self.update, ser)

    def display_speed(self):
        data=random.randrange(40)
        theta=data*math.pi/40
        length=100
        base=math.cos(theta)*length
        height=length*math.sin(theta)
        self.speedo.delete(ALL)
        self.speedo.create_image(300,125,image=self.speedo.image)
        self.speedo.create_line(300,200,300-base,200-height, width=10, fill='red')
        self.tach.create_text(500,100,text='Speedometer',font='Helvetica,16')

    def display_tach(self):
        data=random.randrange(40)
        theta=data*math.pi/40
        length=100
        base=math.cos(theta)*length
        height=length*math.sin(theta)
        self.tach.delete(ALL)
        self.tach.create_image(300,125,image=self.speedo.image)
        self.tach.create_line(300,200,300-base,200-height, width=10, fill='red')
        self.tach.create_text(500,100,text='Tachometer',font='Helvetica,16')


    def display_accel(self):
        self.accel.delete(ALL)
        x=random.randrange(-5,5)
        y=random.randrange(-5,5)
        z=random.randrange(-5,5)
        self.accel.create_rectangle(25,175,125,175+x*30, fill='blue')
        self.accel.create_rectangle(175,175,275,175+y*30, fill='blue')
        self.accel.create_rectangle(325,175,425,175+z*30, fill='blue')
        self.accel.create_rectangle(25,25,125,325, width=5)
        self.accel.create_line(25,175,125,175,width=5)
        self.accel.create_rectangle(175,25,275,325, width=5)
        self.accel.create_line(175,175,275,175,width=5)
        self.accel.create_rectangle(325,25,425,325, width=5)
        self.accel.create_line(325,175,425,175,width=5)
        self.accel.create_text(75,340,text='X', font='Helvetica,16')
        self.accel.create_text(225,340,text='Y', font='Helvetica,16')
        self.accel.create_text(375,340,text='Z', font='Helvetica,16')
        self.accel.create_text(225,10,text='Acceleration',font='Helvetica,16')

    def display_gaspedal(self):
        senseid='Potentiometer0'
        # print self.model.sensedict[senseid].keys()
        try:
            datadict=self.model.sensedict[senseid]
            allentries=datadict.keys()
            allentries.sort()
            data=datadict[allentries[-1]]
            self.gaspedal.delete(ALL)
            self.gaspedal.create_rectangle(0,0,250,250,fill='blue')
            length=250
            pot=data
            height=length*math.sin(math.pi*pot/4+math.pi/6)
            base=length*math.cos(math.pi*pot/4+math.pi/6)
            self.gaspedal.create_line(0,0,base,height, width=20)
            self.gaspedal.create_text(200,75,text='Gas Pedal', font='Helvetica,16')

        except (KeyError, IndexError):
            self.gaspedal.delete(ALL)
            self.gaspedal.create_rectangle(0,0,250,250,fill='blue')
            length=250
            # pot=data
            # height=length*math.sin(math.pi*pot/4+math.pi/6)
            # base=length*math.cos(math.pi*pot/4+math.pi/6)
            self.gaspedal.create_line(0,0,0,250, width=20)
            self.gaspedal.create_text(200,75,text='Gas Pedal', font='Helvetica,16')


    def display_brakepedal(self):
        try:
            data=self.model.lastpotreading
            self.brakepedal.delete(ALL)
            self.brakepedal.create_rectangle(0,0,250,250,fill='red')
            length=250
            pot=data
            height=length*math.sin(math.pi*pot/4+math.pi/6)
            base=length*math.cos(math.pi*pot/4+math.pi/6)
            self.brakepedal.create_line(0,0,base,height, width=20)
            self.brakepedal.create_text(200,75,text='Brake Pedal', font='Helvetica,12')
        except (KeyError,IndexError):
            self.brakepedal.delete(ALL)
            self.brakepedal.create_rectangle(0,0,250,250,fill='red')
            self.brakepedal.create_line(0,0,0,250, width=20)
            self.brakepedal.create_text(200,75,text='Brake Pedal', font='Helvetica,12')



    def display_time(self,datetime):
        self.now.set(datetime)

     
if __name__ == '__main__':
    model=model.Model()

    root=Tk()
    view=View(root, model)
    
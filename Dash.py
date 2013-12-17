"""

This is the main module that should be run on the PC. It contains instructions for building a GUI as well as instructions for fetching data on a regular basis

This module is intended to be run on a linux PC.

Written for Software Design, Fall 2013 by Justin Poh and Zoe Fiddler

"""

from Tkinter import *
import datetime
from time import sleep
import random
import math
import modelclassdef as model
import serial
from PIL import Image, ImageTk
import pickle

class View:
    """
    This class defines methods that instantiate a dashboard GUI and regularly updates it with fresh data
    """

    def __init__ (self,master,model):
        self.model=model
        self.master=master
        
        def exit_protocol(master):
            """ Method called when quit button is pressed
                writes data to a pickle file
                master: instance of Tk 
            """

            pickle.dump( model.sensedict, open( "datafile.txt", "w") )

            master.quit()

        #Initialize all of the widgets in the GUI

        #Time display
        self.now=StringVar()
        self.now.set('Time')

        #Gas Pedal
        self.gaspedal=Canvas(master,width=250,height=250)
        self.gaspedal.grid(row=0,column=1)

        #Brake Pedal
        self.brakepedal=Canvas(master,width=250,height=250)
        self.brakepedal.grid(row=0,column=2)

        #Clock
        self.timer=Label(master,textvar=self.now, padx=5,pady=5,font=('Helvetica,16'))
        self.timer.grid(row=2, column=0)

        #Accelerometers
        self.accel=Canvas(master, width=500, height=350)
        self.accel.grid(row=1,column=1, columnspan=3)

        #Quit Button
        self.quit=Button(master,text='QUIT', command=lambda: exit_protocol(master), font=('Helvetica,12'))
        self.quit.grid(row=0, column=3)

        #Speedometer, initially displays background image with no line
        self.speedo=Canvas(master, width=500, height=300)
        self.speedo.grid(row=0,column=0)
        image = Image.open("speedo.png")    #speedo background image
        photo = ImageTk.PhotoImage(image)
        self.speedo.image=photo
        self.speedo.create_image(300,125,image=photo)

        #Tachometer, initially displays background image with no line
        self.tach=Canvas(master, width=600, height=300)
        self.tach.grid(row=1,column=0)
        image2 = Image.open("tach.png") #tach background image
        photo2 = ImageTk.PhotoImage(image2)
        self.tach.image=photo2


        ser=serial.Serial('/dev/ttyACM0', 9600) #Defines the serial port to use

        ser.close()
        ser.open()

        if ser.isOpen():
            print "Database ready to receive data" 
        
        #Display GUI and begin updating
        self.update(ser)
        master.mainloop()
        

    def update(self, ser):
        """ 
        Gets data from Beaglebone and updates GUI to display it
        ser: serial port

        This function has no return value
        """

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
            # print 'I got a message'
            self.model.store_data_accel(datalist[0], datalist[1], datalist[2])

        if command=='4':
            self.model.store_data_halleffect(datalist[0], datalist[1], datalist[2])

        #Call functions to update GUI
        self.display_gaspedal()
        self.display_brakepedal()
        self.display_time(datetime.datetime.today())
        self.display_speed()
        self.display_tach()
        self.display_accel()

        #set timer to call function again
        self.master.after(10,self.update, ser)

    def display_speed(self):
        """ 
        Gets data from Hall effect sensor and changes speedometer GUI to diplay it
        
        This function has no return value
        """
        senseid='HallEffectSensor3' 

        try:
            #find current speed
            datadict=self.model.sensedict[senseid]
            allentries=datadict.keys()
            allentries.sort()
            data=datadict[allentries[-1]][1]

            #calculate line dimensions
            theta=data*math.pi/40
            length=100
            base=math.cos(theta)*length
            height=length*math.sin(theta)

            #change GUI
            self.speedo.delete(ALL)
            self.speedo.create_image(275,125,image=self.speedo.image)
            self.speedo.create_line(250,225,250-base,225-height, width=10, fill='red')
            self.speedo.create_text(300,275,text='Speedometer (MPH)',font=('Helvetica',16))

        except (KeyError, IndexError):
            #When no data is stored, display line at 0 MPH)
            data=0
            theta=data*math.pi/40
            length=100
            base=math.cos(theta)*length
            height=length*math.sin(theta)
            self.speedo.delete(ALL)
            self.speedo.create_image(275,125,image=self.speedo.image)
            self.speedo.create_line(250,225,250-base,225-height, width=10, fill='red')
            self.speedo.create_text(300,275,text='Speedometer (MPH)',font=('Helvetica',16))


    def display_tach(self):
        """ 
        Gets data from Hall effect sensor and changes Tachometer GUI to diplay it
        
        This function has no return value
        """
        senseid='HallEffectSensor3'

        try:
            #Get current tach reading
            datadict=self.model.sensedict[senseid]
            allentries=datadict.keys()
            allentries.sort()
            data=datadict[allentries[-1]][0]

            #calculate line dimensions
            theta=data*math.pi/4000
            length=100
            base=math.cos(theta)*length
            height=length*math.sin(theta)

            #change GUI
            self.tach.delete(ALL)
            self.tach.create_image(275,140,image=self.tach.image)
            self.tach.create_line(250,240,250-base,240-height, width=10, fill='red')
            self.tach.create_text(300,280,text='Tachometer (RPM)',font=('Helvetica',16))

        except (KeyError, IndexError):
            #When no data stored, display line at 0 RPM
            data=0
            theta=data*math.pi/4000
            length=100
            base=math.cos(theta)*length
            height=length*math.sin(theta)
            self.tach.delete(ALL)
            self.tach.create_image(275,140,image=self.tach.image)
            self.tach.create_line(250,240,250-base,240-height, width=10, fill='red')
            self.tach.create_text(300,280,text='Tachometer (RPM)',font=('Helvetica',16))
    

    def display_accel(self):
        """
        Gets data from accelerometer and changes GUI to display it

        This function has no return value
        """
        senseid='Accelerometer2'
        
        try:
            #get current accelerometer reading
            datadict=self.model.sensedict[senseid]
            allentries=datadict.keys()
            allentries.sort()
            data_list=datadict[allentries[-1]]
            self.accel.delete(ALL)
            
            #unpack accelerometer data
            x=data_list[0]
            y=data_list[1]
            z=data_list[2]
            
            #change GUI
            self.accel.create_rectangle(25,175,125,175+x*30, fill='blue')
            self.accel.create_rectangle(175,175,275,175+y*30, fill='blue')
            self.accel.create_rectangle(325,175,425,175+z*30, fill='blue')
            self.accel.create_rectangle(25,25,125,325, width=5)
            self.accel.create_line(25,175,125,175,width=5)
            self.accel.create_rectangle(175,25,275,325, width=5)
            self.accel.create_line(175,175,275,175,width=5)
            self.accel.create_rectangle(325,25,425,325, width=5)
            self.accel.create_line(325,175,425,175,width=5)
            self.accel.create_text(75,340,text='X', font=('Helvetica',16))
            self.accel.create_text(225,340,text='Y', font=('Helvetica',16))
            self.accel.create_text(375,340,text='Z', font=('Helvetica',16))
            self.accel.create_text(225,10,text='Acceleration',font=('Helvetica',16))
       
        except (KeyError, IndexError):
            #when no data is stored, display empty fill bar
            self.accel.delete(ALL)
            self.accel.create_rectangle(25,25,125,325, width=5)
            self.accel.create_line(25,175,125,175,width=5)
            self.accel.create_rectangle(175,25,275,325, width=5)
            self.accel.create_line(175,175,275,175,width=5)
            self.accel.create_rectangle(325,25,425,325, width=5)
            self.accel.create_line(325,175,425,175,width=5)
            self.accel.create_text(75,340,text='X', font=('Helvetica',16))
            self.accel.create_text(225,340,text='Y', font=('Helvetica',16))
            self.accel.create_text(375,340,text='Z', font=('Helvetica',16))
            self.accel.create_text(225,10,text='Acceleration',font=('Helvetica',16))


    def display_gaspedal(self):
        """ 
        Gets data from potentiometer and changes gas pedal GUI to display it 

        This function has no return value
        """
        senseid='Potentiometer0'

        try:
            #get current gas pedal pot reading
            datadict=self.model.sensedict[senseid]
            allentries=datadict.keys()
            allentries.sort()
            data=datadict[allentries[-1]]

            #calculate line dimensions
            length=250
            pot=data
            height=length*math.sin(math.pi*pot/4+math.pi/6)
            base=length*math.cos(math.pi*pot/4+math.pi/6)

            #change GUI
            self.gaspedal.delete(ALL)
            self.gaspedal.create_rectangle(0,0,250,250,fill='blue')
            self.gaspedal.create_line(0,0,base,height, width=20)
            self.gaspedal.create_text(200,75,text='Gas Pedal', font='Helvetica,16')

        except (KeyError, IndexError):
            #When no data, display line straight down
            self.gaspedal.delete(ALL)
            self.gaspedal.create_rectangle(0,0,250,250,fill='blue')
            length=250
            self.gaspedal.create_line(0,0,0,250, width=20)
            self.gaspedal.create_text(200,75,text='Gas Pedal', font='Helvetica,16')


    def display_brakepedal(self):
        """ 
        Gets data from potentiometer and changes brake pedal GUI to display it 

        This function has no return value
        """

        senseid='Potentiometer1'

        try:
            #get current brake pedal potentiometer reading
            datadict=self.model.sensedict[senseid]
            allentries=datadict.keys()
            allentries.sort()
            data=datadict[allentries[-1]]
            
            #calculate line dimensions
            length=250
            pot=data
            height=length*math.sin(math.pi*pot/4+math.pi/6)
            base=length*math.cos(math.pi*pot/4+math.pi/6)

            #Change GUI
            self.brakepedal.delete(ALL)
            self.brakepedal.create_rectangle(0,0,250,250,fill='red')
            self.brakepedal.create_line(0,0,base,height, width=20)
            self.brakepedal.create_text(200,75,text='Brake Pedal', font='Helvetica,12')
        except (KeyError,IndexError):
            #When no data, display line straight down
            self.brakepedal.delete(ALL)
            self.brakepedal.create_rectangle(0,0,250,250,fill='red')
            self.brakepedal.create_line(0,0,0,250, width=20)
            self.brakepedal.create_text(200,75,text='Brake Pedal', font='Helvetica,12')



    def display_time(self,datetime):
        """ 
        Changes GUI to display current time

        datetime: string of datetime object

        This function has no return value
        """

        self.now.set(datetime)

     
if __name__ == '__main__':
    model=model.Model()

    root=Tk()
    view=View(root, model)
"""

Module that defines the text view class that provides a command line view of car status

"""


class TextView(object):

    def __init__(self, model):

        self.model=model
        model.view=self

    def display_car(self):
        print ' '
        print "Your car status is as follows: "
        print ' '

        for eachSensor in self.model.senseloc.keys():

            senseprop=self.model.senseloc[eachSensor]

            if senseprop[0]=='Potentiometer':
                print "%s - %s degrees" % (senseprop[1], self.model.sensedict[eachSensor][self.model.sensedict[eachSensor].keys()[-1]])

            if senseprop[0]=='Accelerometer':
                print "%s - X: %s, Y: %s, Z: %s" % (senseprop[1], self.model.sensedict[eachSensor][-1][0], self.model.sensedict[eachSensor][-1][1], self.model.sensedict[eachSensor][-1][2])

    def display_pot(self, senseid):
        print "Potentiometer has changed position to: %s degrees" % (self.model.sensedict[senseid][self.model.sensedict[senseid].keys()[-1]])

    def display_accel(self, sensor):
        print "Accelerometer has changed to: X: %s, Y: %s, Z: %s" % (self.model.sensedict[sensor.senseid][self.model.sensedict[sensor.senseid].keys()[-1]][0], self.model.sensedict[sensor.senseid][self.model.sensedict[sensor.senseid].keys()[-1]][1], self.model.sensedict[sensor.senseid][self.model.sensedict[sensor.senseid].keys()[-1]][2])
        
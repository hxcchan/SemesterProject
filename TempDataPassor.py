'''
Created on 2018

@author: HSong
'''

#This is a module that will pass data from sensors and start running the app.
#Set the pixel

from SemesterProject import SensorReader

while 1:
    t= sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    for l in range (int(t) - 23):
        if l < 8:
            sense.set_pixel(1,7 - l, [255,0,0] )
    for l in range (int(p/2) - 500):
        if l < 8:
            sense.set_pixel(3,7 - l, [0,255,0] )
    for l in range (int(h) - 35):
        if l < 8:
            sense.set_pixel(5,7 - l, [0,0,255] )
time.sleep(10)


startRunning = senseHatAdaptor.start()

startRunning.run()
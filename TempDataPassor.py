{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset134 \'cb\'ce\'cc\'e5;}}
{\*\generator Riched20 10.0.17134}\viewkind4\uc1 
\pard\f0\fs22 '''\par
Created on 2018\par
\par
@author: HSong\par
'''\par
\par
#This is a module that will pass data from sensors and start running the app.\par
\par
from SemesterProject import SensorReader\par
\lang2052 while 1:\par
\tab t= sense.get_temperature()\par
\tab p = sense.get_pressure()\par
\tab h = sense.get_humidity()\par
\tab for l in range (int(t) - 23):\par
\tab\tab if l < 8:\par
\tab\tab\tab sense.set_pixel(1,7 - l, [255,0,0] )\par

\pard\tab for l in range (int(p/2) - 500):\par
\tab\tab if l < 8:\par
\tab\tab\tab sense.set_pixel(3,7 - l, [0,255,0] )\lang0\par
\lang2052\tab for l in range (int(h) - 35):\par
\tab\tab if l < 8:\par
\tab\tab\tab sense.set_pixel(5,7 - l, [0,0255] )\par
time.sleep(10)\lang0\par

\pard\par
startRunning = senseHatAdaptor.start()\par
\par
startRunning.run()\par
}
 
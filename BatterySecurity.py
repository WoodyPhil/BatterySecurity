#!/usr/bin/env python3.4$

from __future__ import print_function

import Batterystate
import subprocess
import Tkinter
#from Smfl.audio import Listener
import sys
import time
from osax import *

#Volume control
sa = OSAX()
for i in range(50):
    sa.set_volume(i*2)
    time.sleep(0.1)

#sf.Listener.set_global_volume = 30

#def set_password:
#    password = new_password

#replacing by Torben
old_string_length = 0
def print_replace(string):
    global old_string_length
    if len(string) < old_string_length:
        print('\r' + string + (old_string_length - len(string)) * ' ', end='\r')
    else:
        print('\r' + string, end='\r')
    sys.stdout.flush()
    old_string_length = len(string)

#while True:
#    print_replace('bier')
#    time.sleep(2)
#    print_replace('hanspeter')
#    time.sleep(2)


# Hauptfenster
main = Tkinter.Tk()

#Das abzuspielende Warnsignal
audio_file = "/Users/Woody/Documents/nanana.wav"

# Funktion zu Button Ende
def ende():
    main.destroy()

# Funktion der Security
def security():
    while Batterystate.getBatteryStatus() == 999:
        print_replace('Ihr MacBook ist geschuetzt')
        time.sleep(1)
    else:
        while Batterystate.getBatteryStatus() != 999:
            return_alarm = subprocess.call(["afplay", audio_file])
            print_replace('Ihr MacBook wird geklaut!')

#Button fuer Security-Start
b = Tkinter.Button(main, text = "Security - Modus starten!", command = security)
b.pack()

#Button Ende
b = Tkinter.Button(main, text = "Ende", command = ende)
b.pack()

        
#Endlosschleife
main.mainloop()
        
        

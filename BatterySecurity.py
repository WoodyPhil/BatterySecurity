#!/usr/bin/env python3.4$

from __future__ import print_function

__author__ = 'Philippe Woodruff'
#__copyright__ = 'see module docstring'
#__credits__ = 'Philippe Woodruff',
#__license__ = 'see module docstring'
__maintainer__ = 'Philippe Woodruff'
__maintainer_email__ = 'philippe.woodruff@googlemail.com'
#__status__ = 'stable'
#__version__ = '1.0'

import Batterystate
import subprocess
import Tkinter
import sys
import time
from osax import *
import getpass

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

#Main Window
main = Tkinter.Tk()

#arert signal
audio_file = "/Users/Woody/Documents/nanana.wav"

#function for closing button
def ende():
    main.destroy()

#function that asks the user to enter an password
def p():
    getpass.getpass()


#main security function
def security():
    while Batterystate.getBatteryStatus() == 999:
        print_replace('Ihr MacBook ist geschuetzt')
        time.sleep(1)
    else:
        while Batterystate.getBatteryStatus() != 999:
            #increase volume to max
            sa = OSAX()
            for i in range(50):
                sa.set_volume(i*2)
                time.sleep(0.1)
            return_alarm = subprocess.call(["afplay", audio_file])
            print_replace('Ihr MacBook wird geklaut!')

#button to set the user password
b = Tkinter.Button(main, text = "Passwort festlegen", command = p)
b.pack()

#button for starting the securitymode
b = Tkinter.Button(main, text = "Security - Modus starten!", command = security)
b.pack()

#closing button
b = Tkinter.Button(main, text = "Ende", command = ende)
b.pack()

        
#endless loop
main.mainloop()
        
        

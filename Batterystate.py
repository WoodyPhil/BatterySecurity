#!/usr/bin/env python3.4$
import subprocess
import os, sys
import tkSnack

BATTERY_CMD = ["/usr/sbin/ioreg", "-l"]
GREP_CMD    = ["/usr/bin/egrep", "Capacity|ExternalChargeCapable"]

def main(argv):
    content      = getBatteryStatus()
    print(content)

    return 0

def getBatteryStatus():
    process = subprocess.Popen(BATTERY_CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    grep    = subprocess.Popen(GREP_CMD, stdin=process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    grep.wait()
    output  = grep.communicate()[0]
    #print output
    batteryStatus = output.split("\n")
    #print batteryStatus
    if len(batteryStatus) < 3:
        #print(batteryStatus)
        return "Could not get battery status"
   
    if "Yes" in batteryStatus[0]:
        return 999
        
              

print __name__

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
    
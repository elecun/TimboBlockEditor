
# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

#import webrepl
#webrepl.start()


try:
  import usocket as socket
except:
  import socket

import time

import esp
esp.osdebug(None)

import gc
gc.collect()

#connect to network via wifi

ssid = 'U+Net76AB'
password = '1000009347'

import wlan
wlan.start_wlan(ssid, password, 32)

#exec(open('./net/broker.py').read())






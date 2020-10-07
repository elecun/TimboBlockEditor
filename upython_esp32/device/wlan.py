
import network
import machine
import time


def start_wlan(ssid, password, pin):
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid,password)
  wpin = machine.Pin(pin, machine.Pin.OUT)
  
  while station.isconnected() == False:
    time.sleep_ms(500)
    wpin.on()
    time.sleep_ms(500)
    wpin.off()
  
  print(station.ifconfig())
  wpin.on()
  


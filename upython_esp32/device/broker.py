
import time
import _thread

try:
  import usocket as socket
except:
  import socket

def run():
  print("Start broker...")
  broker_run = True
  port = 8080
  addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]
  sock = socket.socket()
  sock.setblocking(True)
  sock.bind(addr)
  sock.listen(1)
  
  while broker_run == True:
    conn, caddr = sock.accept()
    print('client connected from', caddr)
    data = sock.recv(1000)
    print(data);
    
    
    
_thread.start_new_thread(run, ())








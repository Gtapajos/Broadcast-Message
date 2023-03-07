import socket
import time
 
def send_broadcast():
    msg = b"Hello, broadcast world!"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(("", 0))
   
    start_time = time.time()
    while time.time() - start_time < 10:
        s.sendto(msg, ("255.255.255.255", 12345))
        print("Broadcast message sent")
        time.sleep(0.01)
   
    s.close()
 
send_broadcast()
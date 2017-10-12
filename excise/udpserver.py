#author：zoe
from time import ctime
import socket
host = ''
port = 12789
buffsize=1024
ADDR = (host,port)
udpserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpserver.bind(ADDR)
while True:
    print("wait for message...")
    data,addr =udpserver.recvfrom(buffsize)
    returnmsg ="hello!"
    #udpserver.sendto((returnmsg.encode('utf-8')),addr)
    udpserver.sendto(('[%s] %s'%(ctime(),data)).encode('utf-8'),addr)
    print('return to %s'%data)
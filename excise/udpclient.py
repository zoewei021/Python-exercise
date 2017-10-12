#author：zoe
import socket
host ='localhost'
port = 12789
buffsize = 1024
ADDR =(host,port)
udpclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg = input("pleast input massage")
    data =msg.encode('utf-8')
    if data == 0:
        break
    udpclient.sendto(data,ADDR)
    data = udpclient.recvfrom(buffsize)
    print(data)
    if not data:
        break
    print (udpclient.close())
udpclient.close()
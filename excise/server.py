#!/user/bin/env python
# author：zoe
import os
import socket

server = socket.socket()
server.bind(('localhost', 9897))
server.listen(5)
print("wait for calling")
while True:
    conn, addr = server.accept()  # wait for calling
    while True:
        data = conn.recv(1024)
        print("serv2:", data)
        if not data:
            print("client has lost...")
            break
        data2=data.decode("utf-8")
        res = os.popen(data2).read()
        conn.send(res.encode("utf-8"))

server.close()

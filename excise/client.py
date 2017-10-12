#!/user/bin/env python
# author：zoe
# client 客户端
#date：2017/10/12
#修改内容
import socket

client = socket.socket()
client.connect(('localhost', 9897))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0: continue
    client.send(msg.encode("utf-8"))#按utf-8的方式编码，转成bytes
    data = client.recv(10240000)
    f=open("")
    print("recv:", data.decode())

client.close()

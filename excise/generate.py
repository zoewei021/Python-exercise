#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import time
import os
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(5)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")
c = consumer( "zoe")
c.__next__()

b1 = "jiucai"
c.send(b1)

print(os.path.abspath(_file_))

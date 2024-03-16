"""
poll方法示例
"""

from select import *
from socket import *
from time import sleep

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

f = open('net.log','r+')
print(f.fileno())

# 查找字典   通过文件描述符 --> 查找IO对象
fdmap = {s.fileno():s,f.fileno():f}


sleep(3)

# 创建对象
poll = poll()
poll.register(s,POLLIN)
poll.register(f,POLLIN|POLLOUT)

# 提交监控IO发生
events = poll.poll()
print(events)








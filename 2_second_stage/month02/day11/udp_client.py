"""
udp 客户端
重点代码
"""

from socket import *

# 服务端地址
server_address = ("127.0.0.1",8888)

# 创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 消息传输
while True:
    msg = input(">> ")
    if not msg:
        # 结束循环
        break
    udp_socket.sendto(msg.encode(),server_address)
    data,addr = udp_socket.recvfrom(20)
    print("从服务端收到:",data.decode())


# 关闭套接字
udp_socket.close()
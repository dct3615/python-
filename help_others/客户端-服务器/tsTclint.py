# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:31:35 2019

@author: 00124175
"""

from socket import *

#HOST = '127.0.0.1'
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)#创建客户端套接字
tcpCliSock.connect(ADDR)#尝试连接服务器

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())#发送数据
    data = tcpCliSock.recv(BUFSIZ).decode()#接收tcp消息
    if not data:
        break
    print(data)
tcpCliSock.close()
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:50:53 2019
UDP时间戳客户端
@author: 00124175
"""

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21534
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)#创建服务器套接字

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode(),ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode())
    
udpCliSock.close()


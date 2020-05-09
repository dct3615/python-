# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:40:24 2019
UDP时间戳服务器
@author: 00124175
"""

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21534
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)#创建服务器套接字
udpSerSock.bind(ADDR)#套接字与地址绑定

while(True):
    print('waiting for message...')
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(('[%s] %s' % (ctime(), data.decode())).encode(),addr)#数据返回客户端
    print('...received from and return to:',data.decode())
    
udpSerSock.close()
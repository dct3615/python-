# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)#创建服务器套接字
tcpSerSock.bind(ADDR)#套接字与地址绑定
tcpSerSock.listen(5)#监听连接

while True:
    print('waiting for connection...')
    tcpCliSock,addr = tcpSerSock.accept()#接收客户端连接
    print('...connected from:',addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)#接收客户端数据
        if not data:
            break
        print(data.decode('utf-8'))
        tcpCliSock.send(('[%s] %s' % (ctime(), data.decode())).encode())#数据返回客户端
    tcpCliSock.close()#关闭客户端套接字
tcpSerSock.close()#关闭服务器套接字
#socekt assignment

#reading from the web

import socket

mysocks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            #file handle

mysocks.connect(('data.pr4e.org', 80))                                 #creates connection

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()     #command to send

mysocks.send(cmd)


while True:
    data = mysocks.recv(512)
    if len(data) <1:
        break
    print(data.decode())
mysocks.close()


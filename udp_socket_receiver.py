import socket


#udp protocol 
myp=socket.SOCK_DGRAM

#ipv4 n/w family
afn=socket.AF_INET

#telling computer to use this socket
s = socket.socket(afn, myp)

ip = "192.168.43.12"
port = 2222

s.bind( (ip,port) )

#this will take input via network of  ax size 1024 
x = s.recvfrom(1024)

print(x[0])



import socket
UDPServerSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPServerSocket.bind(("127.0.0.1",3377))
print("Server is ready to received")
while True:
    message,clientaddress=UDPServerSocket.recvfrom(2048)
    msg=message.decode()
    msg1=msg
    intnum=0
    for i in range(len(msg1)):
        d=int(msg1[len(msg1)-i-1])
        intnum+=(d*(2**i))
    #ret=d[msg]
    hexnum=str(hex(intnum))
    octnum=str(oct(intnum))
    intnum=str(intnum)
    final=intnum+" "+octnum+" "+hexnum
    UDPServerSocket.sendto(final.encode(),clientaddress)

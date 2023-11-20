import socket
import sys
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=('localhost',10000)
client.connect(server_address)
message=input("enter message")
while message and message!="bye":
    print("sending ",message)
    client.sendall(message.encode())
    #print("original:",message)
    data=client.recv(1000).decode()
    print("server:",data)
    message=input("enter message")
client.close()

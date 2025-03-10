from socket import *
serverPort = 12001
# serverSocket = socket(AF_INET, SOCK_STREAM) # TCP
serverSocket = socket(AF_INET, SOCK_DGRAM) # UDP
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
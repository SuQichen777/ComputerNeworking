from socket import *
serverName = 'localhost'
serverPort = 12001
# clientSocket = socket(AF_INET, SOCK_STREAM) # TCP
clientSocket = socket(AF_INET, SOCK_DGRAM) # UDP
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

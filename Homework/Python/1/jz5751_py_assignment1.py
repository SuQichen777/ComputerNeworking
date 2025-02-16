from socket import * 

#Create a TCP server socket
#Code Start
serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Code End
while True:
    #Establish the connection
    print("The server is ready to receive")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        # print(filename)
        f = open("./html_files/" + filename[1:])
        outputdata = f.read()
        #Send HTTP OK and the Set-Cookie header into the socket
        # set the cookie to whatever value you'd like
        #Code Start
        response_headers = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "Set-Cookie: session_id=12345\r\n"
            "\r\n"
        )
        connectionSocket.send(response_headers.encode())
        # connectionSocket.send(outputdata.encode())
        #Code End
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            # Close the socket 
        #Code Start 
        print("Connection closed")
        connectionSocket.close()
        #Code End
    except IOError:
        #Send HTTP NotFound response 
        #Code Start 
        errorHeaders = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            "<html><body><h1>404 Not Found</h1></body></html>"
        )
        connectionSocket.send(errorHeaders.encode())
        #Code End
        # Close the socket
        #Code Start
        print("Connection closed")
        connectionSocket.close()
        # break
        #Code End 
serverSocket.close()
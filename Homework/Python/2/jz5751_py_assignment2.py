from socket import *
import base64

# dig MX nyu.edu
mailserver = "mxb-00256a01.gslb.pphosted.com"
serverPort = 25

# Create socket and establish TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverPort))
tcp_resp = clientSocket.recv(1024).decode()
print(tcp_resp)

# Send HELO command to begin SMTP handshake.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
helo_resp = clientSocket.recv(1024).decode()
print(helo_resp)

# Send MAIL FROM command and print response.
mailFromCommand = 'MAIL FROM: <jz5751@nyu.edu>\r\n'
clientSocket.send(mailFromCommand.encode())
mailFrom_resp = clientSocket.recv(1024).decode()
print(mailFrom_resp)

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: <jz5751@nyu.edu>\r\n'
clientSocket.send(rcptToCommand.encode())
rcptTo_resp = clientSocket.recv(1024).decode()
print(rcptTo_resp)

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
data_resp = clientSocket.recv(1024).decode()
print(data_resp)

# Send email data.
message = ""
From = "From: Jiaxi Z <jz5751@nyu.edu>\r\n"
To = "To: Jiaxi Z <jz5751@nyu.edu>\r\n"
Subject = "Subject: SMTP Mail Client Test\r\n"
 # Add the message to the email body
message += From + To + Subject + "\r\n"
 # mail body
body = "This is a test email in computer networking course.\r\n"
message += body
 # end
message += "\r\n.\r\n"
clientSocket.send(message.encode())
data_resp = clientSocket.recv(1024).decode()
print(data_resp)


# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
quit_resp = clientSocket.recv(1024).decode()
print(quit_resp)

clientSocket.close()

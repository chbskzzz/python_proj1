import socket

s = socket.socket()
host = 'localhost'
port=8080

s.connect((host,port))
message = s.recv(1024) # 1024 byte 를 받아서 뿌린다. 2로 하면 'He' 만 출력되고 다음에 또 출력

while message:
    print("Message : ", message.decode())
    message=s.recv(1024)

s.close()
import socket

host='localhost'
port=8080
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("The Server is listening for client request on port ", port)
con,address=s.accept()
print("Connection has been established form ", str(address))
try:
    fileName=con.recv((1024))
    file=open(fileName,'rb')
    readFile=file.read()
    con.send(readFile)
    file.close()
    con.close()
except:
    con.send("File Not Found on the server".encode())

# con.send("Hello My name is Bilal and I am the Sever".encode())
# con.close()

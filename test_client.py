import socket

host = socket.gethostbyname('localhost')
port_number = 6789

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

mySocket.connect((host, port_number))

recv_msg = mySocket.recv(1024)

print(recv_msg.decode())

mySocket.sendall(bytes("Hello Server!", "utf-8"))

mySocket.close()


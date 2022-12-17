from v2_proxy import Proxy

prox = Proxy(6789)
prox.bind(prox.get_tsap())
prox.listen()

while True:
    (new_connection, tsap) = prox.accept()

    print("New connection from", tsap)

    new_connection.sendall(bytes("Hello Barry", "utf-8"))

    recv_msg = new_connection.recv(1024)

    print(recv_msg.decode())

    new_connection.close()
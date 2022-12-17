import socket

class Proxy(socket.socket):
    def __init__(self, port_number: int) -> None:
        super().__init__(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__port_number = port_number
        self.__tsap = ('', port_number)
        
    def get_port_number(self):
        return self.__port_number

    def get_tsap(self):
        return self.__tsap

    def serve(self):
        self.listen()
        while True:
            (new_connection, tsap) = self.accept()
            

    

    



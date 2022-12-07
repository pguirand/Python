# socket
# bind (ip, port) 127.0.0.1 -> localhost
# accept -> socket / (ip, port)
# close

import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 
#In case port already in use commonly on windows.
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attende de connexion sur {HOST_IP} - PORT{HOST_PORT}...")
connection_socket, client_address = s.accept()

print(f"Connexion etablie avec {client_address}")

while True:
    text_envoye = input("Vous : ")
    # faut encoder parce que les sockets n'acceptent que les 
    # octets not other types like string
    connection_socket.sendall(text_envoye.encode())
    data_recv = connection_socket.recv(MAX_DATA_SIZE)
    if not data_recv:
        break
    print("Message : ", data_recv.decode())


s.close()
connection_socket.close()

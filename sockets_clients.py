

import socket, time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024


print(f"Connexion au serveur {HOST_IP}, port {HOST_PORT}...")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("Impossible de se connecter au serveur. Reconnexion")
        time.sleep(4)
    else:
        print("Connected to server")
        break

while True:

    data_recv = s.recv(MAX_DATA_SIZE)
    if not data_recv:
        break
    print("Message : ", data_recv.decode())
    text_envoye = input("Vous : ")
    s.sendall(text_envoye.encode())
 
s.close()

   # else:
    #     print("Aucune donnees")
# print(data_recv.decode()) # Decode msg previously encoded by server

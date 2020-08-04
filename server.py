# Hocamızın verdiği şekilde serverımı oluşturdum.
# targethosta istenen değerleri yazdım.
# Nazım Umut Öçgüder 171220036

# UDPPingServer.py
import random
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12345))  # UDP Port no:12345
while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    print("[", message, "]")
    if rand < 4:
        print("[", message, "] DROPPED")
        continue

    if (message.decode().startswith("PING")):
        serverSocket.sendto("PONG".encode(), address)

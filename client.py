# localhostla(127.0.0.1) deneyip çalıştığını test ettim.
# Nazım Umut Öçgüder 171220036

import time
import socket

with open('targethosts.txt', 'r') as file:
    lines = file.read().splitlines()
    a = 1

for x in lines:
    print("#" + str(a) + ". Hedef:" + str(x))
    a = a+1

    for pings in range(5):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(1.0)
        message = b'PING'
        addr = (str(x), 12345)
        start = time.time()
        client_socket.sendto(message, addr)

        try:
            data, server = client_socket.recvfrom(1024)
            end = time.time()
            elapsed = end - start
            print("-> UDP: " + str(x))
            print("<- RTT: " + str(float(elapsed)) + "ms")
            # int verdiğimde daha hoş bir görüntü oluyor ancak böyle de localhostta çalıştığımda net sonuç veriyor.

        except socket.timeout:
            print('Paket kaybı')
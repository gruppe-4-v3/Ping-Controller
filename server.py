import socket
from time import sleep

serverName = '192.168.0.255'
serverPort = 12000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as clientSocket:
    clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    count = 0
    while True:
        clientSocket.sendto(str(count).encode(), (serverName, serverPort))
        count += 1
        sleep(5)
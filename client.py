import socket

PORT = 12000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as clientSocket:
    clientSocket.bind(('', PORT))
    clientSocket.settimeout(10)     # Timeout after 10 seconds of not reciving any data

    while True:
        message = clientSocket.recv(2048)
        print('Received:', message.decode())
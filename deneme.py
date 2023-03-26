import socket

UDP_IP_ADDRESS = "127.0.0.1" # İsteğin gönderileceği IP adresi
UDP_PORT_NO = 5005 # İsteğin gönderileceği port numarası

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    clientSock.sendto("Isteğiniz", (UDP_IP_ADDRESS, UDP_PORT_NO))
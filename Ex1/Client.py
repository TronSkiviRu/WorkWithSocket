import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'smsi', ('localhost', 10100))
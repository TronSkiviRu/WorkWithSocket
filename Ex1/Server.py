import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )
s.bind(('localhost', 10100))
result = s.recv(1024)
print('Message: ', result.decode('utf-8'))
s.close()


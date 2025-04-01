import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10100))
s.send(b'SAKURA')
s.close()
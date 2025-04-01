import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10100))
s.send('Теперь можно по русски:) а не байтовой строкой'.encode('utf-8'))
s.close()
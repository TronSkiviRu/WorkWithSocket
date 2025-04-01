import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 10100))
s.listen(2)
s.settimeout(1.0)

print('Server listening')
while True:
    try:
        client, addr = s.accept()
        print(f'Connection from {addr}')
        try:
            result = client.recv(1024)
            if result:
                print('Message: ', result.decode('utf-8'))
            else:
                print('No data received.')
        except Exception as e:
            print('Error receiving data:', e)
        finally:
            client.close()
    except KeyboardInterrupt:
        print('Shutting down server.')
        s.close()
        break
    except socket.timeout:
        continue
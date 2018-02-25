import socket

port = 12000
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM  # TCP
)
server_socket.bind(('', port)) # '' means local host
server_socket.listen(1) # maximum number of connections is 1

print('The server is ready to receive...')

try:
    while 1:
        connection_socket, addr = server_socket.accept()
        msg = connection_socket.recv(1024)  # buffer size

        print('The server has received the following conent:\n' + msg.decode())

        data = ('Server received: ' + msg.decode()).encode()
        connection_socket.send(data)
        connection_socket.close()

except KeyboardInterrupt:
    print('KeyboardInterrupt detected.')
    print('Closing socket...')
    server_socket.close()
    print('Done!')

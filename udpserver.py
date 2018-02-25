import socket

server_port = 12000
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM  ## UDP
)

server_socket.bind(('', server_port))

print('Server is ready to receive...')

server_socket.sendto(('Server has got message:\n' + msg.decode()).encode(), client_address)

while 1:
    msg, client_address = server_socket.recvfrom(1024)  # buffer size
    print('Server has received the following content: \n' + msg.decode())
    server_socket.sendto(('Server has got message:\n' + msg.decode()).encode(), client_address)


# try:
#     while 1:
#         msg, client_address = server_socket.recvfrom(1024)  # buffer size
#         print('Server has received the following content: \n' + msg.decode())
#         server_socket.sendto(('Server has got message:\n' + msg.decode()).encode(), client_address)
#
# except KeyboardInterrupt:
#     print('KeyboardInterrupt detected.')
#     print('Closing socket...')
#     server_socket.close()
#     print('Done!')



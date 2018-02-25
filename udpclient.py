import socket

server_name = '127.0.0.1'
server_port = 12000

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

msg = input('Content to be sent:\n')
client_socket.sendto(msg.encode(), (server_name, server_port))

data_from_server, info = client_socket.recvfrom(1024) # buffer size
print('\nReceive from server:')
print(data_from_server.decode())

client_socket.close()
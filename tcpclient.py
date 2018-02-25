import socket

server_name = '127.0.0.1'
server_port = 12000
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM  # TCP client
)
client_socket.connect((server_name, server_port))

sentence = input('Input a sentence to be sent:')
data = sentence.encode('utf-8')

client_socket.send(data)  # No need to attach server name and port
response = client_socket.recv(1024)  # buffer size
client_socket.close()

print('From server:\n{}'.format(response.decode()))

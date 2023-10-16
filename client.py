import socket

ADDRESS = 'localhost'
PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ADDRESS, PORT))
print(sock.recv(1024))

print('File received successfully.')

with open('doc.txt', 'r', encoding='utf-8') as file:
    print('Received File Content:')
    for line in file:
        print(line.strip())

while True:
    message = input('Message: ')
    sock.send(message.encode('utf-8'))   
    if message == 'bye':
        break
    
    data = sock.recv(1024)
    print(data)
    if data.decode('utf-8') == 'bye':
        print('Server says bye.')
        break

sock.close()

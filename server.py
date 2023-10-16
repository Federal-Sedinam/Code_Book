import socket

ADDRESS = ''
PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ADDRESS, PORT))
sock.listen(3)
client, _ = sock.accept()

with open('doc.txt', 'w', encoding='utf-8') as file:
    file.write('this file is for practice.\n')
    file.write('it will be sent from a server to client.')

print("Enter a text to send file succcessfully")

while True:   
    message = input('Message: ')
    client.send(message.encode('utf-8'))
    if message == 'bye':
        break
   
    data = client.recv(1024)
    print(data)
    if data.decode('utf-8')== 'bye':
        print('Client says bye.')
        break

client.close()

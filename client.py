# import asyncio
# import websockets

# async def message(msg):
# 	async with websockets.connect("ws://localhost:4999") as socket:
# 		socket.sendall(bytes(msg+'\n', 'utf-8'))
# 		# socket.send(msg+'\n')
# 		print('done')


# msg = "hi hi"
# print(msg)
# asyncio.get_event_loop().run_until_complete(message(msg))

import socket

HOST = "localhost"
PORT = 4999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print (socket.getaddrinfo(HOST,PORT))
buffer_size = 100

while True :  
   
    test = "who are you\n"
    sock.sendall(bytes(test, 'utf-8'))
    print ('you sent : ' , test)
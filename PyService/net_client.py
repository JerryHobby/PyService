# echo_client.py 
# echo_client.py 
# echo_client.py 
# echo_client.py 

import socket 

host = socket.gethostname() 
port = 12345 # The same port as used by the server 

text = [b'Hello World', b'Work goes here.', b'Goodbye World', b'quit' ]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host, port)) 

for msg in text:
	s.sendall(msg) 

	data = s.recv(1024) 
	print('Received', repr(data)) 

s.close() 


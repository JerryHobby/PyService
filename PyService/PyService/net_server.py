# echo_server.py 

import socket 

host = '' 	# Symbolic name meaning all available interfaces 
port = 12345 	# Arbitrary non-privileged port 

def process(conn, data):

	conn.sendall(data) 

	if(data == b"quit"):
		return(False)

	return(True)


def main():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	s.listen(1) 
	
	conn, addr = s.accept() 
	
	print('Connected by', addr) 
	
	while True: 
		data = conn.recv(1024) 
		if not data: 
			break 
		if not process(conn, data):
			return(False)
	
	conn.close()  
	return(True)

while(main()):
	pass
	

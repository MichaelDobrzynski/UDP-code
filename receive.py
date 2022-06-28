import socket

UDP_IP = "192.168.0.30"			#  PIs own IP Address
UDP_RETURN = "192.168.0.24"			#  IP adress from sender
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)	# Buffer size is 1024 bytes
	print "recived message: ", data
	sock.sendto(data, (UDP_RETURN, UDP_PORT))


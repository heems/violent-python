from socket import *
import socket

def conn_scan(port, host):
	try:
		test_socket = socket.socket(AF_INET, SOCK_STREAM)
		test_socket.connect((host, port)) #higher level than socket.connect(), works for both AF_INET and AF_INET6
		test_socket.send('thing')
		results = test_socket.recv(128)
		print '[+] Port %d open.' % port
		print '[+] ' + str(results)
	except socket.gaierror:
		print 'Could not connect to host.'
	except:
		print '[-] Port %d closed.' % port

host = raw_input("enter hostname (google.com): ")
print("\n")
port = int(raw_input("enter port numbers (1, 2, 3): "))

conn_scan(port, host)

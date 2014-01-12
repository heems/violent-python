from socket import *
import socket
from threading import *

screenlock = Semaphore(value=1)

def conn_scan(host, port):
	try:
		test_socket = socket.socket(AF_INET, SOCK_STREAM)
		test_socket.connect((host, port)) #higher level than socket.connect(), works for both AF_INET and AF_INET6
		test_socket.send('thing')
		results = test_socket.recv(128)
		screenlock.acquire()
		print '[+] Port %d open.' % port
		print '[+] ' + str(results)
	except socket.gaierror:
		print 'Could not connect to host.'
	except:
		print '[-] Port %d closed.' % port
	finally:
		screenlock.release()
		test_socket.close()

host = raw_input("enter hostname (google.com): ")
print("\n")
ports = raw_input("enter port numbers (1, 2, 3): ").split(", ")
print ports

for port in ports:
	t = Thread(target=conn_scan, args=(host, int(port)))
	t.start()
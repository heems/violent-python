from socket import *
import socket



def conn_scan(port, host):
	try:
		test_socket = socket.socket(AF_INET, SOCK_STREAM)
		test_socket.create_connection(host, port) #higher level than socket.connect(), works for both AF_INET and AF_INET6
		print '[+] Port %d open.' % port
	except:
		print '[-] Port %d closed.' % port




# def port_scan(host, ports):
# 	try:
# 		tgtIP = gethostby


host = raw_input("enter hostname (google.com): ")
print("\n\n")
port = raw_input("enter port numbers (1, 2, 3): ")

conn_scan()

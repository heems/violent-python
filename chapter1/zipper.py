import zipfile
from threading import Thread
import timeit

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		#return password
		print "password is " + password
	except Exception, e:
		#return
		pass


# def main(): 15.24 sec runtime
# 	zFile = zipfile.ZipFile("evil.zip")
# 	passFile = open('longdict.txt')
# 	for line in passFile.readlines():
# 		password = line.strip("\n")
# 		#t = Thread(target=extractFile, args=(zFile,password))
# 		#t.start()
# 		guess = extractFile(zFile, password)
# 		if guess:
# 			print '[+] Password is ' + password

def main(): #32.3 s runtime?
	zFile = zipfile.ZipFile("evil.zip")
	passFile = open('longdict.txt')
	for line in passFile.readlines():
		password = line.strip("\n")
		t = Thread(target=extractFile, args=(zFile,password))
		t.start()

start = timeit.default_timer()
main()
stop = timeit.default_timer()
print "Finished in %f seconds." % (stop - start)
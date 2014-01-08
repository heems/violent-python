import zipfile
from threading import thread
import optparse

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		return password
	except Exception, e:
		return


def main():
	zFile = zipfile.ZipFile("evil.zip")
	passFile = open('dictionary.txt')
	for line in passFile.readlines():
		password = line.strip("\n")
		guess = extractFile(zFile, password)
		if guess:
			print '[+] Password is ' + password
			exit(0)

main()
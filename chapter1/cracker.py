import fcrypt

def test_pass(crypt_pass):
	salt = crypt_pass[0:2]
	dict_file = open('dictionary.txt', 'r')
	for word in dict_file.readlines():
		word = word.strip('\n')
		crypt_word = fcrypt.crypt(word, salt)
		if(crypt_word == crypt_pass):
			print "[+] Found Password: " + word + "\n"
			return
	print "[-] Password Not Found. \n"

def main():
	pass_file = open('passwords.txt')
	for line in pass_file.readlines():
		user = line.split(":")[0]
		password = line.split(":")[1].strip(" ")
		print "[*] Cracking Password For: " + user +"\n"
		test_pass(password)


main()

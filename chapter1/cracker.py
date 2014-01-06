import fcrypt, hashlib



def test_pass(crypt_pass, encryption):
	dict_file = open('dictionary.txt', 'r')
	for word in dict_file.readlines():
		word = word.strip('\n')
		if(encryption == 'crypt'):
			salt = crypt_pass[0:2]
			crypt_word = fcrypt.crypt(word, salt)
		elif(encryption == 'sha512'):
			crypt_word = hashlib.sha512(word).hexdigest()
		if(crypt_word == crypt_pass):
			print "[+] Found Password: " + word + "\n"
			return
	print "[-] Password Not Found. \n"

def main(encryption):
	pass_file = open('passwords.txt')
	for line in pass_file.readlines():
		user = line.split(":")[0]
		password = line.split(":")[1].strip(" ")
		print "[*] Cracking Password For: " + user +"\n"
		test_pass(password, encryption)


encryption = raw_input("Type of encryption? (crypt or sha512): ")
main(encryption)
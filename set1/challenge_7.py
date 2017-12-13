from Crypto.Cipher import AES

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

# assumes text is already base64 decoded
def decrypt_AES_ECB(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(text)

def test():
	input_file = open('7.txt', 'r').read()
	KEY = "YELLOW SUBMARINE"
	print decrypt_AES_ECB(input_file.decode('base64'), KEY)

test()
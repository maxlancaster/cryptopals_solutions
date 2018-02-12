from Crypto.Cipher import AES
from challenge_9 import pad_to_size

def encrypt_AES_ECB(text, key):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.encrypt(text)

# assumes text is already decoded
def decrypt_AES_ECB(text, key):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.decrypt(text)

def repeating_key_xor(plaintext, key):
	plaintext = list(plaintext)
	key = list(key)
	i = 0
	output = []
	for char in plaintext:
		encoding = str(hex(ord(char) ^ ord(key[i])))[2:] # strip off leading '0x'
		if len(encoding) == 1:
			encoding = '0' + encoding 
		output.append(encoding)
		i += 1
		if i == len(key):
			i = 0
	output = ''.join(output)
	return output

def CBC_encrypt(plaintext, IV, key):
	output = []
	chunked_plaintext = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
	for chunk in chunked_plaintext:
		if len(chunk) != 16:
			chunk = pad_to_size(chunk, 16)
		xor = repeating_key_xor(chunk, IV).decode('hex')
		encrypted = encrypt_AES_ECB(xor, key)
		output.append(encrypted)
		IV = encrypted
	return ''.join(output)

def CBC_decrypt(ciphertext, IV, key):
	output = []
	chunked_ciphertext = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
	for chunk in chunked_ciphertext:
		if len(chunk) != 16:
			chunk = pad_to_size(chunk, 16)
		decrypted = decrypt_AES_ECB(chunk, key)
		xor = repeating_key_xor(decrypted, IV)
		output.append(xor)
		IV = chunk
	return ''.join(output)

KEY = "YELLOW SUBMARINE"
IV = '\x00\x00\x00'
input_file = open('10.txt', 'r').read()
input_file = input_file.decode('base64')

decrypted = CBC_decrypt(input_file, IV, KEY).decode('hex')
print decrypted
encrypted = CBC_encrypt(decrypted, IV, KEY)
if encrypted != input_file:
	raise Exception("encryption failed")
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '}

# helper function to count the number of alpha characters in the resulting xor
def score(str):
	score = 0
	for char in str:
		if char.lower() in alphabet:
			score += 1
	return score

def single_byte_xor_decipher(decoded):
	results = []
	for char in xrange(0,256):
		xor_result = []
		for s in decoded:
			xor_result.append(chr(ord(s) ^ char)) # perform the xor
		xor_result = ''.join(xor_result)
		xor_score = score(xor_result) # score the xor
		results.append((xor_result, xor_score, chr(char))) 
	return max(results, key=lambda x: x[1])#[0] # pick the xor with the highest score

def test():
	hex_in = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	decoded = hex_in.decode('hex')
	print single_byte_xor_decipher(decoded)

test()
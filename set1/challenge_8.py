from challenge_7 import decrypt_AES_ECB

# returns the ciphertext which has most likely been encrpyed with ECB
def detect_AES_ECB(input_file):
	ciphertexts = input_file.split('\n')
	# for now, we'll guess that the chunk size is 16 bytes
	# if this doesn't work, we'll have to try 24 and 32 bytes as well
	CHUNK_SIZE = 16
	# this represents the number of unique chunks in the least likely ciphertext chunk
	# (where none of the 16-byte chunks are repeated)
	best = ("", len(ciphertexts[0])/float(CHUNK_SIZE))

	for cphrtxt in ciphertexts:
		seen_ciphertexts = {}
		chunks = [cphrtxt[x:x+CHUNK_SIZE] for x in range(0, len(cphrtxt), CHUNK_SIZE)] # split into chunks
		for chunk in chunks:
			if chunk in seen_ciphertexts:
				seen_ciphertexts[chunk] += 1
			else:
				seen_ciphertexts[chunk] = 1
		if len(seen_ciphertexts) < best[1]:
			best = (cphrtxt, len(seen_ciphertexts))
	return best[0]


def test():
	input_file = open('8.txt', 'r').read()
	print  "the cipher text that has most likely been encrypted with ECB is", detect_AES_ECB(input_file)

test()
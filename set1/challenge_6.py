def compute_hamming_distance(str1, str2):
	str1_b = ''.join(format(ord(x), 'b').zfill(8) for x in str1)
	str2_b = ''.join(format(ord(x), 'b').zfill(8) for x in str2)
	return sum(x1 != x2 for (x1, x2) in zip(str1_b, str2_b))

def break_repeating_key_xor(plaintext):
	KEYSIZE = 2

def test():
	input_file = open('6.txt', 'r')
	print compute_hamming_distance("this is a test", "wokka wokka!!!")

test()
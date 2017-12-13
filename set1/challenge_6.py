import challenge_5
import challenge_3
import base64
import itertools

def compute_hamming_distance(str1, str2):
	str1_b = ''.join(format(ord(x), 'b').zfill(8) for x in str1)
	str2_b = ''.join(format(ord(x), 'b').zfill(8) for x in str2)
	return sum(x1 != x2 for (x1, x2) in zip(str1_b, str2_b))

def break_repeating_key_xor(plaintext):
	decoded = plaintext.decode('base64')
	normalized_edit_distances = []
	for keysize in xrange(2, 41):
		distances = []
		first = decoded[:keysize]
		second = decoded[keysize:2*keysize]
		third = decoded[2*keysize:3*keysize]
		fourth = decoded[3*keysize:4*keysize]
		edit_distance = compute_hamming_distance(first, second)
		edit_distance += compute_hamming_distance(second, third)
		edit_distance += compute_hamming_distance(third, fourth)
		normalized = float(edit_distance)/(3*keysize)
		normalized_edit_distances.append((keysize, normalized))
	probable_keysizes = sorted(normalized_edit_distances, key=lambda x: x[1])[:3] # proceed with 3 smallest edit distances
	print probable_keysizes
	for keysize in probable_keysizes:
		keysize = keysize[0]
		chunks = [decoded[i:i+keysize] for i in range(0, len(decoded), keysize)]
		transposed_chunks = [''.join(list(x)) for x in list(itertools.izip_longest(*chunks, fillvalue="0"))]
		print ''.join([challenge_3.single_byte_xor_decipher(chunk)[2] for chunk in transposed_chunks])

def test():
	input_file = open('6.txt', 'r').read()
	break_repeating_key_xor(input_file)

test()
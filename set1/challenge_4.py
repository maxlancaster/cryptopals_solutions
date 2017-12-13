import challenge_3

def crack_singlechar_xor(file):
	list_of_bests = []
	for line in file:
		line = line.strip()
		list_of_bests.append(challenge_3.single_byte_xor_decipher(line.decode('hex'))[0])

	score = 0
	best = ''
	for i in list_of_bests:
		this_score = challenge_3.score(i)
		if this_score > score:
			score = this_score
			best = i
	return best

def test():
	input_file = open('4.txt', 'r')
	print crack_singlechar_xor(input_file)

test()
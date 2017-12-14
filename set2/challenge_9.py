def pad_to_size(to_be_padded, size):
	if len(to_be_padded) > size:
		raise ValueError("input {} is larger than the desired pading size: {}".format(to_be_padded, size))
	else:
		PAD = "\x04"
		padded = to_be_padded + PAD*(size - len(to_be_padded))
	return padded

def test():
	print pad_to_size("YELLOW SUBMARINE", 20)

test()

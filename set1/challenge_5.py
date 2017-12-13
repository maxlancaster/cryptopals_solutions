import pytest

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

def test():
	plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	expected_result = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
	actual_result = repeating_key_xor(plaintext, "ICE")
	assert expected_result == actual_result, "expected " + expected_result + " got " + actual_result

test()
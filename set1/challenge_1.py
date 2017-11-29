import pytest
import base64

def hex_to_base64(hex):
	return base64.b64encode(hex.decode("hex"))

def test():
	hex_in = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	base_64_out = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
	assert hex_to_base64(hex_in) == base_64_out, "expected " + base_64_out + ", got " + hex_to_base64(hex_in)

test()
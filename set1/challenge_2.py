import pytest
from challenge_1 import *

def fixed_xor(buff1, buff2):
	return "".join(chr(ord(x) ^ ord(y)) for x,y in zip(buff1, buff2)).encode("hex")

def test():
	buff1 = "1c0111001f010100061a024b53535009181c"
	buff2 = "686974207468652062756c6c277320657965"
	xor_result = "746865206b696420646f6e277420706c6179"
	buff1_hex = buff1.decode("hex") # hex decode buffers
	buff2_hex = buff2.decode("hex")
	assert fixed_xor(buff1_hex, buff2_hex) == xor_result, "expected " + xor_result + ", got " + fixed_xor(buff1_hex, buff2_hex)

test()
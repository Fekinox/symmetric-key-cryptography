# Stream Cipher

import random

def encode(character):
	# If character is uppercase...
	if 'A' <= character and character <= 'Z':
		return ord(character) - 0x40
	# If character is lowercase...
	elif 'a' <= character and character <= 'z':
		return ord(character) - 0x60
	# Catch-all
	else: return 27

def decode(number):
	# Convert the number back into a letter
	return chr(number+0x40) if number in range(1,26) else '-'

def genRandomList(seed):
    nums = list(range(1,27))
    random.seed(seed)
    random.shuffle(nums)
    return nums

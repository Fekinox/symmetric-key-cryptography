# Stream-style Encryption

import random

# Encode letters as numbers, and convert back. Anything else is converted to the null case, 27.

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

def encodeString(string):
	return [encode(c) for c in string]

def decodeString(string):
	res = ""
	for n in string:
		res += decode(n)
	return res

# Generates a randomized list. If called with the same key value, will return the same list- this is important

def genRandomList(seed):
    nums = list(range(1,28))
    random.seed(seed)
    random.shuffle(nums)
    return nums

# Maps each encoded number to each number in the list, and back.

def encrypt(key, string):
	print("Your plaintext:", string)
	encodedString = encodeString(string)
	print("Encoded string:", encodedString)
	randlist = genRandomList(key)
	encryptedString = [randlist[i-1] for i in encodedString]
	print("Encrypted string:", encryptedString)
	decodedString = decodeString(encryptedString)
	print("Decoded string:", decodedString)

def decrypt(key, string):
	print("Your plaintext:", string)
	encodedString = encodeString(string)
	print("Encoded string:", encodedString)
	randlist = genRandomList(key)
	decryptedString = [randlist.index(i)+1 for i in encodedString]
	print("Decrypted string:", decryptedString)
	decodedString = decodeString(decryptedString)
	print("Decoded string:", decodedString)

# Symmetric Key Crytography Project

# These functions encode letters as numbers. Case-insensitive. Any foreign characters or spaces are converted to the null case, 27.

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
	return chr(number+0x40) if number is not 27 else '-'

# This function splits text into identical-sized blocks.

def intoBlocks(blocksize, target):
	# List of blocks
	blocklist = []
	# While there's still string data left
	while target is not "":
		# Split the string into a block and the rest of the string. With a blocksize of three, this splits
		# "Hello World" into "Hel" and "lo World".
		(block, rest) = (target[0:blocksize],target[blocksize:len(target)])
		# Add the block to the list and remove the block from the target string
		blocklist.append(block)
		target = rest
	# Return the list
	return blocklist

# These function encode and decode blocks of text.

def encodeBlock(blocksize, block):
	res = 0
	offset = blocksize-1
	for idx in range(0,blocksize):
		res += (encode(block[idx]) if idx < len(block) else 27) * pow(100, offset) 
		offset -= 1
	return res

def decodeBlock(block):
	res = ""
	while block is not 0:
		character = block % 100
		res = decode(character) + res
		block = block // 100
	return res

# Modular addition

# These ciphers encrypt and decrypt blocks of encoded values.
# They use modular addition, which calculates A + K (mod M)
# The value can be decrypted by doing A - K (mod M), but
# this can also be stated as A + (M - K) (mod M), in other
# words encrypting with the modular complement of the key.

def additionencryptBlocks(key, modulus, blocks):
	cipherblocks = [(block + key) % modulus for block in blocks]
	return cipherblocks

def additiondecryptBlocks(key, modulus, blocks):
	inverse = modulus - key
	return encryptBlocks(inverse, modulus, blocks)

# Modular multiplication

# This takes advantage of these two facts:
# n-1 is congruent to -1 mod n
# (n-1)^2 is congruent to (-1)^2 or 1 mod n
# which makes n-1 the modular multiplicative inverse of
# itself. We can use this to encrypt and decrypt information,
# using the modulus as the key.

def multiplicationencryptBlocks(modulus, blocks):
	cipherblocks = [block * (modulus) for block in blocks]

def multiplicationdecryptBlocks(modulus, blocks):
	return multiplicationencryptBlocks(modulus, blocks)

# Modular exponentiation

# No decryption function is defined because it requires computation
# of the discrete logarithm... which is kind of out of the scope
# of this project.

def exponentiationencryptBlocks(key, modulus, blocks):
	cipherblocks - [pow(block, key, modulus) for block in blocks]
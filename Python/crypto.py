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

def additionencryptBlocks(key, modulus, blocks):
	cipherblocks = []
	for block in blocks:
		cipherblocks += ((block + key) % modulus)
	return cipherblocks

def additiondecryptBlocks(key, modulus, blocks):
	# Subtracting in modular addition is the same as adding its modular complement.
	inverse = modulus - key
	return encryptBlocks(inverse, modulus, blocks)

def 
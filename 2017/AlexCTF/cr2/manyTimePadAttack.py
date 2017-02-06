#!/usr/bin/env python 

#Original code: https://github.com/Jwomers/many-time-pad-attack/blob/master/attack.py
import string
import collections
import sets

# XORs two string
def strxor(a, b):     # xor two strings (trims the longer input)
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

# 10 unknown ciphertexts (in hex format), all encrpyted with the same key

c1 = "0529242a631234122d2b36697f13272c207f2021283a6b0c7908"
c2 = "2f28202a302029142c653f3c7f2a2636273e3f2d653e25217908"
c3 = "322921780c3a235b3c2c3f207f372e21733a3a2b37263b313012"
c4 = "2f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d"
c5 = "283f652c2b31661426292b653a292c372a2f20212a316b283c09"
c6 = "29232178373c270f682c216532263b2d3632353c2c3c2a293504"
c7 = "613c37373531285b3c2a72273a67212a277f373a243c20203d5d"
c8 = "243a202a633d205b3c2d3765342236653a2c7423202f3f652a18"
c9 = "2239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c"
c10 = "263e203d63232f0f20653f207f332065262c3168313722367918"
key = "2f2f372133202f142665212637222220733e383f2426386b"

ciphers = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
# The target ciphertext we want to crack
target_cipher = key

# To store the final key
final_key = [None]*1000
# To store the positions we know are broken
known_key_positions = set()

# For each ciphertext
for current_index, ciphertext in enumerate(ciphers):

	counter = collections.Counter()
	# for each other ciphertext
	for index, ciphertext2 in enumerate(ciphers):
		if current_index != index: # don't xor a ciphertext with itself
			for indexOfChar, char in enumerate(strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))): # Xor the two ciphertexts
				# If a character in the xored result is a alphanumeric character, it means there was probably a space character in one of the plaintexts (we don't know which one)
				if char in string.printable and char.isalpha(): counter[indexOfChar] += 1 # Increment the counter at this index
	knownSpaceIndexes = []

	# Loop through all positions where a space character was possible in the current_index cipher
	for ind, val in counter.items():
		# If a space was found at least 7 times at this index out of the 9 possible XORS, then the space character was likely from the current_index cipher!
		if val >= 7: knownSpaceIndexes.append(ind)
	#print knownSpaceIndexes # Shows all the positions where we now know the key!

	# Now Xor the current_index with spaces, and at the knownSpaceIndexes positions we get the key back!
	xor_with_spaces = strxor(ciphertext.decode('hex'),' '*1000)
	for index in knownSpaceIndexes:
		# Store the key's value at the correct position
		final_key[index] = xor_with_spaces[index].encode('hex')
		# Record that we known the key at this position
		known_key_positions.add(index)

# Construct a hex key from the currently known key, adding in '00' hex chars where we do not know (to make a complete hex string)
final_key_hex = ''.join([val if val is not None else '00' for val in final_key])
# Xor the currently known key with the target cipher
output = strxor(target_cipher.decode('hex'),final_key_hex.decode('hex'))
# Print the output, printing a * if that character is not known yet
print 'FLAG:'
print ''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)])

'''
Manual step
'''
# From the output this prints, we can manually complete the target plaintext from:
# The secuet-mes*age*is: Wh** usi|g **str*am cipher, nev***use th* k*y *ore than onc*
# to:
# The secret message is: When using a stream cipher, never use the key more than once

# We then confirm this is correct by producing the key from this, and decrpyting all the other messages to ensure they make grammatical sense
target_plaintext = "ncryption scheme always." #???
print target_plaintext
key = strxor(target_cipher.decode('hex'),target_plaintext)
print(key)
for cipher in ciphers:
	print strxor(cipher.decode('hex'),key)

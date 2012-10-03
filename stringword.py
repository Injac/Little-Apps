#This will encode and decode a string as numbers
#Chunks of letters have unique values and so the overall number of bytes is reduced
#This isn't an effective method of compression but it works

import struct

def wordAsNumber(word):
	value = 0
	index = len(word) - 1
	for c in word:
		cInt = ord(c) - 64
		if (c == ' ') :  cInt = 27
		value += cInt * (28 ** index)
		index -= 1
	return value

def numberAsWord(value):
	original = ""
	while (value > 0):
		char = chr(64 + (value % 28))
		if (value % 28 == 27 or value % 28 == 0) : char = ' '
		original = char + original
		value -= value % 28
		value /= 28
	return original

def splitListToChunks(list, size):
	return [list[i:i+size] for i in range(0, len(list), size)]

def stringAsWords(string):
	return splitListToChunks(string, 6)

def convertToCorrectStyle(string):
	string = string.upper()
	newString = ""
	for c in string:
		if ord(c) >= 65 and ord(c) <= 90: newString += c
		else: newString += ' '
	return newString

def compressToString(integerList):
	all = "";
	for n in integerList: all += struct.pack("I", n)
	return all

def decode(stringEncoded):
	original = ""
	bytes = bytearray(stringEncoded)
	ints = []
	for n in range(0, len(bytes), 4):
		val = int(bytes[n + 3]) * 256 * 256 * 256
		val += int(bytes[n + 2]) * 256 * 256
		val += int(bytes[n + 1]) * 256
		val += int(bytes[n])
		ints.append(val)
	for i in ints: original += numberAsWord(i)
	return original

def encode(string):
	string = convertToCorrectStyle(string)
	list = stringAsWords(string)
	numberList = []
	for l in list: numberList.append(wordAsNumber(l))
	return compressToString(numberList)

word = raw_input("Enter string:")
word = encode(word)
print("Encoded: " + word)
word = decode(word)
print("Decoded: " + word)
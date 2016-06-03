"""
Encryption.py

Simple Encryption/Decryption Program

Written by Tyler Hendrick
"""

def main():
	while True:
		enOrDe = input("Enter 1 for Encrypting a message or 2 for Decrypting a message\n")
		if (enOrDe == 1):
			print "Welcome to the Encryption program"
			str = raw_input("Enter your string to be encrypted: ")
			key = raw_input("Enter your integer key: ")
			encStr = encrypt(str, key)
			print "Your encrypted message is: %s" %encStr
		else:
			print "Welcome to the Decryption program"
			str = raw_input("Enter the string to be decrypted: ")
			key = raw_input("Enter your integer key: ")
			decStr = decrypt(str, key)
			print "Your message is: %s" %decStr
		again = raw_input("Do you wan to go again? y or n: ")
		if again.lower() == 'n':
			break
		
def encrypt(st, key):
	alphaDict, numDict = createDict()
	newStr = ""
	for i in st:
		if i.isalpha():
			newNum = (int(alphaDict[i.lower()]) + int(key)) % 26
			j = numDict[newNum]
			newStr += j
		elif i.isdigit():
			newNum = (int(i) + int(key)) % 10
			newStr += str(newNum)
		else:
			newStr += " "
	return newStr
	
def decrypt(st, key):
	alphaDict, numDict = createDict()
	newStr = ""
	for i in st:
		if i.isalpha():
			newNum = (int(alphaDict[i.lower()]) - int (key)) % 26
			j = numDict[newNum]
			newStr += j
		elif i.isdigit():
			newNum = (int(i) - int(key)) % 10
			newStr += str(newNum)
		else:
			newStr += " "
	return newStr
	
def createDict():
	newdict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z':25}
	array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	return newdict, array
	
if __name__ == "__main__":
	main()
#  File: TestCipher.py

#  Description: Program that will encode and decode lowercase text

#  Student Name: Garner Vincent	

#  Student UT EID: GV4353

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 2-3-15

#  Date Last Modified:2-6-15

def vigenere_decode (strng, passwd):
	#create list to append encoded characters to
	decodedWord = []
	#initialize password counter to cycle through passwd
	passwdCount = 0
	#set the passwd max to the length of the passwd, will alow for cycling
	passwdCountMax = len(passwd)
	#loop to go through each character inside of the strng
	for i in range(len(strng)):
		#if there is a space in the strng, encode a space
		if strng[i] == ' ':
			decodedWord.append(' ')
		elif not (97 <= ord(strng[i]) <= 122):
			decodedWord.append(strng[i])
		#if the the strng[num] > passwd[num], use this
		elif (ord(strng[i]) >= ord(passwd[passwdCount])):
			letter = (ord(strng[i]) - ord(passwd[passwdCount])) + 97
			decodedWord.append(chr(letter))
			passwdCount += 1
		else:
			letter = (ord(strng[i]) - 71) - (ord(passwd[passwdCount]) - 97)
			decodedWord.append(chr(letter + 97))
			passwdCount += 1

		#if the password reaches its max value, reset it to 0 so that it cycles
		if passwdCount == passwdCountMax:
			passwdCount = 0

	#return the encoded word in string format
	return (''.join(decodedWord))

def vigenere_encode (strng, passwd):
	#create list to append encoded characters to
	encodedWord = []
	#initialize password counter to cycle through passwd
	passwdCount = 0
	#set the passwd max to the length of the passwd, will alow for cycling
	passwdCountMax = len(passwd)
	#loop to go through each character inside of the strng
	for i in range(len(strng)):
		#if there is a space in the strng, encode a space
		if strng[i] == ' ':
			encodedWord.append(' ')
		elif not (97 <= ord(strng[i]) <= 122):
			encodedWord.append(strng[i])
		#if the encoded letter can be found on the top left diagonal, use the equation below
		elif (((ord(strng[i]) - 97) + (ord(passwd[passwdCount]) - 97) ) > 25 ):
			letter = (ord(strng[i]) - 97 + ord(passwd[passwdCount]) - 97) + 71
			encodedWord.append(chr(letter))
			passwdCount += 1
		#if the encoded letter is in the bottom right diagonal, use the equation below
		else:
			letter = (ord(strng[i]) - 97) + (ord(passwd[passwdCount]))
			encodedWord.append(chr(letter))
			passwdCount += 1
		#if the password reaches its max value, reset it to 0 so that it cycles
		if passwdCount == passwdCountMax:
			passwdCount = 0
	#return the encoded word in string format
	return (''.join(encodedWord))


def substitution_decode(strng):
	#create the plain text and cipher text
	plain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	cipher = [ 'q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']
	
	#decode the plain text
	plainText = []
	for ch in strng:
		if ch == ' ':
			plainText.append(' ')
		elif not ('a' <= ch <= 'z'):
			plainText.append(ch)
		else:
			idx = cipher.index(ch)
			plainText.append(plain[idx])

	return (''.join(plainText))

def substitution_encode(strng):
	#create the plain text and cipher text
	cipher = [ 'q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']
	
	#encode the plain text
	codeWord = []
	for ch in strng:
		if ch == ' ':
			codeWord.append(' ')
		elif not ('a' <= ch <= 'z'):
			codeWord.append(ch)
		else:
			idx = ord(ch) - ord('a')
			codeWord.append(cipher[idx])

	#convert codeWord into a string
	return (''.join(codeWord))

def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

main()




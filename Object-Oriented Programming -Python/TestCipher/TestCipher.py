#  File: TestCipher.py

#  Description: Given a plain text, this program runs a substitution cipher as well as a vigenere cipher in order to encode and decode messages.

#  Student Name: Aasim Rajabali

#  Student UT EID: afr447

#  Partner Name: Shawn Hu

#  Partner UT EID: sh42578

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: February 6th, 2015

#  Date Last Modified: February 7th, 2015

#This function takes a plain text and substitutes a cipher text to form an encoded string
def substitution_encode (line):
    line = list(line)
    alphabet= list('abcdefghijklmnopqrstuvwxyz')
    cipher = list('qazwsxedcrfvtgbyhnujmikolp')
    encoded_str = ''
    for letter in line:
        if letter in alphabet:
            encoded_str += cipher[alphabet.index(letter)]
        else:
            encoded_str += letter
    return encoded_str

#This function works in reverse, in that it takes an encoded string and decodes it into plain text
def substitution_decode (line):
    line = list(line)
    alphabet= list('abcdefghijklmnopqrstuvwxyz')
    cipher = list('qazwsxedcrfvtgbyhnujmikolp')
    decoded_str = ''
    for letter in line:
        if letter in cipher:
            decoded_str += alphabet[cipher.index(letter)]
        else:
            decoded_str += letter
    return decoded_str

def vignerecipher(st, pswd):
    #create a list of letters so they may be interchanged by indices
    #the idea of the algorithm is this: a = 0, b = 1, c = 2... etc.
    #therefore each letter is equivalent to its index in the list
    #the encoded character, expressed as a number, is just the sum of the pass letter and the  decoded letter modulo 26
    letters = list('abcdefghijklmnopqrstuvwxyz')
    #loop traverses the entire string, replacing each character
    counter = 0
    for x in range (len(st)):
        if st[x] not in letters:
            continue
        decodenum = letters.index(st[x])
        #returns the proper letter in the password, noting that the modulus operation effectively cycles the letters in the password
        passletter = pswd[counter % len(pswd)] 
        passnum = letters.index(passletter)
        encodenum = (decodenum + passnum) % 26
        encodeletter = letters[encodenum]
        st = st[0:x] + encodeletter + st[(x + 1): len(st)]
        #because of the placement of this counter, the password only advances a letter if the message has (i.e, the message didn't have a space or punctuation)
        counter += 1
    return st

def reversevignerecipher(st, pswd):
    #create a list of letters so they may be interchanged by indices
    #the idea of the algorithm is this: a = 0, b = 1, c = 2... etc.
    #therefore each letter is equivalent to its index in the list
    #the encoded character, expressed as a number, is just the sum of the pass letter and the  decoded letter modulo 26

    #in this case, instead of adding the password, we just subtract the password.
    letters = list('abcdefghijklmnopqrstuvwxyz')
    #loop traverses the entire string, replacing each character one by one
    counter = 0
    for x in range (len(st)):
        if st[x] not in letters:
            continue
        decodenum = letters.index(st[x])
        #returns the proper letter in the password, noting that the modulus operation effectively cycles the letters in the password
        passletter = pswd[counter % len(pswd)] 
        passnum = letters.index(passletter)
        encodenum = (decodenum - passnum) % 26
        encodeletter = letters[encodenum]
        st = st[0:x] + encodeletter + st[(x + 1): len(st)]
        #because of the placement of this counter, the password only advances a letter if the message has (i.e, the message didn't have a space or punctuation)
        counter += 1
    return st
    
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
  st = in_file.readline()
  st = st.strip()
  pswd = in_file.readline()
  pswd = pswd.strip()


  # print result
  print ("Plain Text to be Encoded: " + st)
  print ("Pass Phrase (no spaces allowed): " + pswd)
  print ("Encoded Text: " + vignerecipher(st, pswd))
  print ()

  # read line to be decoded and pass phrase
  st = in_file.readline()
  st = st.strip()
  pswd = in_file.readline()
  pswd = pswd.strip()

  # print result
  print ("Encoded Text to be Decoded: " + st)
  print ("Pass Phrase (no spaces allowed): " + pswd)
  print ("Decoded Plain Text: " + reversevignerecipher(st, pswd))
  print ()

  # close file
  in_file.close()

main()

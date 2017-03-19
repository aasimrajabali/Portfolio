
#  File: BST_Cipher.py

#  Description: This program encrypts and decrypts strings
#               using a binary search tree.

#  Student Name: Aasim Rajabali

#  Student UT EID: afr447

#  Partner Name: Shawn Hu

#  Partner UT EID: sh42578

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: April 24, 2015

#  Date Last Modified: April 24, 2015

class Node(object):
   def __init__(self, data):
       self.data = data
       self.lChild = None
       self.rChild = None

class Tree(object):
   # note that the tree takes two input parameters. you must be careful when initiating a new tree because
   # if you input only one parameter it will be taken as the root, not as the encryption string
   def __init__(self, root = None, encrypt_str = ''):
       self.root = root
       for ch in encrypt_str:
           self.insert(ch)


   def insert(self, data):
       root = self.root
       # if the tree is empty
       if root == None:
           self.root = Node(data)
           return
       # if the character was found, and is the root:
       if self.search(data) == '':
           return
       # if the character was found
       if self.search(data)[-1] != 'X':
           return
       # if it wasn't found, uses recursion to insert as usual
       if data < root.data:
           if root.lChild == None:
               self.root.lChild = Node(data)
               return
           leftside = Tree(root.lChild)
           leftside.insert(data)
           return
       if data > root.data:
           if root.rChild == None:
               self.root.rChild = Node(data)
               return
           rightside = Tree(root.rChild)
           rightside.insert(data)
           return



   # the search() function will search for a character in the binary
   # search tree and return a string containing a series of lefts
   # (<) and rights (>) needed to reach that character. It will
   # return a blank string if the character does not exist in the tree.
   # It will return * if the character is the root of the tree.
   def search (self, ch):
       root = self.root
       # definitely not found if the tree is empty
       if root == None:
           return 'X'
       # this should be a star, but that convention is tedious
       if root.data == ch:
           return ''
       # adds a necessary character and then performs recursion to get the desired result
       if ch < root.data:
           leftside = Tree(root.lChild)
           return '<' + leftside.search(ch)
       if ch > root.data:
           rightside = Tree(root.rChild)
           return '>' + rightside.search(ch)


   # the traverse() function will take string composed of a series of
   # lefts (<) and rights (>) and return the corresponding
   # character in the binary search tree. It will return an empty string
   # if the input parameter does not lead to a valid character in the tree.
   def traverse (self, st):
       root = self.root
       # st not found. will happen at some level of recursion for sure
       if root == None:
           return ''
       # st is the root, of course
       if st == '*' or st == '':
           return root.data
       # st is in the left side. goes to the left side and searches again
       if st[0] == '<':
           leftside = Tree(root.lChild)
           return leftside.traverse(st[1:])
       #same deal with the right side
       if st[0] == '>':
           rightside = Tree(root.rChild)
           return rightside.traverse(st[1:])


   # the encrypt() function will take a string as input parameter, convert
   # it to lower case, and return the encrypted string. It will ignore
   # all digits, punctuation marks, and special characters.
   def encrypt (self, st):
       encryptedstring = ''
       for ch in st:
           # removes all non-letter/space characters
           if ch in (' abcdefghijklmnopqrstuvwxyz'):
               encodeblock = self.search(ch)
               # because of the annoying requirement that root be represented by a star
               # the search functino does not return a star ordinarily
               if encodeblock == '':
                   encodeblock = '*'
               encryptedstring += encodeblock + '!'
       # removes the last '!' character at the end
       encryptedstring = encryptedstring[0:len(encryptedstring) - 1]

       return encryptedstring

   # the decrypt() function will take a string as input parameter, and
   # return the decrypted string.
   def decrypt (self, st):
       #decodeblock will build the whole string for one character before being emptied
       decodeblock = ''
       decryptedstring = ''
       for ch in st:
           #builds the string up until it reaches the delimiter
           if ch != '!':
               decodeblock += ch
           #once it reaches the delimiter, finds the character and empties the
           if ch == '!':
               newchar = self.traverse(decodeblock)
               decryptedstring += newchar
               decodeblock = ''
       # this last part is necessary since by the (dumb) convention, we had to remove the last delimiter
       newchar = self.traverse(decodeblock)
       decryptedstring += newchar
       return decryptedstring

def main():
    file = open("input.txt")
    s = 0
    while (s < 8):
        key = file.readline()
        key = key.strip()
        encode = file.readline()
        encode = encode.strip()
        decode = file.readline()
        decode = decode.strip()
        skip = file.readline()
        s += 1
        t = Tree(None, key)
        print(t.encrypt(encode))
        print(t.decrypt(decode))
        print()
main()

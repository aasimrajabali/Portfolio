#  File: WordSearch.py

#  Description: Based on a few assumptions about the formatting, will execute a word search for a provided list of words and
#               write the coordinates of the first letters of the found words in an outfile. 

#  Student Name: Shawn Hu, Aasim Rajabali (Pair programming)

#  Student UT EID: sh42578, afr447

#  Course Name: CS 303E 

#  Unique Number: 52705 (Shawn Hu), 52700 (Aasim Rajabali)

#  Date Created: 24 Nov 2014

#  Date Last Modified: 24 Nov 2014

def restofword(word, grid, row, character):
    #checks to see if there is enough room for the word to avoid future index errors
    #they do not have enough room by default
    enoughroomup = False
    enoughroomdown = False
    enoughroomright = False
    enoughroomleft = False
    #if there is, in fact, enough room, the values are changed
    if row - len(word) + 1 >= 0:
        enoughroomup = True
    if row + len(word) + 1 <= len(grid):
        enoughroomdown = True
    if character - len(word) + 1 >= 0:
        enoughroomleft = True
    if character + len(word) + 1 <= len(grid[0]):
        enoughroomright = True
    #if there is enough froom in any case, will execute a loop that checks the string against consecutive values in each direction where there is enough room
    if enoughroomright:
        for x in range (len(word)):
            #check values. if any value fails to coincide, the loop will break
            if word[x] == grid[row][character + x]:
                 found = 'yes'
            else:
                found = 'no'
            if found == 'no':
                break
        # if the values all coincided, we've found the word and can return the correct index
        # otherwise, we will continue until the end, where the default value will be returned
        if found == 'yes':
            return [row + 1, character + 1]
    #each of these blocks is the same as the previous, but for a different direction.
    if enoughroomleft:
        for x in range (len(word)):
            if word[x] == grid[row][character - x]:
                 found = 'yes'
            else:
                found = 'no'
            if found == 'no':
                break
        if found == 'yes':
            return [row + 1, character + 1]
    if enoughroomdown:
        for x in range (len(word)):
            if word[x] == grid[row + x][character]:
                 found = 'yes'
            else:
                found = 'no'
            if found == 'no':
                break
        if found == 'yes':
            return [row + 1, character + 1]
    if enoughroomup:
        for x in range (len(word)):
            if word[x] == grid[row - x][character]:
                 found = 'yes'
            else:
                found = 'no'
            if found == 'no':
                break
        if found == 'yes':
            return [row + 1, character + 1]
    #the diagonal cases are the same, but require enough room in two dimensions and scan moving along both a row and column
    if enoughroomup and enoughroomright:
        for x in range (len(word)):
            if word[x] == grid[row - x][character + x]:
                 found = 'yes'
            else:
                found = 'no'
            if found == 'no':
                break
        if found == 'yes':
            return [row  + 1, character + 1]
    if enoughroomup and enoughroomleft:
        for x in range (len(word)):
            if word[x] == grid[row - x][character - x]:
                 found = 'yes'
            else:
                found = 'no'
            if found == 'no':
                break
        if found == 'yes':
            return [row + 1, character + 1]
    if enoughroomdown and enoughroomright:
        for x in range (len(word)):
            if word[x] == grid[row + x][character + x]:
                 found = 'yes'
            else:
                found = 'no'
            if found == 'no':
                break
        if found == 'yes':
            return [row + 1, character + 1]
    if enoughroomdown and enoughroomleft:
        for x in range (len(word)):
            if word[x] == grid[row + x][character - x]:
                 found = 'yes'
            else:
                found = 'no'
            if found == 'no':
                break
        if found == 'yes':
            return [row + 1, character + 1]
        
    #default value, in case, for example, there is not enough room or if the word is never found      
    return [0,0]
    
    

def searchword(word, grid):
    #default value
    wordfound = [0,0]
    for rownum in range (len(grid)):
        for column in range (len(grid[0])):
            if grid[rownum][column] == word[0]:
                #will search to see if the rest of the word is attached to the first letter
                wordfound = restofword(word, grid, rownum, column)
                #signifies that the word has been found. if the word was not attached to the first character, the loop will continue to iterate
                if wordfound != [0,0]:
                    return wordfound
    #if the word is not found in the grid at all, will return [0,0]
    return wordfound

def main():
    #open files
    infile = open('hidden.txt', 'r')
    outfile = open('found.txt', 'w')
    numbers = infile.readline()
    numbers = numbers.split()
    # assign dimensions based on an assumption about file formatting
    numrows = int(numbers[0])
    numcols = int(numbers[1])
    blank = infile.readline()
    #expresses the grid as a 2d list
    grid = []
    for x in range (numrows):
        line = infile.readline()
        linelist = line.split()
        grid.append(linelist)
    #formatting purposes
    blank = infile.readline()
    numwords = infile.readline()
    numwords = numwords.strip()
    numwords = int(numwords)
    #creates list of words
    wordlist = []
    for x in range (numwords):
        line = infile.readline()
        line = line.strip()
        wordlist.append(line)
    for word in wordlist:
        #searches for each word in the list of words. searchword will return the coordinates as a list, allowing us to extract the coordinates with list functions
        coord = searchword(word, grid)
        #just formatting, justification
        outfile.write (format(word, '<12s') + format(coord[0], '>4d') + format(coord[1], '>4d') + "\n")

        print (format(word, '<12s'), end = '')
        print (format(coord[0], '>4d'), end = '')
        print (format(coord[1], '>4d'), end = '')
        print()
    #close files
    infile.close()
    outfile.close()
    
main()
        

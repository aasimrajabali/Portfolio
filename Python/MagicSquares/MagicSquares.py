#  File: MagicSquare.py

#  Description: This program takes a number of square matrices and confirms whether or not they are magic squares

#  Student Name:Aasim Rajabali

#  Student UT EID: afr447

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: November 12, 2014

#  Date Last Modified: November 12, 2014
import string
def isMagic(a):
    #check dimension of a 2-D list
    n = len(a)
    
    #calculate the canonical sum
    canon_sum = (n * ((n*n)+1)) // 2
    
    #check sum of each row
    for i in range(len(a)):
        sum_row = 0
        for j in range(len(a[0])):
            sum_row += a[i][j]
            
    #check that the sum_row == canon_sum
    if sum_row != canon_sum:
        return 'invalid'
    
    #check the sum of each column
    for j in range(len(a[0])):
        sum_col = 0
        for j in range(len(a)):
            sum_col += a[i][j]
            
    #check that sum_col == canon_sum
    if sum_col != canon_sum:
        return 'invalid'
    
    #check sum of diagonal left to right
    sum_lr = 0
    for i in range(len(a)):
        sum_lr += a[i][i]
        
    #check that sum_lr == canon_sum
    if sum_lr != canon_sum:
        return 'invalid'
    
    #check sum of diagonal right to left
    sum_rl = 0
    for i in range(len(a)):
        sum_rl += a[i][len(a) - 1 - i]
        
    #check sum_rl == canon_sum
    if sum_rl != canon_sum:
        return 'invalid'
    return 'valid'

def main():

    #open file for reading
    in_file = open("squares.txt","r")
    #open file for writing
    out_file = open("results.txt","w")
    #read number of squares, write number into output file
    num_squares = in_file.readline()
    num_squares = num_squares.strip()
    num_squares = int(num_squares)
    out_file.write(str(num_squares) + "\n")
    print(str(num_squares) + "\n")
    
    #process each square separately
    for i in range(num_squares):
        #read blank line
        blank = in_file.readline()
        out_file.write(blank)
        
        #read the dimension of the square
        dim = in_file.readline()
        dim = dim.strip()
        dim = int(dim)

        #create a 2-D list
        a = []
        
        for j in range(dim):
            row = in_file.readline()
            row = row.strip()
            out_file.write(row + "\n")

            #write out matrices into the output file
            b = row.split()
            for k in range(len(b)):
                b[k] = int(b[k])
            a.append(b)
        
        #write the dimension and validity into the output file
        print(dim)
        out_file.write(str(dim) +' '+ str(isMagic(a)))

        for x in range(dim):
            for y in range(dim):
                matrix= str(a[x][y])
                matrix= matrix.ljust(2)
                print(matrix,end=" ")
            print()
        print()
        out_file.write("\n")
        
    #print result message and close files
    print('The output has been written to results.txt')
    in_file.close()
    out_file.close()
main()

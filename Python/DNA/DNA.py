#  File: DNA.py

#  Description: This program compares DNA strings from a file and returns the longest common substring(s) for each pair

#  Student Name: Aasim Rajabali

#  Student UT EID: afr447

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: October 29, 2014

#  Date Last Modified: October 29,2014

import string
#This function returns the longest common substring(s) for each pair
def findSubstr(st1,st2,len1,len2):
    max_len= 0
    match=[]
    for i in range(len1):
        for j in range(len1 - i + 1):
            sub= st1[i:i + j]
            if len(sub) > 1 and st2.find(sub) != -1:
                if len(sub)>max_len:
                    max_len= len(sub)
                    match= [sub]
                elif len(sub)== max_len:
                    match.append(sub)
    if match==[]:
        return('No Common Sequence Found')            
    return (", ".join(match))

def main():
    #open file for reading
    in_file= open("dna.txt","r")
    #read number of pairs
    num_pair= in_file.readline()
    num_pair= num_pair.strip()
    num_pair= int(num_pair)
    number=0
    for pairs in range(num_pair):
        dna1= in_file.readline()
        dna2= in_file.readline()

        dna1= dna1.strip()
        dna2= dna2.strip()
        #find the shorter of the two strands
        if(len(dna1)>len(dna2)):
            st1= str.upper(dna1)
            st2= str.upper(dna2)
        else:
            st1= str.upper(dna2)
            st2= str.upper(dna1)
        len1=len(st1)
        len2=len(st2)
        number+=1
        #print results of longest common substrings
        print('Pair',str(number)+':',findSubstr(st1,st2,len1,len2))
    #close file  
    in_file.close()
main()

            
    

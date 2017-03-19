#  File: Benford.py

#  Description: This program creates a frequency distribution of state
#               populations' starting digits using data from the 2009 Census.    

#  Date Created: November 26,2014

import string
def main():
    #create an emtpy dictionary
    pop_freq={}

    #initialize the dictionary
    pop_freq['1']=0
    pop_freq['9']=0

    #open the file for reading
    infile=open("Census_2009.txt","r")

    #read the header
    header= infile.readline()

    #read subsequent lines
    tot_pop=[]
    for line in infile:
        line=line.strip()
        pop_data=line.split()
        tot_pop.append(pop_data[-1])
     
    #close file
    infile.close()
    
    #process and write output
    print('Digit'+'  ''Count'+'  '+'%')
    for i in range(1,10):
        num_list=[]
        for number in tot_pop:
            if int(number[0])==i:
                num_list.append(number)
                count=len(num_list)
                rel_freq=(len(num_list) / len(tot_pop))*100
                rel_freq=format(rel_freq,'.1f')
                rel_freq=str(rel_freq)
                count=str(count).ljust(7)
        print(str(i).ljust(7)+count+rel_freq)
main()

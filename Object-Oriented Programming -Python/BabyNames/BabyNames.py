#  File: BabyNames.py 

#  Description: This program allows a user to query a data base \
#               of the 1000 most popular baby names in the United States

#  Date Created: March 14, 2015

import string
def Option2(nam,nam_dict,rank):
    if nam in nam_dict:
        rank = ' '.join(rank)
        print(nam+':',rank)
        
        
        
            
def Option1(a, b, c):
    if a in b:
        print()
        idx = c.index(min(c))
        if idx == 0:
            year = '1900'
        elif idx == 1:
            year = '1910'
        elif idx == 2:
            year = '1920'
        elif idx == 3:
            year = '1930'
        elif idx == 4:
            year = '1940'
        elif idx == 5:
            year = '1950'
        elif idx == 6:
            year = '1960'
        elif idx == 7:
            year = '1970'
        elif idx == 8:
            year = '1980'
        elif idx == 9:
            year = '1990'
        elif idx == 10:
            year = '2000'
        print('The matches with their highest ranking decade are:')
        print(a+' '+year)
    
   
def main():
    #create an emtpy dictionary and list to store rank values
    nam_dict = {}
    #initialize the dictionary
    nam_dict['0'] = 1001
    #open the file for reading
    infile = open("names.txt",'r')
    #read lines
    for line in infile:
        line = line.strip()
        nam_data = line.split()
        #assign a variable to the name of the baby
        names = nam_data[0]
        rank = nam_data[1:]
        #assign the names to be the key and the rankings to be the values
        if names in nam_dict:
            nam_dict[names].append(rank)
        else:
            new_list = []
            new_list.append(rank)
            nam_dict[names] = new_list
            
    print('Options:')
    
    #create a loop in which you display the menu choices
    for i in range(8):
        j = str(i)
        begin = str('Enter ' + j + ' to ')
        if i==1:
            print(begin + 'search for names.')
        elif i==2:
            print(begin + 'display data for one name.')
        elif i==3:
            print(begin + 'all names that appear in only one decade.')
        elif i==4:
            print(begin + 'all names that appear in all decades.')
        elif i==5:
            print(begin + 'all names that are more popular in every decade.')
        elif i==6:
            print(begin + 'all names that are less popular in every decade.')
        elif i==7:
            print(begin + 'quit.')
            
    print()
    num = input('Enter choice: ')
    if num == '1':
        nam = input('Enter a name: ')
        Option1(nam,nam_dict,rank)
    elif num == '2':
        nam = input('Enter a name: ')
        Option2(nam,nam_dict,rank)
        
        
    
   
    
main()

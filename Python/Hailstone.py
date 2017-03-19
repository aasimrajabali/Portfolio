#  File: Hailstone.py

#  Description: This program runs the Hailstone Sequence to verify any
#               starting number converges to 1.

#  Date Created: October 10, 2014

def main():
    #Prompt user to enter two range values, with start being the lowest value
    start= eval(input('Enter starting number of the range:'))
    last= eval(input('Enter ending number of the range:'))
    while(start<=0 or last<=0) or (last <= start):
        print('Ranges are invalid. Please enter again.')
        start= eval(input('Enter starting number of the range:'))
        last= eval(input('Enter ending number of the range:'))
        
    #Generate the Hailstone Sequence for the given range
    max_length= 0
    max_num= 0
    for i in range(start, (last + 1)):
        cycle_length = 0 
        num = i 
        while (num > 1):
            if (num%2 == 0):
                num= (num // 2)
                cycle_length += 1
            else:
                num=(3 * num + 1)
                cycle_length += 1
            if(num==1):
                cycle_length= cycle_length 
        if(cycle_length >= max_length):
            max_length = cycle_length
            max_num = i
    max_length= str(max_length)
            
    #Print result of the Hailstone Sequence
    print('The number', max_num, 'has the longest cycle length of', max_length + '.')     
main()

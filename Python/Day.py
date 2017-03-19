
#  File: Day.py

#  Description: This program prompts the user to enter a date and prints out the day of the week for that specific date.

#  Student Name: Aasim Rajabali

#  Student UT EID: afr447

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: September 27, 2014

#  Date Last Modified: September 27, 2014
def main():
    #Prompt user to enter the year, month, and day
    year= eval(input('Enter year:'))
    c= year % 100
    d= year // 100
    while (year<1900 or year>=2100):
        year= eval(input('Enter correct year:'))
    mon= eval(input('Enter month:'))
    if mon>=3:
        a= mon-2
    if mon<3:
        a=mon+10
        if (a==11 or a==12) and (1900<=year<2000):
            c= (year-1)-1900
        elif (a==11 or a==12) and (2000<=year<2100):
            c=(year-1)-2000
    while (mon<1 or mon>12):
        mon=eval(input('Enter correct month:'))
    b=eval(input('Enter Day:'))
    if (mon==1 or mon==3 or mon==5 or mon==7 or mon==8 or mon==10 or mon==12):
        while(b<1 or b>31):
            b=eval(input('Enter Correct Day:'))
    elif(mon==4 or mon==6 or mon==9 or mon==11):
        while(b<1 or b>30):
            b=eval(input('Enter Correct Day:'))
    elif mon==2 and ((year%4==0 and year%100!=0) or (year%400==0)):
        while(b<1 or b>29):
            b=eval(input('Leap.Enter Correct Day:'))
    elif mon==2:   
        while(b<1 or b>28):
            b=eval(input('Enter Correct Day:'))
    #Compute quantities using Rev. Zeller's Algorithm:
    w = (13 * a - 1 ) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7
    if r==0:
        r= str('Sunday')
    if r==1:
        r= str('Monday')
    if r==2:
        r= str('Tuesday')
    if r==3:
        r= str('Wednesday')
    if r==4:
        r= str('Thursday')
    if r==5:
        r= str('Friday')
    if r==6:
        r= str('Saturday')
    #Print day represented in days of the week
    print('The day is', r + '.')
main()
    
  

    
    

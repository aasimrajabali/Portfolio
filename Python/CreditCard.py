#  File: CreditCard.py

#  Description: This program tests whether a 15 or 16-digit credit card is valid
#               through Luhn's Algoritm, and then determines the type of credit card

#  Student Name: Aasim Rajabali

#  Student UT EID: afr447   

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created: October 20, 2014

#  Date Last Modified: October 20, 2014

#This function checks if a credit card number is valid

def is_valid(cc_num):
    #Check if card is valid by number of digits
    if(cc_num<100000000000000 or cc_num>=10000000000000000):
        return('Not a 15 or 16-digit number')
    cc_string= str(cc_num)
    sum_odd=0
    sum_even=0
    #Use Luhn's Algoriithm to test validity of a 15 or 16-digit number
    if (len(cc_string)==16):
        for i in range (0,16,2):
            odd_digits=cc_string[i]
            product_sum= (int(odd_digits)*2)
            if product_sum >= 10:
                digit_1= product_sum // 10
                digit_2= product_sum % 10
                product_sum= digit_1 + digit_2             
            sum_odd += product_sum
        for i in range (1,16,2):
            even_digits=cc_string[i]
            sum_even += int(even_digits)
        total= sum_even + sum_odd
        if(total % 10 != 0):
            return ('Invalid credit card number ')
       

    if (len(cc_string)==15):
        for i in range (0,15,2):
            even_digits=cc_string[i]
            sum_even += int(even_digits)
        for i in range (1,15,2):
            odd_digits=cc_string[i]
            product_sum= (int(odd_digits)*2)
            if product_sum >= 10:
                digit_1= product_sum // 10
                digit_2= product_sum % 10
                product_sum= digit_1 + digit_2             
            sum_odd += product_sum
        total= sum_even + sum_odd
        if(total % 10 != 0):
            return ('Invalid credit card number ')
        
#This function returns the type of credit card

def cc_type(cc_num):
    cc_string= str(cc_num)
    cc_num= int(cc_string)
    if int(cc_string[0])==4:
        return ('Visa')
    elif int(cc_string[:2])==37 or int(cc_string[:2])==34:
        return ('American Express')
    elif int(cc_string[:4])==6011 or int(cc_string[:3])==644 or int(cc_string[:2])==65:
        return ('Discover')
    elif int(cc_string[:2])==50  or int(cc_string[:2])==51 or int(cc_string[:2])==52 or int(cc_string[:2])==53 or int(cc_string[:2])==54 or int(cc_string[:2])==55:
        return ('MasterCard')
    else:
        return str()
          
#The main function prints if the card is valid    

def main():
    cc_num=int(input('Enter a 15 or 16-digit credit card number:'))
    if(is_valid(cc_num)):
        print(is_valid(cc_num))
        return
    print()
    print('Valid', (cc_type(cc_num)),'credit card number')
main()
    


    
    
        
    
    

            

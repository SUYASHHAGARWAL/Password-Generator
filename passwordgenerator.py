import random

print("\t\tPASSWORD GENERATOR")
'''
Here we have stored all the alphabets in list 'char', all numbers in list 'num' and 
symbols in list 'sym', We will use random to randomly select entries from these lists 
and append it to our main password list.
'''

char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num=['1','2','3','4','5','6','7','8','9','0']
sym=['@','!','#','$','%','^','&','*','(',')']

'''
In this project we will take the number of characters, symbols and integers from the user 
tjay they want in their password.
'''
n=int(input("Enter number of alphabets you want in your password "))
no=int(input("Enter number of integers you want in your password: "))
ns=int(input("Enter number of symbols you want in your password: "))


p=[]       
#creating empty list to store selected entities. 


for c in range(0,n):
    p+=random.choice(char)      
    #append/add random character in p list.

for c in range(0,no):
    p+=random.choice(num)       
    #append/add random numbers in p list.

for c in range(0,ns):
    p+=random.choice(sym)       
    #append/add random symbols in p list.


password=""     
#creating an empty string to randomly collect all elements from list and store in password.
for l in p:
    password+=l
print(f"Your password is {password}")
import random
char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num=['1','2','3','4','5','6','7','8','9','0']
sym=['@','!','#','$','%','^','&','*','(',')']
n=int(input("Enter number of alphabets you want in your password "))
no=int(input("Enter number of integers you want in your password: "))
ns=int(input("Enter number of symbols you want in your password: "))
p=[]
for c in range(0,n):
    p+=random.choice(char)
for c in range(0,no):
    p+=random.choice(num)
for c in range(0,ns):
    p+=random.choice(sym)
password=""
for l in p:
    password+=l
print(f"Your password is {password}")
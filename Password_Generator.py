import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/']

print("Wlcome to the PyPassword Generator !")
letters=int(input("How many letters do you want in your password ? "))
symbol=int(input("How many symbols do you want in your password ? "))
num=int(input("How many numbers do you want in your password ? "))
# easy level

# password=""
# for char in range(1,num+1):
#     password+=random.choice(small_letters)
# for char in range(1,symbol+1):
#     password+=random.choice(s_symbols)
# for char in range(1,num+1):
#     password+=random.choice(digits)
    
# print(password)

password_list=[]
for char in range(1,num+1):
    password_list+=random.choice(small_letters)
for char in range(1,symbol+1):
    password_list+=random.choice(s_symbols)
for char in range(1,num+1):
    password_list+=random.choice(digits)

random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(password)
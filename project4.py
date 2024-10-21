import random
print("what do you choose ? 0 for rock , 1 for paper or 2 for scissors : ")
user_input=int(input("Please enter choose : "))
print("your choice")
if user_input ==0:
    print("rock")
elif user_input==1:
    print("paper")  
else:
    print("scissors")

random_integer=random.randint(0,2)
print(random_integer)
print("computer choice ")
if random_integer ==0:
    print("rock")
elif random_integer==1:
    print("paper")  
else:
    print("scissors")

if user_input==0 and random_integer==2:
    print("you win")
elif user_input==2 and random_integer==1:
    print("you win")
elif user_input==2 and random_integer==0:
    print("you win")
elif user_input==0 and random_integer==0:
    print("Tie...")
elif user_input==1 and random_integer==1:
    print("tie")
elif user_input==2 and random_integer==2:
    print("tie")
else:
    print("computer wins")

# # 
# 0 1 2

# 00 11 22
# 01 02
# 10 12
# 20 21
# # 
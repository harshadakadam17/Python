

print("Welcome to tresure island.your missioon is to find the trsure")
direction=input("Left or Right ?")
if direction=='left'or direction=='Left':
    instruction1=input("Swim or Wait :")
    if instruction1=='Swim'or instruction1=='swim':
        print("game over")

    else:
        dooor=input("Select door Red or Blue or yellow :")
        if dooor=='Yellow'or dooor=='yellow':
            print("you win")
        else:
            print("game over")   
else:
    print("Game over")
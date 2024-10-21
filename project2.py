print("Welcome to tip calculator !")
bill=float(input("What was the total bill : "))
tipammount=int(input("how much tip would you like to give 10,20, or 15 : "))
splitthebill=int(input("How many people would you like to split the bill :"))
tip=tipammount*bill/100
divide=bill+tip/splitthebill
print(f"Each person should pay : {divide}")
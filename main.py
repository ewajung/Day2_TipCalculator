print ("*** TIP CALCULATOR ***\n\n")
print("Welcome to the tip calculator!")
bill = float(input("What was a total bill? $"))
tip = int(input("How much tip would you like to give: 10, 12, 15? "))
people = int(input ("How many people to split the bill? "))
calculate = bill * (tip/100 + 1) / people
print(f"Each person should pay: ${round(calculate,2)}")


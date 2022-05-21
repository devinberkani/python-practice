print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip /= 100
numOfPeople = int(input("How many people to split the bill? "))
result = round(((bill + (bill * tip)) / numOfPeople), 2)
result = '{:.2f}'.format(result)
print(f"Each person should pay: ${result}")
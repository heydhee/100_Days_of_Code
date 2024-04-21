print("Welcome to Tip Calculator")
bill=float(input("Enter the bill amount"))
interest=int(input("What percentage of tip would you like to give? 10, 12 or 15? "))
ppl=int(input("How many people should split the bill"))
tip = (bill + ((interest/100)*bill))/ppl
print(f"Each person should pay: {tip}")


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 , or 15? "))
people_split = int(input("How many people to split the bill? "))

total_percentage_tip = percentage_tip / 100
total_tip_amount = bill * total_percentage_tip
total_bill = bill + total_tip_amount

result = total_bill / people_split
round(result, 2)
print(f"Each person should pay: ${result}")
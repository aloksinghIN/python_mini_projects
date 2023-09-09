print("Welcome to the tip calculator!\n")
total_bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people_count = int(input("How many people to split the bill?\n"))

bill_with_tip = total_bill*(1+tip/100)
bill_per_person = round(bill_with_tip/people_count,2)
print(f"Each person should pay: ${bill_per_person}")
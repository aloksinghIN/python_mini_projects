print("Welcome to the tip calculator!\n")
total_bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people_count = int(input("How many people to split the bill?\n"))

bill_with_tip = total_bill*(1+tip/100)
bill_per_person = round(bill_with_tip/people_count,2)
# print("{:.2f}".format(round(a, 2)))
print("Each person should pay: ${:.2f}".format(bill_per_person))
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
total_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

each_person_to_pay = (total_bill * (1 + total_tip / 100)) / no_of_people
print(f"Each person to pay: ${each_person_to_pay:.2f}")

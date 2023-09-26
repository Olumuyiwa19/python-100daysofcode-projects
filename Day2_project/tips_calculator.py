#display a welcome message to the user
print("Welcome to Tips Calculator app")

#prompt user to input the bill amount, follow by number of people to share the bill with, also get their desired Tips percentage
bill_amount = float(input("Enter the actual bill amount here: $"))
number_people = int(input("Specify the number of people to share the bill here: "))
tip_percent = float(input("Specify the percentage of the tips here: "))

#calcu the tip amount
tip_amount = bill_amount * (tip_percent / 100)

#calcu total bill
total_bill = bill_amount + tip_amount

#calcu share of the bill per person
individual_bill = total_bill / number_people

#display the total_bill and individual bill_amount
print(f"total_bill is ${total_bill:.2f}, and the individual bill is ${individual_bill:.2f}")

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill_total = float(input("What was the total bill?\n"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15?\n")) / 100
num_of_people = int(input("How many of you are splittng the bill?\n"))
total_with_tip = bill_total + (tip_percentage * bill_total)
amount_to_pay_per_person = total_with_tip / num_of_people
print(f"Each person should pay £{amount_to_pay_per_person:.2f}")

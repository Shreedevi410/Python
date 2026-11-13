print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill?"))
tip_bill = int(input("How much tip would you like to give? 10, 12 or 15"))
total_people = int(input("How many people to split the bill"))
print(f"Total Bill: {total_bill}")
print(f"Tip Bill: {tip_bill}")
print(f"Total People: {total_people}")
split_per_person = (total_bill + (tip_bill / 100 * total_bill)) /total_people

print(split_per_person)

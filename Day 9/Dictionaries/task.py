student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for score in student_scores:
    score_value = student_scores[score]
    if int(score_value > 90 and score_value <= 100):
        student_grades[score] = "Outstanding"
    elif int(score_value > 80 and score_value <= 90):
        student_grades[score] = "Exceeds Expectations"
    elif int(score_value > 70 and score_value <= 80):
        student_grades[score] = "Acceptable"
    else:
        student_grades[score] = "Fail"

print(student_grades)
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
# Retrieving a value from a dictionary
print(programming_dictionary["Function"])

# Adding more items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
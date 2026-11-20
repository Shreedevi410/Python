import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
length_chosen_word = len(chosen_word)
for letters in range(length_chosen_word):
    placeholder += "-"
print(placeholder)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


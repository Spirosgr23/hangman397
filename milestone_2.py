import random

# Favorite fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Step 2: Assign this list to a variable called word_list
word_list = fruits

# Step 3: Print out the newly created list
print(word_list)

word = random.choice(word_list)

# Step 5: Print out the randomly chosen word
print(word)

# Take user input
guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
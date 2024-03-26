import random

user_input = input("Press any key to continue or 'q' to quit: ")
if user_input == "q":
    raise SystemExit("Bye!!")

bot_of_range = input("Please enter the min number: ")
top_of_range = input("Please enter the max number: ")
if bot_of_range.isdigit() and top_of_range.isdigit():
    bot_of_range = int(bot_of_range)
    top_of_range = int(top_of_range)

    if bot_of_range <= 0 and top_of_range <= 0:
        print("Please enter valid numbers.")

random_number = random.randint(bot_of_range, top_of_range)
guesses = 0

while True:
    guesses += 1
    guess = input(
        f"Please guess the number in between {bot_of_range} and {top_of_range}: "
    )
    if guess.isdigit():
        guess = int(guess)

    if guess == "q":
        raise SystemExit("Bye!")

    if guess == random_number:
        print(f"You guessed the number! The number is {random_number}.")
        break
    elif guess > random_number:
        print("You are above the number.")
    else:
        print("You are below the number.")

print(f"You guessed the number in {guesses} times.")

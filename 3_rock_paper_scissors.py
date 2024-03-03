import random

user_wins = 0
computer_wins = 0
draw = 0
total_games = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Enter Rock / Paper / Scissors or Q to quit: ").lower()
    if user_pick == 'q':
        break

    if user_pick not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_pick == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        total_games += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        total_games += 1

    elif user_pick == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        total_games += 1

    elif user_pick == computer_pick:
        print("Draw!")
        draw += 1
        total_games += 1

    else:
        print("You lose!")
        computer_wins += 1
        total_games += 1

print("You won: ", user_wins)
print("The computer won: ", computer_wins)
print("Draws: ", draw)
print("Total games: ", total_games)
print("BuuhhhhByeee!")

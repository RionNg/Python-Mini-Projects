print("Welcome to the quiz!")

playing = input("Do you want to play? (Enter y to play):  ")

if playing.lower() != "y":
    print("Bye!")
    quit()

print("Ok! Let's play!")

score = 0

answer = input("What does CPU stand for?:  ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?:  ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for?:  ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for?:  ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

final_score = int((score / 4) * 100)

print("You got " + str(score) + " questions correct!")
print("You got " + str(final_score) + "%!")

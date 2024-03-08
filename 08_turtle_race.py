import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'orange', 'yellow', 'green', 'blue',
          'indigo', 'violet', 'black', 'brown', 'pink']


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 ~ 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric, please try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number of racers (2 ~ 10). Please try again!")


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []

    for i, color in enumerate(colors):
        spacing_x = -WIDTH//2 + (i + 1) * (WIDTH // (len(colors) + 1))
        spacing_y = -HEIGHT//2 + 20
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(spacing_x, spacing_y)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is {winner} turtle!")
time.sleep(5)

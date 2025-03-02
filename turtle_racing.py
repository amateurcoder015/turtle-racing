import turtle
import time
import random

WIDTH , HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'brown', 'cyan', 'yellow', 'black','pink', 'purple']


def get_number_racers():
    racers = 0
    while True:
        racers = input('enter the number of racers (2-10): ')
        if racers.isdigit() and int(racers) >= 2 and int(racers) <= 10:
            return int(racers)
        else:
            print('please enter a valid number between 2 and 10')
            continue

def race(colors):
    turtles = create_turtles(colors) 
    while True:
        for racer in turtles:
            racer.forward(random.randint(1, 20))
            if racer.ycor() >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles=[]
    spacingx = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)* spacingx, -HEIGHT//2 + 20) 
        racer.pendown()
        turtles.append(racer)
    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('turtle racing!')


racers = get_number_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
 
winner = race(colors)
print(f'The winner is: {winner}')

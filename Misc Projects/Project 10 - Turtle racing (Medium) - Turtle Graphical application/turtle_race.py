import turtle       # https://docs.python.org/3/library/turtle.html
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'indigo']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Please enter the number of turtles (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Not a valid number. ', end='')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range. ', end='')

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Awesome Turtle Racing!!')

def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            racer.forward(random.randrange(1, 20))
            _, y = racer.pos()
            if y >= HEIGHT // 2 - 20:
                return colors[turtles.index(racer)]

def main():
    racers = get_number_of_racers()
    init_turtle()

    random.shuffle(COLORS)
    colors = COLORS[:racers]
    
    winner = race(colors)
    print(f'The winner is Turtle with color {winner.upper()}')
    time.sleep(3)



if __name__ == '__main__':
    main()
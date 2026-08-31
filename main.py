import turtle
from time import sleep
import random
WIDTH = 500
HEIGHT = 500
COLORS = ['red','green','blue','orange','yellow','violet','black','silver','grey','gold']
def get_number_of_racers():
    while True:
        racers = int(input("Введрите количество черепах для гонки от 2 до 10: "))
        if racers < 2 or racers > 10:
            print("Количество черепах должно быть больше 1 и меньше 11")
            continue
        else:
            print(f"Выбранное количество гонщиков {racers}")
            return racers
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Черепашьи гонки')
    sleep(3)
def create_turtles(colors):
    ready_racers= []
    spacing = WIDTH//(len(colors)+1)
    for index, color in enumerate(colors):
        t = turtle.Turtle()
        t.color(color)
        t.left(90)
        t.penup()
        t.shape("turtle")
        t.setpos(-WIDTH//2+(index + 1)*spacing, -HEIGHT//2+ 20)
        t.pendown()
        ready_racers.append(t)
    return ready_racers
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT//2- 10:
                return colors[turtles.index(racer)]
def main():
    racers = get_number_of_racers()
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race(colors)
    print(f"Победила черепаха цветом {winner}!")


if __name__ == '__main__':
    main
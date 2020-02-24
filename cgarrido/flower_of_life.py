import turtle

def draw_circle(t):
    t.down()
    t.circle(50)

def main_column():
    starting_y = -300
    while starting_y < 200:
        t.up()
        t.sety(starting_y)
        draw_circle(t)
        starting_y += 100

if __name__ == '__main__':
    try:
        t = turtle.Turtle()
        main_column()
    except turtle.Terminator:
        print('Program terminated.')
    except KeyboardInterrupt:
        print('Program terminated.')

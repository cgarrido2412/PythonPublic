import turtle

def draw_circle(t):
    t.down()
    t.circle(50)

def main_column():
    starting_y = -150
    while starting_y < 100:
        t.up()
        t.sety(starting_y)
        draw_circle(t)
        starting_y += 50

def outer_column():
        starting_y = -125
        t.sety(starting_y)
        draw_circle(t)
        t.up()
        starting_y += 50
        t.sety(starting_y)
        draw_circle(t)
        t.up()
        starting_y += 50
        t.sety(starting_y)
        draw_circle(t)
        t.up()
        starting_y += 50
        t.sety(starting_y)
        draw_circle(t)

def outer_most_column():
        starting_y = -100
        t.sety(-100)
        draw_circle(t)
        t.up()
        starting_y += 50
        t.sety(starting_y)
        draw_circle(t)
        t.up()
        starting_y += 50
        t.sety(starting_y)
        draw_circle(t)
        t.up()
        starting_y += 50
        t.sety(starting_y)

if __name__ == '__main__':
    try:
        t = turtle.Turtle()
        main_column()

        #right side
        t.up()
        t.setx(45)
        outer_column()

        #left side
        t.up()
        t.setx(-45)
        outer_column()

        #outer left
        t.up()
        t.setx(-90)
        outer_most_column()

        #outer right
        t.up()
        t.setx(90)
        outer_most_column()
    except turtle.Terminator:
        print('Program terminated.')
    except KeyboardInterrupt:
        print('Program terminated.')

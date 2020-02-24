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

if __name__ == '__main__':
    try:
        t = turtle.Turtle()
        main_column()
        t.up()
        starting_y = -125
        t.sety(starting_y)
        t.setx(45)
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
        t.up()
        starting_y = -125
        t.sety(starting_y)
        t.setx(-45)
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
    except turtle.Terminator:
        print('Program terminated.')
    except KeyboardInterrupt:
        print('Program terminated.')

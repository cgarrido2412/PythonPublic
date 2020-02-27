#! /usr/bin/env python3
#import modules
import pygame
import time
import random

#start pygame instance
pygame.init() 

#define screen parameters, referenced in other areas of code
display_width = 800
display_height = 600

#RGB definitions
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#define block color
block_color = (53,115,255)

#articulation of car boundaries
car_width = 73

#game window, sets caption and starts game clock
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

#load the car image
carImg = pygame.image.load('racecar.png')

#keeping score 
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

#define objects for collisions
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#places the car in the display window
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

#Create text_objects
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#define message_display
def message_display(text):
    largeText = pygame.font.Font('BluePrinted.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

#define crash
def crash():
    message_display('You Crashed')

#main game loop
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    x_change = 0
    thingCount = 1
    dodged = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -5

                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y corssover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x corssover')
                crash()

        pygame.display.update()
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()

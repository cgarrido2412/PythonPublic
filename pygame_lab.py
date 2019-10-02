import pygame
pygame.init() #initiates pygame

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height)) #defines game display A.K.A. 'surface'
pygame.display.set_caption('A bit Racey') #caption for the game

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock() #game clock
crashed = False
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN: #First, we're asking if the event is a keydown event
            if event.type == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP: #Finally, if the key change is actually a KEYUP
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x += x_change

    gameDisplay.fill(white)
    car(x,y)



    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit() 

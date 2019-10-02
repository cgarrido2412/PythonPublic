import pygame
pygame.init() #initiates pygame

gameDisplay = pygame.display.set_mode((800,600)) #defines game display A.K.A. 'surface'
pygame.display.set_caption('A bit Racey') #caption for the game

clock = pygame.time.Clock() #game clock

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit() 

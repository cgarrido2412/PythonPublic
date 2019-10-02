#import module
import pygame  

#start pygame instance
pygame.init() 

#define screen parameters, referenced in other areas of code
display_width = 800
display_height = 600

#RGB definitions
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#articulation of car boundaries
car_width = 73

#game window, sets caption and starts game clock
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

#load the car image
carImg = pygame.image.load('racecar.png')

#places the car in the display window
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

#Create text_objects
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#define message_display
def message_display(text):
    #This part needs troubleshooting
    #largeText = pygame.font.Font('Control Panel\Appearance and Personalization\Fonts\Arial.ttf', 115)
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
    x_change = 0
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
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
        car(x,y)
        if x > display_width - car_width or x < 0:
            crash()
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()

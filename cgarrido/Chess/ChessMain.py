#!/usr/bin/env python3

'''
This is our main driver file. 
It will be responsible for handling user input and displaying the current GameState object. 

TODO:
    Work through video 2
'''

import pygame as p
import ChessEngine
import os

WIDTH = HEIGHT = 512 #400 is another option 
DIMENSION = 8 #Dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION 
MAX_FPS = 15 #For animaitons later on
IMAGES = {}

'''
Initialize a global directory of images. This will be done exactly once in the main. 
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bN', 'bB', 'bQ', 'bK', 'bR']
    for piece in pieces:
         #IMAGES[piece] = p.transform.scale(p.image.load("/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
         IMAGES[piece] = p.transform.scale(p.image.load(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Python\cgarrido\Chess\images\\'+piece+'.png'), (SQ_SIZE, SQ_SIZE)) #Have only got this to work on Windows with the repo saved to the desktop
    #Note: We can acess an image by saying 'IMAGES['wp']'

'''
The main driver for our code. This will handle user input and updating the graphics. 
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    #print(gs.board)
    loadImages() #Only do this once, before the while loop
    running = True 
    sqSelected = () #no square is selected initially, keep track of the last click of the user (tuple: row, column)
    playerClicks = [] #keep track of player clicks (two tuples: [(6,4), (4,4)]) would move e2 to e4
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False 
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) location of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): #the user clicked the same square twice
                    sqSelected = () #deslect
                    playerClicks = [] #clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #append for both 1st and 2nd clicks
                if len(playerClicks) == 2: #after the 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () #reset user clicks
                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip() 

'''
Responsible for all the graphics within a current game state. 
'''
def drawGameState(screen, gs):
    drawBoard(screen) #Draw squares on the board
    #Add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board) #Draw pieces on top of those squares 

'''
Draw the squares on the board. 
'''
def drawBoard(screen):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != '--': #Not an empty square
                screen.blit(IMAGES[piece], p.Rect(column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
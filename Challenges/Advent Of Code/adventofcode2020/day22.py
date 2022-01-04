#! /usr/bin/env python3

import collections
import os 

def combat_game(deck1, deck2):
    total_cards = len(deck1) + len(deck2)

    while len(deck1) != total_cards and len(deck2) != total_cards:
        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    if len(deck1) == total_cards:
        return 'player', deck1
    else:
        return 'crab', deck2

def score(winning_hand):
    total = 0
    for x in range(len(winning_hand)):
        total += winning_hand[x] * (len(winning_hand) - x)

    return total 

if __name__ == "__main__":
    #Load the card game
    card_game = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Prisma API\Documents\puzzle_input.txt').read()
    players = card_game.split('\n\n') 

    #Split between the human player and the crab player, remove the first item of the list to have a list of just the cards. 
    human_player = players[0].split('\n')
    crab_player = players[1].split('\n')
    del human_player[0]
    del crab_player[0]
    
    #Convert the decks to integer
    human_deck = [int(x) for x in human_player]
    human_deck = collections.deque(human_deck)
    crab_deck = [int(x) for x in crab_player]
    crab_deck = collections.deque(crab_deck)

    #Play the game and wait for the result
    winner, winning_hand = combat_game(human_deck, crab_deck)
    answer = score(winning_hand)
    print(answer)

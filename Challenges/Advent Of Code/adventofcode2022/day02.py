#!/usr/bin/env python3

import os 

if __name__ == "__main__":
    
    #Read Puzzle Input. Split by line. 
    rock_paper_scissors = open(os.getenv('HOMEDRIVE')+os.getenv('HOMEPATH')+'\Desktop\Python\Coding Challenges\\adventofcode2022\day02_input.txt').read().split('\n')

    #Map out strategy guide to choices 
    oppponent_dictionary = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    player_dictionary = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

    #Map out scoring for the selected shape
    shape_score = {'rock': 1, 'paper': 2, 'scissors': 3}

    #Keeping score
    total_score = 0

    #Compare each match in the game
    for game in range(len(rock_paper_scissors)):

        #Convert Opponent Choice to rock, paper, or scissors
        opponent_choice = rock_paper_scissors[game][0]
        opponent_ouctome = oppponent_dictionary.get(opponent_choice)

        #Convert Player Chocie to rock, paper, or scissors
        player_choice = rock_paper_scissors[game][2]
        player_ouctome = player_dictionary.get(player_choice)

        #Start scoring, start with score for shape decision
        decision_score = shape_score.get(player_ouctome)
        total_score += decision_score

        #For Draws
        if opponent_ouctome == player_ouctome:
            total_score += 3
        
        #If the Opponent Wins, then if player wins
        elif opponent_ouctome == 'rock':
            if player_ouctome == 'scissors':
                total_score += 0
            elif player_ouctome == 'paper':
                total_score += 6
        elif opponent_ouctome == 'paper':
            if player_ouctome == 'rock':
                total_score += 0
            elif player_ouctome == 'scissors':
                total_score += 6
        elif opponent_ouctome == 'scissors':
            if player_ouctome == 'paper':
                total_score += 0
            elif player_ouctome == 'rock':
                total_score += 6

    print(total_score) #Part one correct and complete

    '''
    For Part 2, [X,Y,Z] determine the outcome of the game instead of representing the player choice
    '''

    #Define outcome dictionary
    outcome_dictionary = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

    #Create separate score for part 2
    round_2_score = 0

    #Compare each match in the game again
    for game in range(len(rock_paper_scissors)):

        #Convert Opponent Choice to rock, paper, or scissors
        opponent_choice = rock_paper_scissors[game][0]
        opponent_ouctome = oppponent_dictionary.get(opponent_choice)

        #Convert Player outcome to win, lose, draw
        player_tactics = rock_paper_scissors[game][2]
        game_outcome = outcome_dictionary.get(player_tactics)

        if game_outcome == 'draw':
            if opponent_ouctome == 'rock':
                round_2_score += 4
            elif opponent_ouctome == 'paper':
                round_2_score += 5
            elif opponent_ouctome == 'scissors':
                round_2_score += 6
        elif game_outcome == 'lose':
            if opponent_ouctome == 'rock':
                round_2_score += 3
            elif opponent_ouctome == 'paper':
                round_2_score += 1
            elif opponent_ouctome == 'scissors':
                round_2_score += 2
        elif game_outcome == 'win':
            if opponent_ouctome == 'rock':
                round_2_score += 8
            elif opponent_ouctome == 'paper':
                round_2_score += 9
            elif opponent_ouctome == 'scissors':
                round_2_score += 7

    print(round_2_score) #Part 2 Correct and Complete 

#! /usr/bin/env python3
'''
Author: Charles Garrido
'''

import random
import time

class Card(object):
    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }
    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]

def ascii_version_of_card(*cards, return_string=True):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # we will use this to prints the appropriate icons for each card
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']
    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]
    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.rank == '10':  # ten is the only one who's rank is 2 char long
            rank = card.rank
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            rank = card.rank[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]
        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')
    result = [''.join(line) for line in lines]
    # hidden cards do not use string
    if return_string:
        return '\n'.join(result)
    else:
        return result

playing_cards = {'Joker':'taking a risk | doing something foolish | innocence',
                 'Ace of Clubs':'Spark of inspiration, passion. A new love affair, the idea for a business or life-change.',
                 'Two of Clubs':'Planning, delays, waiting for the signal to move.',
                 'Three of Clubs':'You’ve done all you can, hard work pays off.',
                 'Four of Clubs':'Celebration, rest, stability, pause.',
                 'Five of Clubs':'Competition, petty arguments, fights, not working in harmony.',
                 'Six of Clubs':'Success, victory, good exam results.',
                 'Seven of Clubs':'Standing up for oneself. Defending your viewpoint.',
                 'Eight of Clubs':'Events moving quickly, getting organized (fast), possible pregnancy.',
                 'Nine of Clubs':'Stressed, but unbowed. Determined to finish the task/fight.',
                 'Ten of Clubs':'Responsibilities, weighed down, burdened but almost at the end of the project/life-stage.',
                 'Jack of Clubs':'Feckless charmer. Passionate affair. Individual unable to focus on one task.',
                 'Queen of Clubs':'Passionate, enthusiastic, fun. Career woman.',
                 'King of Clubs':'Leader, always aware of the larger picture, not good at details.',
                 'Ace of Hearts':'New love, beginnings of a deep connection, conception.',
                 'Two of Hearts':'Mutual attraction, love, friendship.',
                 'Three of Hearts':'Celebration of friendship, a girls’ (or boys’) night out, end of an emotional cycle.',
                 'Four of Hearts':'Emotional stability, possible low-level depression; unaware, or deliberately ignoring the positive aspects in life.',
                 'Five of Hearts':'Loss, sadness, depression, grief.',
                 'Six of Hearts':'Childhood, nostalgia, memories, the past revisited, an old flame appears.',
                 'Seven of Hearts':'Feeling-based choices, indecision, going astray.',
                 'Eight of Hearts':'Leaving, splitting up, change of direction.',
                 'Nine of Hearts':'Fulfillment, understanding that solitariness is not loneliness, contentment.',
                 'Ten of Hearts':'family, love, achievement of emotional peak.',
                 'Jack of Hearts':'A person who is in love with being in love. Romantic suitor, short-term love affair.',
                 'Queen of Hearts':'Someone to turn to; she offers emotional support, a listening ear. Watch out for darker undercurrents; she may have problems of her own.',
                 'King of Hearts':'Kindly counselor, gives wise advice based on experience. Possible alcoholic or addict of some kind.',
                 'Ace of Spades':'Flash of insight, revelation, realization, understanding, idea.',
                 'Two of Spades':'Reluctance/refusal to acknowledge the truth, withdrawal. Possible communication difficulties.',
                 'Three of Spades':'Breakdown in communication; misunderstanding leading to a rift, fight or break-up.',
                 'Four of Spades':'Recovery, recuperation, time-out.',
                 'Five of Spades':'Deception, bullying, walking away from a disagreement. Resistance or non-resistance.',
                 'Six of Spades':'Moving on, a change of direction, travel; putting the past behind you.',
                 'Seven of Spades':'Theft, recovery of property or abstract quality (confidence, self-esteem, etc.). Subterfuge.',
                 'Eight of Spades':'Feeling there’s no choice, backing oneself into a corner, can’t see the way out—although the solution is right there in plain view.',
                 'Nine of Spades':'Nightmares, repetitive thought, problems, anxiety, depression',
                 'Ten of Spades':'Endings, mental breakdown, the only way is up. New beginning.',
                 'Jack of Spades':'Someone on a mission. Single-minded individual. Clever, sarcastic, intelligent.',
                 'Queen of Spades':'Truthseeker, efficient person. She cannot put up with indecisiveness or stupidity.',
                 'King of Spades':'Professional, good at his job, highly motivated and intelligent. Advisor, lawyer, accountant, writer.',
                 'Ace of Diamonds':'Prize, gift, new home, new project, new job.',
                 'Two of Diamonds':'Balancing the budget, time management. Juggling resources.',
                 'Three of Diamonds':'Focus on work. Honing skills, teamwork, collaboration.',
                 'Four of Diamonds':'Guarding resources, not socializing; holding oneself apart from society.',
                 'Five of Diamonds':'Needing help, destitution, lack of money, loss of job.',
                 'Six of Diamonds':'Charity, offering/receiving help, supporting another financially.',
                 'Seven of Diamonds':'Materially well-off yet spiritually dissatisfied. Looking for a possible new direction.',
                 'Eight of Diamonds':'New job, change of career, improving skills, undergoing training or teaching.',
                 'Nine of Diamonds':'Material and spiritual independence. Satisfaction, happy in solitude.',
                 'Ten of Diamonds':'Family, inheritance, traditions, family business, social gatherings.',
                 'Jack of Diamonds':'Hard worker, loyal person, hidden attributes.',
                 'Queen of Diamonds':'Home lover, nest-builder, mother, female leader.',
                 'King of Diamonds':'Businessman, achievements through hard work. Enjoyment of luxury and fruits of own labor.'}

card_selection_conversion = {'Ace':'Ace',
                             'Two':'2',
                             'Three':'3',
                             'Four':'4',
                             'Five':'5',
                             'Six':'6',
                             'Seven':'7',
                             'Eight':'8',
                             'Nine':'9',
                             'Ten':'10',
                             'Jack':'Jack',
                             'Queen':'Queen',
                             'King':'King'}

the_suit_of_clubs = '''
Clubs are the equivalent of the tarot suit of Wands.
They represent action, passion and inspiration.
They are associated with fire.
'''

the_suit_of_hearts = '''
Hearts are the same as the tarot Cups.
They represent emotions, feelings, fulfillment, and, of course, love and loss.
Hearts are associated with water.
'''

the_suit_of_spades = '''
Spades are equivalent to the tarot suit of Swords.
They are connected to thought and communication.
All the activity that goes on in our minds; ‘head stuff’.
Spades are associated with air.
'''

the_suit_of_diamonds = '''
Diamonds are equal to the suit of Pentacles in tarot.
They relate to the material word; all that we see and touch.
They cover such areas as money, work, practical projects, homes, etcetera.
Diamonds can also represent the practical aspects of relationships.
Diamonds are associated with earth.
'''

suits = ['Spades',
         'Diamonds',
         'Hearts',
         'Clubs']

cards = ['Ace',
         'Two',
         'Three',
         'Four',
         'Five',
         'Six',
         'Seven',
         'Eight',
         'Nine',
         'Ten',
         'Jack',
         'Queen',
         'King']

if __name__ == '__main__':
    try:
        while True:
            question = input('\n\n\nDraw a card?\n[y/n]\n')
            if question == 'y':
                suit_selection = random.sample(suits, 1)
                if suit_selection[0] == 'Spades':
                    print('The deck has been shuffled, your card is in the suit of Spades.\n')
                    print(the_suit_of_spades)
                elif suit_selection[0] == 'Hearts':
                    print('The deck has been shuffled, your card is in the suit of Hearts.\n')
                    print(the_suit_of_hearts)
                elif suit_selection[0] == 'Clubs':
                    print('The deck has been shuffled, your card is in the suit of Clubs.\n')
                    print(the_suit_of_clubs)
                elif suit_selection[0] == 'Diamonds':
                    print('The deck has been shuffled, your card is in the suit of Diamonds.\n')
                    print(the_suit_of_diamonds)
                card_selection = random.sample(cards, 1)
                final_card = card_selection[0] + ' of ' + suit_selection[0]
                converted_card_selection = card_selection_conversion.get(card_selection[0]) 
                print('Your tarot card is:\n' + final_card)
                print(ascii_version_of_card(Card(suit_selection[0], converted_card_selection)))
                print(playing_cards.get(final_card))
            elif question == 'n':
                exit()
    except KeyboardInterrupt:
        print('Program terminated.')
        exit()

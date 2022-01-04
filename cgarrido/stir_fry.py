#!/usr/bin/env python3

'''
Description:
    This script was made to generate random stir fry recipes. 
    It keeps the ingredient selection to seven items both for simplicity
    and to make things easier for one bag / one trip shopping. 
    The elements of each dish include, protein, aromatics, vegetables, a finishing acid and a garnish. 
    Along with heat, sweet and salt, these are some pretty tasty meals!
'''

import random 

#Function to generate a random recipe based on ingredients
def create_recipe(protein, aromatic, vegetables, finishers, garnish):
    shopping_list = []
    ingredients = [protein, aromatic, vegetables, finishers, garnish]
    for x in range(len(ingredients)):
        if ingredients[x] == vegetables:
            random_selection = random.sample(vegetables, 3)
            for item in random_selection:
                shopping_list.append(item)
        else:
            random_selection = random.choice(ingredients[x])
            shopping_list.append(random_selection)
    return shopping_list

if __name__ == "__main__":
    #starting ingredient lists
    protein = ['chicken', 'pork', 'steak', 'shrimp', 'tofu']
    aromatic = ['garlic', 'scallions', 'ginger']
    vegetables = ['onion', 'bell pepper', 'carrot',
                    'celery', 'bean sprout', 'mushroom',
                    'broccoli/cauliflower', 'cabbage', 'baby spinach',
                    'bok choy', 'peas/corn', 'kale',
                    'green beans', 'asparagus', 'zucchini']
    finishers = ['lime juice', 'lemon juice']
    garnish = ['cilantro', 'basil', 'green onion', 'sesame seeds', 'peanuts', 'hot sauce']

    #putting together something at random
    shopping_list = create_recipe(protein, aromatic, vegetables, finishers, garnish)

    #Output of shopping list
    recipe = '''
Your stir fry recipe list!
Protein: {}
Aromatic: {}
Vegetables: {}, {}, {}
Finish: {}
Garnish: {}
    '''.format(shopping_list[0],
               shopping_list[1],
               shopping_list[2],
               shopping_list[3],
               shopping_list[4],
               shopping_list[5],
               shopping_list[6])
    print(recipe)

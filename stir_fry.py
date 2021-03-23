#!/usr/bin/env python3

import random 

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

    #shopping list
    print(shopping_list)

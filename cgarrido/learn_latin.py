#! /usr/bin/env python3
import random
phrases = {'Ad astra per aspera':'Through adversity to the stars',
           'Acta deos numquam mortalia fallunt':'Mortal actions never deceive the gods',
           'Carpe vinum':'Seize the wine',
           'Alea iacta est':'The die is cast',
           'Dulce periculum':'Danger is sweet',
           'Acta non verba':'Deeds, not words',
           'Condemnant quo non intellegunt':'They condemn that which they do not understand',
           'Audentes fortuna iuvat':'Fortune favors the bold',
           'Factum fieri infectum non potest':'It is impossible for a deed to be undone',
           'Aut viam inveniam aut faciam':'I will either find a way or make one',
           'Qui totum vult totum perdit':'He who wants everything loses everything',
           'Faber est suae quisque fortunae':'Every man is the artisan of his own fortune',
           'Aquila non capit muscas':'The eagle does not catch flies',
           'Natura non constristatur':'Nature is not saddened',
           'Flectere si nequeo superos, Acheronta movebo':'If I cannot move Heaven, I will raise Hell',
           'Ad meliora':'Toward better things',
           'Nullum magnum ingenium sine mixture dementia fuit':'There has been no great wisdom without an element of madness',
           'Barba tenus sapientes':'As wise as far as the beard',
           'Creo quia absurdum est':'I believe because it is absurd',
           'Lupus non timet canem latrantem':'A wolf is not afraid of a barking dog',
           'Non ducor duco':'I am not led; I lead',
           'Fere libenter homines id quod volunt credunt':'Men generally believe what they want to',
           'Sic gorgiamus allos subjectatos nunc':'We gladly feast on those who would subdue us',
           'Amore et melle et felle es fecundissimus':'Love is rich with honey and venom',
           'In absentia lucis, Tenebrae vincunt':'In the absence of light, darkness prevails',
           'De omnibus dubitandum':'Be suspicious of everything',
           'Ars longa, vita brevis':'Art is long, life is short',
           'Nemo mortalium omnibus horis sapit':'Of mortal men, none is wise at all times',
           'Quid infantes sumus':'What are we, babies',
           'Mea navis aëricumbens anguillis abundant':'My hovercraft is full of eels',
           'Bibo ergo sum':'I drink, therefore I am'}

program_running = True

while program_running is True:
    continue_running = input('Generate a phrase? [y/n]\n')
    continue_running = continue_running.strip()
    continue_running = continue_running.lower()

    if continue_running == 'y':
        res = key, val = random.choice(list(phrases.items())) 
        print(res)

    elif continue_running == 'n':
        program_running = False

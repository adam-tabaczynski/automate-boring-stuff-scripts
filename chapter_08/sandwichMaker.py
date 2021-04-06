#sandwichMaker.py - program utilizng PyInputPlus

import pyinputplus as pyip

def sandwich_maker():
    
    print('Welcome to sandwich maker!')
    bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                                prompt='Choose bread type:\n')
    protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                                prompt='Choose protein type:\n')
    
    want_cheese = pyip.inputYesNo(prompt='You want cheese?\n')
    if want_cheese == 'yes':
        cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],
                                prompt='Choose cheese type:\n')
    else:
        cheese_type = 'No'

    want_mayo = pyip.inputYesNo(prompt='You want mayo?\n')
    want_mustard = pyip.inputYesNo(prompt='You want mustard?\n')
    want_lettuce = pyip.inputYesNo(prompt='You want lettuce?\n')
    want_tomato = pyip.inputYesNo(prompt='You want tomato?\n')
    number_of_sandwiches = pyip.inputInt(
        prompt='How many sandwiches you want?\n', min=1)

    price, ingredients_dict = price_counter(bread_type, protein_type, cheese_type,
                              want_mayo, want_mustard, want_lettuce,
                              want_tomato)
    price_print(price, ingredients_dict, number_of_sandwiches)

def price_counter(bread, protein, cheese, mayo, mustard, lettuce, tomato):
    price = 0
    ingredients_dict = {}
    bread_dict = {'wheat': 1.70, 'white': 1.50, 'sourdough': 2.20}
    ingredients_dict[bread] = bread_dict[bread]
    price += bread_dict[bread]
    prot_dict = {'chicken': 1.50, 'turkey': 1.30, 'ham': 1.70, 'tofu': 2.20}
    ingredients_dict[protein] = prot_dict[protein]
    price += prot_dict[protein]
    cheese_dict = {'cheddar': 0.50, 'Swiss': 0.60, 'mozzarella': 1.00, 'No': 0.00}
    ingredients_dict[cheese] = cheese_dict[cheese]
    price += cheese_dict[cheese]

    if mayo == 'yes':
        ingredients_dict['mayo'] = 0.30
        price += 0.30
    if mustard == 'yes':
        ingredients_dict['mustard'] = 0.30
        price += 0.30
    if lettuce == 'yes':
        ingredients_dict['lettuce'] = 0.20
        price += 0.20
    if tomato == 'yes':
        ingredients_dict['tomato'] = 0.20
        price += 0.20

    return (price, ingredients_dict)

def price_print(price, ingredients_dict, number_sandwiches):
    for ingr, pricing in ingredients_dict.items():
        print(f'{ingr} - {pricing}')
    print(f'Price for one sandwich - {price}')
    print("Price for " + str(number_sandwiches) +": " + str(float(price) * int(number_sandwiches)))

sandwich_maker()   

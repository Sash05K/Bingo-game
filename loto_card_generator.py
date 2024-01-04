from random import randrange, sample

def card_generator():
    '''Generates a bingo card and stores the  number a dictionary'''
    card = {
        'B': [],
        'I': [],
        'N': [],
        'G': [],
        'O': [],
    }
    start = 1
    end = 16 
    for key in card:
        card[key] = sample(range(start, end), 5)
        start = end
        end += 15
        
    return card

    

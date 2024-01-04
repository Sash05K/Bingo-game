 # Define a function to check if a Bingo card has a winning combination
def check_row(card: dict) -> bool:
    '''First checks for row win'''
    return any(sum(card[key][index] for key in card) == 0 for index in range(len(card)))

def _check_col(card: dict) -> bool:
    '''Second checks for col wins'''
    return any(sum(card[key]) == 0 for key in card)
    
def check_diag(card: dict) -> bool:
    '''At the last check for diagonal wins'''
    return sum(card[key][index] for index, key in enumerate(card)) == 0

def update_card(card: dict, num: int) -> dict:
    '''This will check if the number is in the card and change it to zero '''
    for key in card:
        if num in card[key]:
            card[key][card[key].index(num)] = 0


__all__ = ['_check_col', 'check_diag', 'check_row', 'update_card']
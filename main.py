from loto_card_generator import card_generator
from card_checker import *
from print_card import pprinter
from random import choice
import time


def run():
    '''Run Bingo game'''
    pprinter(card)
    
    balls = [i for i in range(1, 76)]
   
    while not any((_check_col(card), check_diag(card), check_row(card))):
        ball = choice(balls)
        balls.remove(ball)
        time.sleep(3)
        print(f"The ball number is: {ball}")
        update_card(card, ball)
        pprinter(card)
    
      
    
    return card
    
if __name__ == '__main__':
    '''Main method for the program ,generates a card,prints it,and loops through printing antil the checker  methods return True'''
    print("Let's play Bingo")
    card = card_generator()

   
    run()

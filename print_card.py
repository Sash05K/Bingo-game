from card_checker import *
from pprint import pprint

def pprinter(card):
   '''Print the Bingo cards'''
   print(f"{'B':>5}{'I':>5}{'N':>5}{'G':>5}{'O':>5}")
  

   for i in range(5):
        for k,v in card.items():
            print(f"{v[i]:>5}",end='')
           
        print()
   if  any((_check_col(card), check_diag(card), check_row(card))):
      pprint("You win the Bingo game".center(50))

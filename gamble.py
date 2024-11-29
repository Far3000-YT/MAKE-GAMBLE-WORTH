import sys
from random import randint
from json import load

import time

with open("values.json", 'r+') as file:
    data = load(file)

balance, bet_amount = int(data['balance']), int(data['bet_amount'])
bet_true, i = True, 0

#Reduced output frequency (for example, print every 100th bet)
while bet_true:
    i += 1
    choice = randint(0, 1)  #0 for loss and 1 for win
    
    if choice == 1:
        balance += bet_amount
        bet_amount = data['bet_amount']
        if i % 1000 == 0:
            print(f"WIN  - {i} - {choice} - {balance}")
    else:
        balance -= bet_amount
        bet_amount = bet_amount * 2
        if i % 1000 == 0:
            print(f"LOSS - {i} - {choice} - {balance}")
    sys.stdout.flush()

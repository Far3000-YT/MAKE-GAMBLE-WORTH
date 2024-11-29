from sys import stdout
from random import randint
from json import load

with open("values.json", 'r+') as file:
    data = load(file)

balance, bet_amount = int(data['balance']), int(data['bet_amount'])
bet_true, i = True, 0

#reduced output frequency (print every 1k th iteration)
while bet_true:
    i += 1
    choice, freq = randint(0, 1), 1000 #0 for loss and 1 for win
    if choice == 1:
        balance += bet_amount
        bet_amount = data['bet_amount']
        if i % freq == 0:
            print(f"WIN  - {i} - {choice} - {balance}")
    else:
        balance -= bet_amount
        bet_amount = bet_amount * 2
        if i % freq == 0:
            print(f"LOSS - {i} - {choice} - {balance}")
        if balance <= 0: print("loss xd")
    stdout.flush()
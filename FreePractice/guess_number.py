import random

def guess(x):
    random_num = random.randint(0,x)
    attemps = 0
    while True:
        attemps += 1
        your_bet = int(input(f"Give me a number between 0 and {x}: "))
        
        if your_bet < random_num:
            print(f"{your_bet}, is too low...")
            continue
        elif your_bet > random_num:
            print(f"{your_bet} is too high...")
            continue
        elif your_bet == random_num:
            print("YOU WIN!!!")
            print(f"You only used {attemps} attemps!")
            break
guess(100)

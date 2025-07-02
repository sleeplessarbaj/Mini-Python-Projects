# guess my number 

import random

computer = random.randint(1, 10)

player = int(input("Guess number between 1 to 10: "))

print(f"Computer choose number {computer}.")
print(f"Player choose number {player}.")

if(player == computer):
    print("You Won!")
else:
    print("You lost!")

print("Thanks for playing.")
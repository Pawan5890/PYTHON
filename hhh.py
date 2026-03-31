import random

def roll():
    return random.randint(1,6)
diceroll=roll()
print("you roll",diceroll)

for i in range(6):
    print("roll",i+1,":",roll())

import random


# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose stone
    elif comp == 'stone':
        if you=='scissor':
            return False
        elif you=='paper':
            return True
    
    # Check for all possibilities when computer chose scissor
    elif comp == 'scissor':
        if you=='paper':
            return False
        elif you=='stone':
            return True
    
    # Check for all possibilities when computer chose paper
    elif comp == 'paper':
        if you=='stone':
            return False
        elif you=='scissor':
            return True

guess = 0

print("Comp Turn: (stone) (scissor) or (paper)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'stone'
elif randNo == 2:
    comp = 'scissor'
elif randNo == 3:
    comp = 'paper'

you = input("What do you choose: type stone, paper or scissor?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")

import random

words = ["apple","mango","orange","banana","grape"]
print(words)

chosenword = random.choice(words)
print(chosenword)


chosenlist = []
for i in chosenword:
    chosenlist.append("_")
print(chosenlist)

length = len(chosenword)

endofgame = False
while not endofgame:
    guess = input("enter a letter").lower()
    
    for i in range(length):
        if chosenword[i] == guess:
            chosenlist[i] = guess
    print(chosenlist)
    if '_' not in chosenlist:
        endofgame = True
        print("you win")

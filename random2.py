import random

words = ["apple","mango","orange","banana","grape"]
print(words)
str = "soumya"
print(str[::-1])

chosenword = random.choice(words)
print(chosenword)
guess = input("enter a letter").lower()


chosenlist = []
for i in chosenword:
    chosenlist.append(i)
print(chosenlist)

for index, value in enumerate(chosenlist):
    if guess != value:
        chosenlist[index] = "_"
print(chosenlist)

import random

namelist = ["aravindgoudkasarapu","thirugoudkasarapu","chikkakasarapu","soumyakasarapu"]

chosenword = random.choice(namelist)
print(chosenword)

letter = input("enter a letter")

for i in chosenword[0:len(chosenword)]:
    if letter == i:
        print(f"{i}{letter}...right")
    else:
        print(f"{i}{letter}...wrong")
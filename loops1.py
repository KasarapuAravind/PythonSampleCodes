fruits = ["apple","mango","grape","orange","banana"]
for i in fruits:
    print(i)


scorelist = input("enter student score list").split()
for n in range(0, len(scorelist)):
    scorelist[n] = int(scorelist[n])
    print(scorelist[n])
    print(type(scorelist[n]))

print(type(scorelist))
print(scorelist)

maxscore = 0
for score in scorelist:
    if score > maxscore:
        maxscore = score
print(maxscore)
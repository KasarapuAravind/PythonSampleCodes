import random
namestring = input("enter names seperated by comma..")
list1 = namestring.split(",")
print(list1)
print(type(list1))
listlength = len(list1)
randomindex = random.randint(0,listlength-1)
print(randomindex)
print(f"{list1[randomindex]} has to pay the bill today")

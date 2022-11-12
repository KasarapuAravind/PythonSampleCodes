
mytuple = ("aravind", 29, "engineer")
mylist = ["apple","mango",2]
print(type(mytuple))
print(mytuple)

tuplecon = tuple(mylist)
print(type(tuplecon))
print(tuplecon[1])

mylist[0] = "banana"
print(mylist)

for i in tuplecon:
    print(i)

if 'aravind' in mytuple:
    print('yes')
else:
    print('no')


#tuple in python
print("")

print(mylist.index(2))





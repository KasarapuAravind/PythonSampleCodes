
mylist = ['apple','mango','banana','grape']
str1 = "aravindgoud"
dict1 = {"name":"aravind","jobname":"software","age":40,"qualities":[{"best":"kindness","worst":"lazyness"}]}

for item in mylist:
    print(item)

for i in range(len(mylist)):
    print(mylist[i])



for j in range(len(str1)):
    print(str1[j])

print(dict1["qualities"][0]["worst"])

mylist.append("cherry")
print(mylist)

mylist.insert(3,'orange')
print(mylist)

newlist = sorted(mylist)

#mylist.pop(2)
print(mylist)
print(newlist)

newlist1 = ["aravind"] * 2 + ["thiru"] * 2
newlist2 = newlist1[1] 
print(newlist1)
print(newlist2)

##########################################################################################

mylist2 = [1, 5, 2, 9, 4, 7]
mylist2_1 = []
#mylist2_1 = [i*i*i for i in mylist2]    ## this is shortcut way
for i in range(0, len(mylist2)):
    mylist2_1.append(mylist2[i] * mylist2[i])
print(f"the new list is : {mylist2_1}")

#########################################################################################








keys = ['ten', 'twenty','thirty']
values = [10, 20, 30, 40]

mydict1 = {}

### first way
# for i in range(0, len(keys)):
#     for j in range(i, i+1):
#         mydict1[keys[i]] = values[j]
# print(mydict1) 


### second way
for i in range(len(keys)):
    mydict1.update({keys[i]:values[i]})
print(mydict1)
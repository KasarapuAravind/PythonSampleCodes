import random
print(random.random())

v1 = "aravind"
if v1 == "aravind":
    v2 = ["a", "b", "c","d","e"]

print(type(v1))
print(type(v2))
print(len(v2))
v2[5:] = ["f"]
print(v2)  
v2.append("g")
print(v2)
v2.extend(["h","i","j"])
print(v2)
delvalue = v2.pop(3)
print(v2)
print(delvalue)


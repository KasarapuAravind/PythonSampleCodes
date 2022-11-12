
###### Combining two dictionaries
# dict1 = {'ten':10, 'twenty': 20, 'thirty': 30}
# dict2 = {'thirty': 30,'forty':40,'fifty':50}

# tot = {**dict1, **dict2}
# print(tot)


### Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

newdict1 = {}
for i in employees:
    newdict1[i] = defaults
print(newdict1) 

##########################################################
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

for i in keys:
    sample_dict.pop(i)
print(sample_dict)

#######################################3

sample_dict2 = {'a': 100, 'b': 400, 'c': 300}

if 'city' in sample_dict2.keys():
    print("yes 200 exists")
else:
    print('no')

####################################################################33

sample_dict3 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict3['location'] = sample_dict3.pop('city')
print(sample_dict3)


######################################################################

sample_dict4 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict4, key=sample_dict4.get))










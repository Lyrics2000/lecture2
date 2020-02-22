#Creating a dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Accessing a dict
x = thisdict.get("model")
print(x)

#Change a dict

thisdict["year"] = 2018
print(thisdict)

#Loop thru dict
for x in thisdict:
  print(x)

#prints values one by one
for x in thisdict:
  print(thisdict[x])

#prints values one by one
for x in thisdict.values():
  print(x)

#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)

#Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
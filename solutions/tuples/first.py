#creatinga a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#NB: most things applied in a list can also be applied to a tuple
#selecting values of a tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Remove Items
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exist

#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)




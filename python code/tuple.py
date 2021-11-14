thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(thistuple[1])
print(thistuple[-3])
print(thistuple[2:5]) # Return the third, fourth, and fifth item
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-2:])
print(thistuple[1:-2])

thistuples = ("apple", "banana", "cherry")
print(len(thistuples))

thistuple1 = ("apple",)
print(type(thistuple1))

#NOT a tuple
thistuple2 = ("apple")
print(type(thistuple2))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thattuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thattuple)

# change a variable in a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# cond 2 tuples first way 
thistuple10 = ("apple", "banana", "cherry")
z = list(thistuple10)
z.append("orange")
thistuple10 = tuple(z)

# cond 2 tuples second way
thistuple100 = ("apple", "banana", "cherry")
y = ("orange",)
thistuple100 += y
print(thistuple100)

# Remove a variable from tuple
thistuple20 = ("apple", "banana", "cherry")
y = list(thistuple20)
y.remove("apple")
thistuple20 = tuple(y)

# delete a tuple
thistuple200 = ("apple", "banana", "cherry")
del thistuple200

# Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Assign the rest of the values as a list called "red"
fruitss = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruitss
print(green)
print(yellow)
print(red)

# Add a list of values the "tropic" variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply the fruits tuple by 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# count the number of times that 5 occurs in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# Search for the first occurrence of the value 8, and return its position
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
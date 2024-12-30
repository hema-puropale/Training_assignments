# creating
x = list()
print(x)   # o/p []

x = []
print(x)  # o/p []

# length
x = ["apple", "banana", "cherry"]
print(x)
print(len(x))  # o/p 3

# type
x = [5, 2.5, True, "apple", "apple"]
print(type(x))  # o/p <class 'list'>

# indexing
x = [5, 2.5, True, "apple"]
print(x[-2])  # o/p True

# slice
x = [5, 2.5, True, "apple"]
y = x[1:3]
print(y)  # o/p [2.5,True]

# append
x = [5, 2.5, True, "apple"]
x.append(7)
print(x)  # o/p [5,2.5,True,"apple",7]

# insert
x = [5, 2.5, True, "apple"]
x.insert(1, "banana")
print(x)   # o/p [5,banana,2.5,True,"apple"]

# EXTEND
x = [5, 2.5, True, "apple"]
y = [2, 3, "banana"]
x.extend(y)
print(x)  # o/p [5,2.5,True,"apple",2,3,"banana"]

# remove (removes specified item)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # o/p ["apple","cherry"]

# pop (removes item at particular index)
x = [5, 2.5, True, "apple"]
x.pop(1)
print(x)  # o/p [5,True,"apple"]

# sort
x = [5, 2]
x.sort()
print(x)  # o/p [2,5]

x = ["apple", "mango", "banana"]
x.sort(reverse=True)
print(x)  # o/p ["mango","banana","apple"]

# reverse
x = [5, 2.5, True, "apple"]
x.reverse()
print(x)  # o/p ["apple",True,2.5,5]

# split
x = "hema is a good girl"
y = x.split()
print(y)  # o/p ["hema","is","a","good","girl"]

# join
x = ["Durga", "mam", "is", "our", "trainer"]
y = " ".join(x)
print(y)  # o/p Durga mam is our trainer

# count
x=[5, 6, 6, 7, 7, 8, 9]
y=x.count(2)
print(y)  # o/p 0

# index
x=[5, 6, 6, 7, 7, 8, 9]
print(x.index(6))   # o/p 1

# tuple creating
x=()
print(x)     # o/p ()

x=tuple()
print(x)         # o/p ()
print(type(x))   # o/p <class "tuple">

# length
x=(1,2,2.5,True,"hi")
print(len(x))    # o/p 5

# changing values by converting to list
x = ("apple", "banana", "cherry", "apple")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)    # o/p ("apple", "kiwi", "cherry", "apple")

# add tuple to a tuple
x = ("apple","banana","cherry")
y=(True,"hi")
x+=y
print(x)    # o/p ("apple","banana","cherry",True,"hi")

# count
x = ("apple", "banana", "cherry", "apple")
y=x.count("apple")
print(y)    # o/p 2

# index
x = ("apple", "banana", "cherry", "apple")
print(x.index("apple")) # o/p 0


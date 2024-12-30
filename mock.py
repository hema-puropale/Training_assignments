for i in range(1,10):
    if i==5:
        continue
    else:
        print(i)

# remove (removes specified item)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # o/p ["apple","cherry"]

# pop (removes item at particular index)
x = [5, 2.5, True, "apple"]
x.pop(1)
print(x)  # o/p [5,True,"apple"]
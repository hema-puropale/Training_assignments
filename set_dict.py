# 1. Set Methods
# •	add(elem): Adds an element to the set.
my_set = {1, 2, 3}
my_set.add(4)  # my_set becomes {1, 2, 3, 4}
print(my_set)

# •	remove(elem): Removes an element from the set. Raises a KeyError if the element is not present.
my_set = {1, 2, 3}
my_set.remove(2)  # my_set becomes {1, 3, 4}
print(my_set)

my_set = {1, 2, 3}
my_set.discard(5)  # No error if 5 is not in the set
print(my_set)

# •	pop(): Since sets are unordered, we can't predict which element will be removed.
my_set = {1, 2, 3}
my_set.pop()
print(my_set)

# •	clear(): Removes all elements from the set, making it empty.
my_set = {1, 2, 3}
my_set.clear()  # my_set becomes set()
print(my_set)

# •	union : Returns a new set with elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3=set1.union(set2)  # Returns {1, 2, 3, 4, 5}
print(set3)

# •	intersection : Returns a new set with elements that are in both sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3=set1.intersection(set2)  # Returns {2, 3}
print(set3)

# •	difference : Returns a new set with elements in the current set but not in the other set (i.e., set difference).
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3=set1.difference(set2)  # Returns {1}
print(set3)

# •	issubset: Returns True if all elements of the current set are in the other set.
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Returns True

# •	issuperset : Returns True if the current set contains all elements of the other set.
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Returns True

# •	copy(): Returns a shallow copy of the set.
my_set = {1, 2, 3}
my_set_copy = my_set.copy()
print(my_set_copy)

# 2. Dictionary Methods
# A dictionary is an unordered collection of key-value pairs. Keys are unique, and each key maps to a value.

# •	get(key, default=None): Returns the value for the specified key. If the key is not found, it returns the default value (or None if not specified).
my_dict = {"a": 1, "b": 2}
my_dict.get("a")  # Returns 1
my_dict.get("c", "not found")  # Returns 'not found'

# •	setdefault(key, default=None): Returns the value for the key if it exists. If it doesn't exist, it sets the key with the default value and returns it.
my_dict = {"a": 1, "b": 2}
my_dict.setdefault("c", 3)  # Adds 'c' with value 3 and returns 3

# •	update(other_dict): Updates the dictionary with elements from another dictionary or iterable. It will overwrite existing keys with new values.
my_dict = {"a": 1, "b": 2}
my_dict.update({"b": 3, "c": 4})  # my_dict becomes {"a": 1, "b": 3, "c": 4}

# •	keys(): Returns a view object displaying all keys in the dictionary.
my_dict = {"a": 1, "b": 2}
my_dict.keys()  # Returns dict_keys(['a', 'b'])

# •	values(): Returns a view object displaying all values in the dictionary.
my_dict.values()  # Returns dict_values([1, 2])

# •	items(): Returns a view object displaying all key-value pairs in the dictionary as tuples.
my_dict.items()  # Returns dict_items([('a', 1), ('b', 2)])

# •	pop(key): Removes and returns the value for the specified key. Raises a KeyError if the key doesn't exist.
my_dict.pop("a")  # Removes and returns the value of 'a', my_dict becomes {"b": 2}

# •	clear(): Removes all key-value pairs from the dictionary, making it empty.
my_dict.clear()  # my_dict becomes {}

# •	copy(): Returns a copy of the dictionary.
my_dict_copy = my_dict.copy()

name=input()
designation=input()
technology=input()
for i in range(100):
    print(name+", "+designation+", "+technology)


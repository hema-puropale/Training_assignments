#1
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
#2
for i in range(5):  # Iterates from 0 to 4
    print(f"Iteration {i}")
#3
for i in range(1, 6):
    print(i)
#4
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#5
x='hema'
for i in x:
    print(i)
#6
for i in range(11,21,3):
    print(i)
#7
for i in range(21,11,-1):
    print(i)
#8
for i in range(10,21):
    if i%5==0:
        print(i)
#9
for i in range(10,21):
    if i%5!=0:
        print(i)
#10
numbers = [1, 2, 3, 4, 5]
s=0
for i in numbers:
    s+=i
print("Total with for loop:", s)
total =sum(numbers)
print('Total sum with sum function:', total)

#11
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

#while loop
i = 1
while i <= 10:
    print(i)
    i+=1
#
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Total sum:", total)
#
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
#
i = 0
while i < 5:
    i += 1
    if i == 3:  # Skip when i is 3
        continue
    print(i)







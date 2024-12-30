# 1.print your name 100 times
name=input()
for i in range(100):
    print(name)

# 2.Check whether the number is even or not
n=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")

# 3.Print 7th table
for i in range(1,11):
    print("7 * "+str(i)+" = "+str(i*7))

# 4.min and max from 2 numbers
a=int(input())
b=int(input())
if a<b:
    print("a is minimum and b is maximum")
elif b<a:
    print("b is minimum and a is maximum")

# 5.Largest of 3 numbers (give space separated integers as input)
list_a=list(map(int,input().split()))
largest=list_a[0]
for i in range(1,len(list_a)):
    if list_a[i]>largest:
        largest=list_a[i]
print(largest)
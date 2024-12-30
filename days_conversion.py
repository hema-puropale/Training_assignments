n=int(input())
p1=str(int(n/365))
n=n%365
p2=str(int(n/7))
n=n%7
p3=str(int(n/1))
print(p1+" years "+p2+" weeks "+p3+" days ")
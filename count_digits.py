"""
We are given an n-digit number. The task is to find the number of digits in the number,
 provided that, n>0.
"""


n=int(input())
C=0
while n>0:
    n=n//10
    C+=1
print(C)

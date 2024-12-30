"""
We are given a number. The task is to find the factorial of the number.

The factorial (n!) of a number is the product of all the integers from 1 to that number, i.e, 

                     n! = 1*2*3*.....(n-1)*n
"""
n=int(input())
res=1
for i in range(2,n+1):
    res=res*i
print(res)

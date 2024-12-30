"""We want to print the divisors in sorted order.

The idea is to 1st print all divisors from 1 (inclusive) to square root n (exclusive)

Then, print all divisors from square root n (inclusive) to n (inclusive)

Time Complexity: O(sqrt(n)) """

n=int(input())
for i in range(1,int(n**0.5)):
    if n%i==0:
        print(i)
for i in range(int(n**0.5),n+1):
    if n%i==0:
        print(i)

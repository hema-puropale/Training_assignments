""" We are given a number n. The task is to print all prime factors of n."""
n=int(input())
def prime_factors(n):
    if n<1:
        return
    while n%2==0:
        print(2)
        n=n/2
    while n%3==0:
        print(3)
        n=n/3
    i=5
    while i<=int(n**0.5):
        while n%i==0:
            print(i)
            n=n/i
        while n%(i+2)==0:
            print(i+2)
            n=n/(i+2)
        i+=6
    if n>3:
        print(int(n))

prime_factors(n)

""" The task is to find the GCD / HCF of the numbers. """

a=int(input())
b=int(input())
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
res=gcd(a,b)
print(res)

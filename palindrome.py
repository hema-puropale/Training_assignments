"""
We are given an n-digit number. The task is to find if the number 
is palindrome or not, provided that, n>=0.

If the Reversed Number is equal to the original number, then
 the number is said to be a palindrome number, otherwise not
"""
n=int(input())
temp=n
rev=0
while temp>0:
    rev=rev*10+temp%10
    temp=temp//10
print(rev==n)

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPallindrome(x):
    return str(x) == str(x)[::-1]

INITIALVALUE = 999
i = INITIALVALUE
j = INITIALVALUE

maxFound = 0

while i > 1:
    while j > 1:
        mult = i * j
        if mult > maxFound and isPallindrome(mult):
            maxFound = mult
        j -= 1
    j = INITIALVALUE
    i -= 1

print maxFound

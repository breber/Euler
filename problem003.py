'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
import util

VALUE = 600851475143

maxPrime = 0
for i in range(1, int(math.sqrt(VALUE)), 2):
    if VALUE % i == 0 and util.isPrime(i):
            maxPrime = i

print maxPrime

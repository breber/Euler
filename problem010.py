'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import util

MAX_NUM = 2000000

sum_val = 1
for i in range(0, MAX_NUM):
    if util.isPrime(i):
        sum_val += i

print sum_val

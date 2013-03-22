'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
'''
import util

MAX_NUM = 10001

current_number = 1
prime_count = 1

while prime_count < MAX_NUM:
    current_number += 1

    if util.isPrime(current_number):
        prime_count += 1

print current_number

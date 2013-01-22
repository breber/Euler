'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

MAX_NUM = 20

current = 21
while True:
    divisible = True
    for i in range(2, MAX_NUM):
        if current % i:
            divisible = False
            break

    if divisible:
        print current
        break

    current += 1

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
BASE = 2
POWER = 1000

digit_sum = 0

for i in str(BASE ** POWER):
    digit_sum = digit_sum + int(i)

print digit_sum

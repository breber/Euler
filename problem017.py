'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
def build_str(num):
    to_ret = ""
    if num >= 1000:
        num_str = str(num)
        num = int(num_str[-3:])
        to_ret = to_ret + build_str(int(num_str[:-3])) + "thousand"
    
    if num >= 100:
        num_str = str(num)
        num = int(num_str[-2:])
        
        if num == 0:
            to_ret = to_ret + build_str(int(num_str[:-2])) + "hundred"
        else:
            to_ret = to_ret + build_str(int(num_str[:-2])) + "hundredand"

    if num >= 20:
        num_str = str(num)
        num = int(num_str[-1:])

        if num_str[0] == '2':
            to_ret = to_ret + "twenty"
        elif num_str[0] == '3':
            to_ret = to_ret + "thirty"
        elif num_str[0] == '4':
            to_ret = to_ret + "forty"
        elif num_str[0] == '5':
            to_ret = to_ret + "fifty"
        elif num_str[0] == '6':
            to_ret = to_ret + "sixty"
        elif num_str[0] == '7':
            to_ret = to_ret + "seventy"
        elif num_str[0] == '8':
            to_ret = to_ret + "eighty"
        elif num_str[0] == '9':
            to_ret = to_ret + "ninety"

    if num >= 10:
        num_str = str(num)
        num = int(num_str[-2:])

        if num_str[1] == '0':
            to_ret = to_ret + "ten"
        elif num_str[1] == '1':
            to_ret = to_ret + "eleven"
        elif num_str[1] == '2':
            to_ret = to_ret + "twelve"
        elif num_str[1] == '3':
            to_ret = to_ret + "thirteen"
        elif num_str[1] == '4':
            to_ret = to_ret + "fourteen"
        elif num_str[1] == '5':
            to_ret = to_ret + "fifteen"
        elif num_str[1] == '6':
            to_ret = to_ret + "sixteen"
        elif num_str[1] == '7':
            to_ret = to_ret + "seventeen"
        elif num_str[1] == '8':
            to_ret = to_ret + "eighteen"
        elif num_str[1] == '9':
            to_ret = to_ret + "nineteen"

    if num == 1:
        to_ret = to_ret + 'one'
    elif num == 2:
        to_ret = to_ret + 'two'
    elif num == 3:
        to_ret = to_ret + 'three'
    elif num == 4:
        to_ret = to_ret + 'four'
    elif num == 5:
        to_ret = to_ret + 'five'
    elif num == 6:
        to_ret = to_ret + 'six'
    elif num == 7:
        to_ret = to_ret + 'seven'
    elif num == 8:
        to_ret = to_ret + 'eight'
    elif num == 9:
        to_ret = to_ret + 'nine'

    return to_ret

def num_letters(num):
    return len(build_str(num))

LIMIT = 1000

sum_val = 0
for i in range(1, LIMIT + 1):
    sum_val = sum_val + num_letters(i)

print sum_val

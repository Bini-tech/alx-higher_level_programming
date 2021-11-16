#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num_last = ((number * -1) % 10) * -1
else:
    num_last = number % 10
if num_last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, num_last))
elif num_last == 0:
    print("Last digit of {} is {} and is 0".format(number, num_last))
elif num_last < 6 and num_last != 0:
    print("Last digit of {} is {} and is less\
 than 6 and not 0".format(number, num_last))

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
str1 = "Last digit of"
str2 = "is"
str3 = ("and is greater than 5, and is 0, and is less than 6 and not 0")
if number < 0:
    num = num * (-1)
if num == 0:
    print(str1, number, str2, num, str3[23:31])
elif num <= 5:
    print(str1, number, str2, num, str3[33:])
else:
    print(str1, number, str2, num, str3[0:21])

# program to solve problem 21 on projecteuler.net by Luc VuTuan

import math
import time


def sum_of_divisors(numbers):
    sum_divisor = 1
    for n in range(2, int(math.sqrt(numbers)) + 1):
        if numbers % n == 0:
            sum_divisor += n
            sum_divisor += numbers / n  # if n is divisor, so is number / n
    return sum_divisor                 # eg: 2 is divisor of 24, so is 12


def is_prime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < math.sqrt(n) + 1:
        if n % p == 0:
            return False
        p += 2
    return True


sum_amicable = 0
start = time.time()
for number in range(1, 10000):
    if not is_prime(number):
        temp = sum_of_divisors(number)       # d(a) = b
        if sum_of_divisors(temp) == number:  # if d(b) = a
            if temp != number:               # and if a != b
                sum_amicable += number

print sum_amicable
print time.time() - start

Output:
root@luc-pc:/home/lucvutuan/PycharmProjects/Exercises# python AmicableNumbers.py 
31626
0.0784718990326

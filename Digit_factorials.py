# program to solve problem 34 on projecteuler.net
# the reason why 1.500.000 should be upper-bound limit
# can be referred here: https://blog.dreamshire.com/project-euler-34-solution/
# the rest has nothing to explain, cause it totally straight codes

import math
import time

start = time.time()
total = 0


for number in range(10, 1500000):
    sum_fact = 0
    temp = number

    while temp > 0:
        mod = temp % 10
        temp = temp / 10
        sum_fact += math.factorial(mod)

    if sum_fact == number:
        print sum_fact
        total += sum_fact
print total, (time.time() - start)


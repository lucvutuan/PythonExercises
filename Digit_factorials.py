# program to solve problem 34 on projecteuler.net
# the reason why 1.500.000 should be upper-bound limit
# can be referred here: https://blog.dreamshire.com/project-euler-34-solution/
# the rest has nothing to explain, cause it totally straight codes


# updated: I figured it out that, if we create a dictionary of factorials of digits
# from 1 to 9 to look up, it would be faster than we calculate the factorial again and again.
# so the program could be updated like:
import math
import time

start = time.time()
total = 0

# update: create a dict of factorials of digits from 1 to 9 to look up
list_fact = {i: math.factorial(i) for i in range(10)}
for number in range(10, 1500000):
    sum_fact = 0
    temp = number

    while temp > 0:
        mod = temp % 10
        temp = temp / 10
        # sum_fact += math.factorial(mod)
        # update:
        sum_fact += list_fact[mod]

    if sum_fact == number:
        print sum_fact
        total += sum_fact
print total, (time.time() - start)


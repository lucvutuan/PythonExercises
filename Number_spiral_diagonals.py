# program to solve problem 28 on projecteuler.net by Luc VuTuan

import math

'''
for n x n spiral which n is odd
- the top right will be pow(n,2)
- the top left is equal to (top_right - n + 1) = pow(n,2) - n + 1
- the bottom left will be pow(n-1,2) + 1 = pow(n,2) - 2*n + 2
- the bottom right will be equal to (bottom_left - n + 1) = pow(n,2) - 3*n + 3
- sum all of them we have: 4 * pow(n,2) - 6 * n + 6
- so we run the loop from 3 to 1001 (increment of 2) and add up the results
- and add the result to 1 (which is centre of the form)
'''
total = 0
for n in range(3, 1003, 2):
    total += 4 * pow(n,2) - 6 * n + 6

print total + 1

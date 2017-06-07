# program to solve problem 29 on projecteuler.net by Luc VuTuan
import time

start = time.time()
list_power = []
for a in range(2, 101):
    for b in range(2,101):
        list_power.append(a**b)

print len(set(list_power))
print time.time() - start
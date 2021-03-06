"""
Problem 14 on projecteuler.net using python

The following iterative sequence is defined for the set of positive integers:

n -> n/2    (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

--------------------------------------------

Firstly when I came up with the problem, I tried to approach it in a classical way, which was using while loop to search each and every number from 1 -> 1.000.000. Something like this (I did this exercise few days ago, so the program using while loop is not now present on my pc, that 's why I just copy some while loop from the others):

----------------------------------------------------
import time
start = time.time()
result = 0
longest = 1
for number in range(500001, 1000000, 2):
    count = 1
    temp = number
    while temp != 16:
        if temp % 2 == 0:
            temp >>= 1
        else:
            temp = 3 * temp + 1
        count += 1

    if longest < count:
        longest = count
        result = number

print result, time.time() - start
----------------------------------------------------
The output is: 837799 4.7966029644

The result is correct, and finishing it in 4.7s is not so bad shot. But then, when I took a look closer to the sequence of any number, I found these key points:
  1. We dont need to check the collatz_sequence of number (n) if it is already shown up in the chain of any number.
  2. If the number is even, for example the number 8 - which has the collatz_sequence is 4. It is equal to 1 + collatz(8/2).
  3. If the number is odd, for example the number 5. Following an odd number, always be an even number (in this case is 16).      Because the formula to generate the collatz sequence if the number is odd is: 3 * n + 1. And if number is even, we came      back with key-point number 2. Which means: if number is odd -----> then collatz_of_number is 1 + collatz(3 * n + 1)
  # Why does it always have 1 + something??? Because every number has its own-self in the chain of collatz sequence.

  So, with those 3 key points, I came up with the algorithm like this:
  - With the key-point number 1: we create a list to look up if the number to find out the collatz sequence is already in the     list or not. i.e my_dict = {1 : 1} #yes, just give it some values to check if the number in the list or not.
  - With the key-point number 2: if number is even ----> return 1 + collatz_sequence of this number divided by 2. i.e:
    if n % 2 == 0: return 1 + collatz(n / 2)
   - With the key-point number 3: if the number is odd ----> return 1 + collatz_sequence of the number after this. i.e
     if n % 2 == 0: return 1 + collatz(3 * n + 1)

  In python, it should be like:

---------------------------------------------------------------
my_dict = {1: 1}
def collatz_sequence(n):
    if n in my_dict:
        return my_dict[n]
    elif n % 2 == 0:
        my_dict[n] = 1 + collatz_sequence(n / 2)
    else:
        my_dict[n] = 1 + collatz_sequence((3 * n) + 1)

    return my_dict[n]
---------------------------------------------------------------

Running the above algorithm, with the range from 1 to 1000000, we found: 837799 in 1.18671584129s. Which is pretty fast (3s faster than the while-loop algorithm). This is good isnt it? Yes, it is. The case was closed. Back to few days ago, I was so satisfied with this algorithm. But back to the day before yesterday, when I sat in the chair and do nothing, I wrote down this problem again, and I found one thing even more interestinng than those key-points I found before. It is: it is always an even number after an odd. Which mean: Eg: collatz(5) = 1 + collatz(16) = 1 + 1 + collatz(16/2) = 2 + collatz(8) - which is (3 * 5 + 1) / 2. Or we can write:
  - if n is odd, then return 1 + collatz_sequence(3 * n + 1) = 1 + 1 + collatz_sequence((3*n+1) / 2). Change the code using this idea, we have:

---------------------------------------------------------------
  def collatz_sequence(n):
    if n in my_dict:
        return my_dict[n]
    elif n % 2 == 0:
        my_dict[n] = 1 + collatz_sequence(n / 2)
    else:
        my_dict[n] = 2 + collatz_sequence(((3 * n) + 1) / 2)

    return my_dict[n]
---------------------------------------------------------------

Run this new function, the output is: found 837799 in 0.970762014389s with the range of (1, 1000000).
My final program is:
"""

import time
my_dict = {1: 1}
def collatz_sequence(n):
    if n in my_dict:
        return my_dict[n]
    elif n % 2 == 0:
        my_dict[n] = 1 + collatz_sequence(n / 2)
    else:
        my_dict[n] = 2 + collatz_sequence(((3 * n) + 1) / 2)

    return my_dict[n]

maxLength = 0
maxNum = 0

start = time.time()
for x in range(1, 1000000):
    temp = collatz_sequence(x)

    if temp > maxLength:
        maxLength = temp
        maxNum = x

print "The number %s has %s numbers in the chain" % (maxNum, maxLength)
print "Finish in %s seconds" % (time.time() - start)

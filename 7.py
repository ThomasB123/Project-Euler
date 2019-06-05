# 10001st prime
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
# Answer = 104743

import math
number = 1
count = 1
while count < 10001:
    number += 2
    prime = True
    for x in range(2,int(math.sqrt(number)+1)):
        if number % x == 0:
            prime = False
            break
    if prime:
        count += 1
print(number)
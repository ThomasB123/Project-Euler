# Largest prime factor
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
# Answer: 6857

import math
num = 600851475143
x = int(math.sqrt(num))
while x > 0:
    if num % x == 0:
        factor = True
        for i in range(2,x):
            if x % i == 0:
                factor = False
        if factor:
            print(x)
            break
    x -= 1
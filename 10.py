# Summation of primes
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
# Answer = 142913828922

import math
answer = 2
x = 3
while x < 2000000:
    prime = True
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            prime = False
            break
    if prime:
        answer += x
    x += 2
print(answer)
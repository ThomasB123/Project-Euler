# Smallest multiple
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# Answer: 232792560

x = 100000000
found = False
while not found:
    x += 20
    found = True
    for i in range(2,21):
        if x % i != 0:
            found = False
print(x)
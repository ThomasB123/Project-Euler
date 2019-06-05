# Largest palindrome product
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
# Answer: 906609

def palindrome(s):
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False

large = 0
for x in range(1000,900,-1):
    for y in range(1000,900,-1):
        if palindrome(str(x*y)):
            large = max(large,x*y)
print(large)
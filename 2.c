// Even Fibonacci numbers
/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
*/
// Answer: 4613732

#include <stdio.h>
int main()
{
    int x = 4000000;
    int out = 0;
    int a = 1;
    int b = 1;
    int temp;
    while (b < x)
    {
        if (b % 2 == 0)
        {
            out += b;
        }
        temp = a;
        a = b;
        b += temp;
    }
    printf("%d\n", out);
    return 0;
}
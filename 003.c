// Largest prime factor
/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/
// Answer: 6857

#include <stdio.h>
#include <stdbool.h>
#include <math.h>
long num = 600851475143;
int x;
bool factor;
int main(){
    x = floor(sqrt(num));
    while (x > 0)
    {
        if (num % x == 0)
        {
            factor = true;
            for (int i = 2; i < x; i++)
            {
                if (x % i == 0)
                {
                    factor = false;
                }
            }
            if (factor)
            {
                printf("%d\n", x);
                break;
            }
        }
        x -= 1;
    }
    return 0;
}
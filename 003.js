// Largest prime factor
/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/
// Answer: 6857

num = 600851475143;
x = Math.round(Math.sqrt(num));
while (x > 0) {
    if (num % x == 0) {
        factor = true;
        for (i = 2; i < x; i++) {
            if (x % i == 0) {
                factor = false;
            }
        }
        if (factor) {
            console.log(x);
            break;
        }
    }
    x -= 1;
}
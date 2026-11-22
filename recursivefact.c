#include <stdio.h>

long long factorial(int n) { // ----> O(n)
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    printf("Factorial = %lld\n", factorial(n));

    return 0;
}

// T(n) = T(n-1) + c (Recurrence Relation)
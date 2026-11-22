#include <stdio.h>

int main() {
    int n, i;
    long long fact = 1;

    printf("Enter a number: ");
    scanf("%d", &n);

    for(i = 1; i <= n; i++) { // --->> loop runs 'n' times  O(n)
        fact = fact * i;
    }

    printf("Factorial = %lld\n", fact);

    return 0;
}

// T(n) = T(n-1) + c (Recurrence Relation)
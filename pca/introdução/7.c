#include <stdio.h>

int main() {
    int x[10];
    int t;

    for (t = 0; t < 10; t++) {
        x[t] = t * 2;
        printf("%d\n", x[t]);
    }

    for (t = 0; t < 10; t++) {
        x[t] = (t * 2) - 1;
        printf("%d\n", x[t]);
    }

    return (0);
}
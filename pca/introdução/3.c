#include <stdio.h>

int main() {
    int a;

    printf("Digite um a inteiro: ");
    scanf("%d", &a);

    if (a % 2 == 0) {
        printf("O a %d e par.\n", a);
    } 
    else {
        printf("O a %d e impar.\n", a);
    }

    return (0);
}
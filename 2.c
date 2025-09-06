#include <stdio.h>

int main() {
    int a, b;

    printf("Digite o primeiro numero inteiro: ");
    scanf("%d", &a);

    printf("Digite o segundo numero inteiro: ");
    scanf("%d", &b);

    if (a < b) {
        printf("O menor numero e: %d\n", a);
    } 
    else if (b < a) {
        printf("O menor numero e: %d\n", b);
    } 
    else {
        printf("Os numeros sao iguais: %d = %d\n", a, b);
    }

    return 0;
}
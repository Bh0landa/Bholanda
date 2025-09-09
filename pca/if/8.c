#include <stdio.h>

int main() {
    float a;

    printf("Digite o valor do salrio: ");
    scanf("%f", &a);

    if (a <= 300) {
        a = a + (a * 0.35);
        printf("O novo valor do salrio com aumento de 35%%: %.2f\n", a);
    }
    else {
        a = a + (a * 0.15);
        printf("O novo valor do salrio com aumento de 15%%: %.2f\n", a);
    }

    return 0;
}
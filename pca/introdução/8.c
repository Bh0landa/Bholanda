#include <stdio.h>
int main() {
    float vnota[10], media, soma = 0;

    for (int i = 0; i < 10; i++) {
        printf("informe a nota: ");
        scanf("%f", &vnota[i]);
        soma += vnota[i];
    }
    media = soma / 10;
    printf("A media e: %.2f\n", media);
    
    return (0);
}
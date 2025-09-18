#include <stdio.h>
#define TAMMAX 10
int main() {
    float v_nota[TAMMAX], media, soma = 0;

    for (int i = 0; i < TAMMAX; i++) {
        printf("informe a nota: ");
        scanf("%f", &v_nota[i]);
        soma += v_nota[i];
    }
    media = soma / TAMMAX;

    for (int i = 0; i < TAMMAX; i++) {
        if (v_nota[i] > media) {
            printf("nota maior que a media: %.2f\n", v_nota[i]);
        }
    }
    printf("A media e: %.2f\n", media);

    return (0);
}
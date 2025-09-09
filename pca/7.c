#include <stdio.h>
#include <ctype.h>
#define tp 6

int main() {
    int idade[tp], contador = 0, soma_idade = 0, qtd_altura = 0, qtd_azul = 0, qtd_ruiva = 0;
    float peso[tp], altura[tp];
    char olhos[tp], cabelo[tp];

    for (int i = 0; i < tp; i++) {
        printf("Pessoa %d:\n", i + 1);
        printf("Idade: ");
        scanf("%d", &idade[i]);
        printf("Peso: ");
        scanf("%f", &peso[i]);
        printf("Altura: ");
        scanf("%f", &altura[i]);
        printf("Cor dos olhos (A-azul, P-preto, V-verde): ");
        scanf(" %c", &olhos[i]);
        printf("Cor dos cabelos (P-preto, C-castanho, L-loiro, R-ruivo): ");
        scanf(" %c", &cabelo[i]);
        printf("\n");
    }

    for (int i = 0; i < tp; i++) {
        if (idade[i] > 50 && peso[i] < 60) {
            contador++;
        }
    }

    if (contador == 0) {
        printf("Nenhuma pessoa com idade > 50 e peso < 60\n");
    }

    printf("Quantidade de pessoas com idade > 50 e peso < 60: %d\n", contador);

    for (int i = 0; i < tp; i++) {
        if (altura[i] < 1.50) {
            soma_idade += idade[i];
            qtd_altura++;
        }
    }

    if (qtd_altura > 0) {
        printf("Media da idade das pessoas com altura < 1.50: %.2f\n", (float)soma_idade / qtd_altura);
    }
    
    else {
        printf("Nenhuma pessoa com altura < 1.50\n");
    }

    for (int i = 0; i < tp; i++) {
        if (toupper(olhos[i]) == 'A') {
            qtd_azul++;
        }
    }

    if (qtd_azul == 0) {
        printf("Nenhuma pessoa com olhos azuis\n");
    }

    float porcentagem = (qtd_azul / (float)tp) * 100;
    printf("Porcentagem de pessoas com olhos azuis: %.2f%%\n", porcentagem);

    for (int i = 0; i < tp; i++) {
        if ((toupper(cabelo[i]) == 'R') && (toupper(olhos[i]) != 'A')) {
            qtd_ruiva++;
        }
    }

    if (qtd_ruiva == 0) {
        printf("Nenhuma pessoa com cabelos ruivos e olhos nao azuis\n");
    }

    float porcentagem_ruiva = (qtd_ruiva / (float)tp) * 100;
    printf("Porcentagem de pessoas com cabelos ruivos (e olhos nao azuis): %.2f%%\n", porcentagem_ruiva);

    return 0;
}
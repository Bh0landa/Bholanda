#include <stdio.h>

int main() {
    int i, idade, soma_idades = 0, cont_peso_altura = 0, cont_mais190 = 0, cont_10a30_mais190 = 0;
    float peso, altura;

    for (i = 1; i <= 10; i++) {
        printf("Pessoa %d - Digite a idade: ", i);
        scanf("%d", &idade);
        printf("Digite o peso (kg): ");
        scanf("%f", &peso);
        printf("Digite a altura (m): ");
        scanf("%f", &altura);

        soma_idades += idade;

        if (peso > 90 && altura < 1.5) {
            cont_peso_altura++;
        }
        if (altura > 1.9) {
            cont_mais190++;
            if (idade >= 10 && idade <= 30) {
                cont_10a30_mais190++;
            }
        }
    }

    printf("\nMédia das idades: %.2f\n", soma_idades / 10.0);
    printf("Quantidade de pessoas com peso > 90kg e altura < 1,50m: %d\n", cont_peso_altura);
    if (cont_mais190 > 0) {
        printf("Porcentagem de pessoas com idade entre 10 e 30 anos entre as que medem mais de 1,90m: %.2f%%\n", (cont_10a30_mais190 * 100.0) / cont_mais190);
    } else {
        printf("Nenhuma pessoa mede mais de 1,90m.\n");
    }

    return 0;
}

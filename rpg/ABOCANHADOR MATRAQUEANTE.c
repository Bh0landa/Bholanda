#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "");

    int quantidade;
    printf("Digite o quantidade da lista: ");
    scanf("%d", &quantidade);

    int *lista = (int*) malloc(quantidade * sizeof(int));
    if (lista == NULL) {
        printf("Erro ao alocar memória!\n");
        return 1;
    }

    // Inicializa todos os valores com 67
    for (int i = 0; i < quantidade; i++) {
        lista[i] = 67;
    }

    // Permite ao usuário alterar valores até decidir parar
    char opcao;
    do {
        printf("Deseja alterar algum valor da lista? (s/n): ");
        scanf(" %c", &opcao);

        if (opcao == 's' || opcao == 'S') {
            int indice, numero;
            char operacao;
            printf("Digite o índice do item que deseja alterar (0 a %d): ", quantidade - 1);
            scanf("%d", &indice);

            if (indice >= 0 && indice < quantidade) {
                printf("Deseja somar (+) ou subtrair (-) ao valor atual? ");
                scanf(" %c", &operacao);
                printf("Digite o número para a operação: ");
                scanf("%d", &numero);

                if (operacao == '+') {
                    lista[indice] += numero;
                } else if (operacao == '-') {
                    lista[indice] -= numero;
                } else {
                    printf("Operação inválida!\n");
                }
            } else {
                printf("Índice inválido!\n");
            }
        }
    } while (opcao == 's' || opcao == 'S');

    // Mostra a lista final
    printf("Valores da lista:\n");
    for (int i = 0; i < quantidade; i++) {
        printf("%d ", lista[i]);
    }
    printf("\n");

    free(lista); // Libera a memória alocada
    return 0;
}
#include <stdio.h>
#include <ctype.h>

int main() {
    char codigo;
    float valor, total_vista = 0, total_prazo = 0, total_geral = 0;
    int i;

    for (i = 1; i <= 15; i++) {
        printf("Transacao %d - Digite o codigo (V para a vista, P para a prazo): ", i);
        scanf(" %c", &codigo);
        codigo = toupper(codigo);
        printf("Digite o valor da transacao: R$");
        scanf("%f", &valor);

        if (codigo == 'V') {
            total_vista += valor;
        }
        
        else if (codigo == 'P') {
            total_prazo += valor;
        }
        
        else {
            printf("Codigo invalido! Considere apenas V ou P.\n");
            i--;
            continue;
        }
        total_geral += valor;
    }

    printf("\nTotal das compras a vista: R$%.2f\n", total_vista);
    printf("Total das compras a prazo: R$%.2f\n", total_prazo);
    printf("Total das compras efetuadas: R$%.2f\n", total_geral);
    printf("Valor da primeira prestacao das compras a prazo juntas: R$%.2f\n", total_prazo / 3);

    return 0;
}

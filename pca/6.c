#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "");

    float nota, soma = 0, media;
    int quantidade = 0;

    printf("Digite as notas dos alunos (digite -1 para encerrar):\n");

    while (1) {
        printf("Nota: ");
        scanf("%f", &nota);

        if (nota == -1) {
            break;
        }

        if (nota < 0 || nota > 10) {
            printf("Nota invalida! Digite um valor entre 0 e 10.\n");
            continue;
        }

        soma += nota;
        quantidade++;
    }

    if (quantidade > 0) {
        media = soma / quantidade;
        printf("Media da turma: %.2f\n", media);
    } else {
        printf("Nenhuma nota foi informada.\n");
    }

    return 0;
}
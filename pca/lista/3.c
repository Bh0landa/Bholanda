#include <stdio.h>
#define T 6

int main() {
    int f[T], n, v;
    printf("Digite quantas vezes o dado sera jogado: \n");
    scanf("%d", &n);

    for (int i = 0; i < T; i++) {
        f[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        printf("Digite o valor do dado: \n");
        scanf("%d", &v);
        f[v - 1]++;
    }

    printf("Face\tFrequencia\n");
    for (int i = 0; i < T; i++) {
        printf("%d\t%d\n", i + 1, f[i]);
    }

    return 0;
}
#include <stdio.h>

#define VET_TAM 4

int main()
{
    int vet[VET_TAM];

    for(int i = 0; i < VET_TAM; i ++){
        printf("Informe o valor do elemento vet[%d]:\n", i);
        scanf("%d", &vet[i]);
    }

    for(int i =0; i < VET_TAM; i++){
        printf("vet[%d] = %d\n", i, vet[i]);
    }

    return (0);
}
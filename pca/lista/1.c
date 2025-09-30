#include <stdio.h>

int main(){
    int n;
    printf("Defina o tamanho da lista: \n");
    scanf("%d", &n);
    int lista[n];

    for(int i = 0; i < n; i++){
        printf("Digite o valor da posicao %d: \n", i+1);
        scanf("%d", &lista[i]);
    }

    for(int i = n-1; i >= 0; i--){
        printf("O valor da posicao %d e: %d\n", i+1, lista[i]);
    }
}
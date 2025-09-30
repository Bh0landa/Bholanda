#include <stdio.h>
#define T 10

 int main(){
    int n[T], m[T], p[T], soma = 0;

    for(int i = 0; i < T; i++){
        printf("Informe o valor do vetor a[%d]:\n", i);
        scanf("%d", &n[i]);
    }

    for(int i = 0; i < T; i++){
        printf("Informe o valor do vetor b[%d]:\n", i);
        scanf("%d", &m[i]);
    }

    for(int i = 0; i < T; i++){
    p[i] = n[i] * m[i];
    }

    for(int i = 0; i < T; i++){
        soma += p[i];
    }
    printf("O produto escalar entre os vetores a e b e: %d\n", soma);
    
    return (0);
 }
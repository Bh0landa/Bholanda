#include <stdio.h>

int main() {
    float preco, novo_preco;
    int percentual;
    char *classificacao;

    printf("Digite o preço do produto: R$ ");
    scanf("%f", &preco);

    if (preco <= 50.0) {
        percentual = 5;
    }
    
    else if (preco <= 100.0) {
        percentual = 10;
    }
    
    else {
        percentual = 15;
    }

    novo_preco = preco + (preco * percentual / 100.0);

    if (novo_preco <= 80.0) {
        classificacao = "Barato";
    }
    
    else if (novo_preco <= 120.0) {
        classificacao = "Normal";
    }
    
    else if (novo_preco <= 200.0) {
        classificacao = "Caro";
    }
    
    else {
        classificacao = "Muito caro";
    }

    printf("Novo preço: R$ %.2f\n", novo_preco);
    printf("Classificação: %s\n", classificacao);

    return 0;
}
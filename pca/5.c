#include<stdio.h>
int main(){
    int op;
    do{
        printf("Digite a opssao desejada:\n");
        printf("1 - Cadastrar\n");
        printf("2 - Consultar\n");
        printf("3 - Excluir\n");
        printf("4 - Sair\n");
        scanf("%d", &op);
        
        switch(op){
            case 1:
                printf("Cadastrado com sucesso!\n");
                break;
            case 2:
                printf("Consulta realizada com sucesso!\n");
                break;
            case 3:
                printf("Exclusao realizada com sucesso!\n");
                break;
            case 4:
                printf("Saindo...\n");
                break;
            default:
                printf("Opssao invalida!\n");
        }
    }
    while (op !=4);
    return 0;
}
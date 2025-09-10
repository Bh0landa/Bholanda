#include <stdio.h>
#define x 8
int main() {
    int idade[x], cont1 = 0, cont2 = 0, cont3 = 0, cont4 = 0, count5 = 0;

    for ( int i = 0; i < x; i++) {
        printf("Digite a idade da pessoa %d: ", i + 1);
        scanf("%d", &idade[i]);
    }

    for (int i = 0; i < x; i++) {
        if (idade[i] <=15) {
            cont1++;
        }
        else if (idade[i] > 15 && idade[i] <=30) {
            cont2++;
        }
        else if (idade[i] > 30 && idade[i] <=45) {
            cont3++;
        }
        else if (idade[i] > 45 && idade[i] <=60) {
            cont4++;
        }
        else {
            count5++;
        }
    }

    if (cont1 > 0) {
        printf("A primeira faixa etaria tem %d pessoa(s) e representa %.2f%% em relacao ao total\n", cont1, (cont1 / (float)x) * 100);
    }
    
    else {
        printf("Nao a nimguem na primeira faixa etaria\n");
    }

    if (cont2 > 0) {
        printf("A segunda faixa etaria tem %d pessoa(s)\n", cont2);
    }
    
    else {
        printf("Nao a nimguem na segunda faixa etaria\n");
    }

    if (cont3 > 0) {
        printf("A terceira faixa etaria tem %d pessoa(s)\n", cont3);
    }
    
    else {
        printf("Nao a nimguem na terceira faixa etaria\n");
    }

    if (cont4 > 0) {
        printf("A quarta faixa etaria tem %d pessoa(s)\n", cont4);
    }
    
    else {
        printf("Nao a nimguem na quarta faixa etaria\n");
    }

    if (count5 > 0) {
        printf("A quinta faixa etaria tem %d pessoa(s) e representa %.2f%% em relacao ao total\n", count5, (count5 / (float)x) * 100);
    }
    
    else {
        printf("Nao a nimguem na quinta faixa etaria\n");
    }

    return 0;
}
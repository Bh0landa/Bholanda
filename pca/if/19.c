#include <stdio.h>
#include <ctype.h>

int main() {
    float h, x;
    char s;

    printf("Digite sua haltura: ");
    scanf("%f", &h);
    printf("Digite seu sexo (M/F): ");
    scanf(" %c", &s);

    if (toupper(s) == 'F') {
        x = 62.1 * h - 44.7;
    }
    
    else {
        x = 72.7 * h - 58;
    }
    printf("Seu peso ideal eh: %.2f\n", x);

    return 0;
}
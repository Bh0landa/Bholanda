package aula3;

public class Operadores {
    public static void main(String[] args) {
        //Aritméticos +, -, /, *

        int number1 = 10;
        int number2 = 20;

        System.out.println("soma 10 + 20 = " + (number1 + number2));
        System.out.println("subtração 10 - 20 = " + (number1 - number2));
        System.out.println("multiplicação 10 * 20 = " + (number1 * number2));
        System.out.println("divisão 10 / 20 = " + (number1 / (double) number2)); //casting feito apenas para exemplificar, não é uma boa prática

        //Resto %

        int rest = 21 % 7;

        System.out.println("Resto da divisão de 21 por 7 = " + rest);

        //Relacionais <, >, <=, >=, ==, !=

        boolean isNumber1LessThanNumber2 = number1 < number2;
        boolean isNumber1GreaterThanNumber2 = number1 > number2;
        boolean isNumber1EqualToNumber2 = number1 == number2;
        boolean isNumber1NotEqualToNumber2 = number1 != number2;

        System.out.println("10 é menor que 20? " + isNumber1LessThanNumber2);
        System.out.println("10 é maior que 20? " + isNumber1GreaterThanNumber2);
        System.out.println("10 é igual a 20? " + isNumber1EqualToNumber2);
        System.out.println("10 é diferente de 20? " + isNumber1NotEqualToNumber2);

        //Lógicos &&, ||, !

        boolean hasMoney = true;
        boolean isHealthy = false;
        boolean canGoOut = hasMoney && isHealthy;
        boolean canBuyIceCream = hasMoney || isHealthy;
        boolean cannotGoOut = !canGoOut;
        
        System.out.println("Pode sair? " + canGoOut);
        System.out.println("Pode comprar sorvete? " + canBuyIceCream);
        System.out.println("Não pode sair? " + cannotGoOut);

        //Atribuição =, +=, -=, /=, *=, %=

        double bonus = 1800;

        bonus += 1000; //2800
        bonus -= 500; // 1800
        bonus /= 2; // 900
        bonus *= 2; // 1800
        bonus %= 1000; // 800

        System.out.println("Bônus: " + bonus);
        
        //Unário ++, --

        int counter1 = 0;
        int counter2 = 0;

        counter1++;
        counter2--;

        System.out.println("countador1: " + counter1);
        System.out.println("countador2: " + counter2);
    }
    
}
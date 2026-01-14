package aula2;
/*
Crie variaveis para os campos descritos abaixo entre <> e imprima a seguinte mensagem

Eu <name>, morando na <adress>, confirmo que recebi o salario de R$ <salary> na data <date>.
*/

public class Exercicio {
    public static void main(String[] args) {
        String name = "Almo Çaar";
        String adress = "Rua dos Bobos número 0 ";
        double salary = 5431.12;
        String date = "10/05/2024"; 
        // a duas formas de fazer
        //1
        System.out.println("Eu " + name + ", morando na " + adress + ", confirmo que recebi o salario de R$ " + salary + " na data " + date + ".");

        //2
        String message = String.format("Eu %s, morando na %s, confirmo que recebi o salario de R$ %.2f na data %s.", name, adress, salary, date);

        System.out.println(message);

        //2.5
        String message2 = ("Eu " + name + ", morando na " + adress + ", confirmo que recebi o salario de R$ " + salary + " na data " + date + ".");

        System.out.println(message2);
    }

}
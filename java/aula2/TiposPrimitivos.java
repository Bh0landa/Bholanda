package aula2;

public class TiposPrimitivos {
    public static void main(String[] args) {
        //int, double, float, char, byte, short, long, boolean

        int age = 10;
        double salary = 2000.00;
        float salaryFloat = 2500.00F;
        char caracter = 65; // ou 'A'
        byte ageByte = 10;
        short ageShort = 10;
        long bigNumber = 10000000000L;
        boolean trueValue = true;
        boolean falseValue = false;

        System.out.println("idade: " + age + " anos");
        System.out.println("salario: R$ " + salary);
        System.out.println("salario float: R$ " + salaryFloat);
        System.out.println("caracter: " + caracter);
        System.out.println("idade byte: " + ageByte + " anos");
        System.out.println("idade short: " + ageShort + " anos");
        System.out.println("big number: " + bigNumber);
        System.out.println("valor booleano verdadeiro: " + trueValue);
        System.out.println("valor booleano falso: " + falseValue);

        //casting
        int forceint = (int) 10000000000L; //(int) para forçar um long em um int
        float forcefloat = (float) 2500.00D; //(float) para forçar double em um float
        long forceLong = (long) 155.00; //(long) para forçar double em long
        
        System.out.println("força long convertida para int: " + forceint);
        System.out.println("força double convertida para float: " + forcefloat);      
        System.out.println("força double convertida para long: " + forceLong);
        
        //Stings
        String name = "Almo Çaar";

        System.out.println("meu nome é " + name);
    }

}
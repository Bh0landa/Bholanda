package aula4;

public class EstruturasCondicionais {
    public static void main(String[] args) {
        
        int age = 20;
        boolean hasAuthorization = age >= 18;

        if (hasAuthorization) {
            System.out.println("Autorizado a comprar bebida alcoólica");
        }

        if(!hasAuthorization) {
            System.out.println("Não autorizado a comprar bebida alcoólica");
        }

        System.out.println("Fora do if");
        
    }
    
}

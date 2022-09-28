



import java.util.Scanner;


class Main {
    public static void main(String[] args) throws Exception { 
        //Leitura dos dados 
        System.out.println("Insira o coeficiente a:");
        int a = EntradaTeclado.leInt();
        
        System.out.println("Insira o coeficiente b:");
        int b = EntradaTeclado.leInt();

        System.out.println("Insira o coeficiente c:");
        int c = EntradaTeclado.leInt();

        //Verificação do delta
        double deltaAux = (b*b) - 4*a*c;
        if(deltaAux < 0){
            System.out.println("Delta menor que 0");
            return;
        } 

        //Calculo
        double delta = Math.sqrt( deltaAux );
        double X1 = (delta - b)/2*a; 
        double X2 = (delta + b)/2*a;
        
        //Saida
        System.out.printf("X1 = %f \n", X1);
        System.out.printf("X2 = %f \n", X2);
    }
}


import java.util.Scanner;

class Main {
    public static void main(String[] args) {

        //Inicialização para leitura
        Scanner cx = new Scanner(System.in);
        double x;

        //Leitura do valor a ser calculado
        System.out.println("Digite o número a ser calculado:");
        x = cx.nextDouble();


        //Leitura do chute inicial
        System.out.println("Digite o chute:");
        double x_0 = cx.nextDouble();

        //Calculo
        double xAux = 0;
        while( (x_0 - xAux) > 0.00000001)
        {
            xAux = x_0;
            x_0 = ( xAux + (x/xAux) ) / 2;
        }

        //Saída do programa
        System.out.println("Resultado:");
        System.out.println(x_0);
        
    }
}





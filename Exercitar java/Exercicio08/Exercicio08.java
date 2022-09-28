
import java.lang.Math;


class Main{
    
    /*
        Função dada:
            f(x) = x^3 - x^2 - 13x + 8
    */ 
    static double f(double x){
        return ( (x*x*x) - (x*x) -(13*x) +8 );
    }

    /*
        Derivada da função dada:
            f'(x) = 3x^2 - 2x  - 13
    */ 
    static double f_linha(double x){
        return ( (3*x*x) - 2*x -13 );
    }
    
    public static void main(String[] args) throws Exception {

        //Leitura e declaração inicial
        System.out.printf("Insira o chute inicial:\n");
        double raiz_chute = EntradaTeclado.leDouble();
        double raiz = 0;

        //Primeira iteração
        raiz = raiz_chute - (f(raiz_chute)/f_linha(raiz_chute));
        
        //Loop de calculo
        while(Math.abs(raiz_chute - raiz) > 0.00000001){
            System.out.printf("===== Entrou no loop =====\n");
            System.out.printf("Raiz chute %f |-| Raiz %f\n");
            
            raiz_chute = raiz;
            raiz = raiz_chute - (f(raiz_chute)/f_linha(raiz_chute));

            System.out.printf("======== Fim do loop =======\n");
            System.out.printf("Raiz chute %f |-| Raiz %f\n");

        }



    }
}
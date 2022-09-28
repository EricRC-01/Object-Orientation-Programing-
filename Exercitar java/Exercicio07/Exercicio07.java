import java.lang.Math;
class Main{
    //Função dada 
    static double f(double x){
        double x2 = x*x, x3 = x*x*x;    
        return (x3 - x2 - (13*x) + 8);
    }


    public static void main(String[] args) throws Exception {

        //Leitura dos valores do dominío 
        double a = 0, b = 0;
        System.out.println("ínsira o primeiro valor do dominio: ");
        a = EntradaTeclado.leDouble();
        System.out.println("ínsira o segundo valor do dominio: ");
        b = EntradaTeclado.leDouble();

        System.out.printf("f(a) = %f\n",f(a));
        System.out.printf("f(b) = %f\n",f(b));

        //Verificar se os números iniciais tem sinais opostos
        if( f(a)*f(b) >= 0){
            System.out.println("Os valores não tem sínais opostos.");
            System.out.println("Logo, não se pode garantir a existência de raízes.");
            return;
        }

        //loop de resolução
        double pontoMedio = (a+b)/2, extremoAux = 0;

        while( Math.abs(pontoMedio - extremoAux) > 0.0000001){
            //Caso: ponto médio e a tenham sinais opostos
            if( f(pontoMedio)*f(a) < 0){
                extremoAux = a;
                b = pontoMedio;
                pontoMedio = (a+pontoMedio)/2;
            }
            //Consequencia: ponto médio e b tem sínais opostos
            else{
                extremoAux = b;
                a = pontoMedio;
                pontoMedio = (b+pontoMedio)/2;
            }
        }
        System.out.printf("A raiz encontrada é: %f\n",pontoMedio);
    }
}
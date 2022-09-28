

class Main{
    public static void main(String[] args) throws Exception {
    
        //Leitura do número 
        System.out.println("Insira o numero :");
        int numero = EntradaTeclado.leInt();

        //Calculo e verificação
        for(int i = 2; i < numero; i++){
            if(numero % i == 0){
                System.out.printf("%d Não é primo! O menor divisor é %d\n",numero,i);
                return;
            }
        }
        System.out.printf("O número %d é primo!\n",numero);
    }
}

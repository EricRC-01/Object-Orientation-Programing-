





class Main{
    
    //Função para verificar se um número é primo
    static boolean serPrimo(int numero){

        //Verificação
        for(int i = 2; i < numero; i++){
            if(numero % i == 0){
                return false;
            }
            
        }
        return true;
    }
    
    
    public static void main(String[] args) throws Exception {
    
        //Leitura do número 
        System.out.println("Insira o numero :");
        int numero = EntradaTeclado.leInt();

        //Declaração das variavéis utilizadas
        int numeroAlvo = numero-1; 
        boolean alvoPrimo = false; //Verifica se o número alvo atual é primo
        
        while(alvoPrimo == false && numeroAlvo > 1){
            numeroAlvo--;            
            alvoPrimo = serPrimo(numeroAlvo);
        }
        if(numeroAlvo == 1){
            System.out.printf("Não existe número primo menor que %d\n",numero);
        }
        if(alvoPrimo == true){
            System.out.printf("O primeiro numero primo menor que %d é %d\n",numero, numeroAlvo);
        }
    }
}

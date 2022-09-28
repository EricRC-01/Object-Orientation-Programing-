

class Main{
    
    public static void main(String[] args) throws Exception {
        
        //Declarações iniciais
        double maior = 0, menor = 0, leitor = 1;
        
        //Primeira leitura 
        System.out.println("insira um número:");
        leitor = EntradaTeclado.leDouble();

        //Primeira atribuição
        if (leitor != 0){ 
            maior = leitor;
            menor = leitor;
        }
        else{
            System.out.printf("====Fim do programa====\n");
            return;
        }


        while( leitor != 0 ){

            //Ler novo número
            System.out.println("insira um número:");
            leitor = EntradaTeclado.leDouble();

            //Definir maior e menor
            if (leitor <= menor && leitor != 0) menor = leitor;

            else if (leitor > maior && leitor != 0) maior = leitor;
            
        }

        //Saída do programa
        System.out.printf("O maior numero lido é: %f\n", maior);
        System.out.printf("O menor numero lido é: %f\n", menor);
        System.out.printf("====Fim do programa====\n");



        return;
    }
}

class Senha{

    public static void main(String[] args) throws Exception {

        //Leitura inicial de N
        System.out.print("Insira o valor de N: ");
        int N = EntradaTeclado.leInt();
        
        //Delcaração do número aleatório positivo
        Random rd = new Random();
        int rnd_num = rd.getIntRand(N);
        if(rnd_num < 0) rnd_num = rnd_num * (-1);

        //Loop de execução do programa
        int chute = 0;
        do{
            chute = EntradaTeclado.leInt();
            
            if(chute > rnd_num) 
                System.out.printf("O chute é maior que o número\n");
            else if (chute < rnd_num) 
                System.out.printf("O chute é menor que o número\n");


        }while(chute != rnd_num);

        System.out.printf("O chute é igual ao número!\n");
    }
}
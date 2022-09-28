


class Main {
    public static void main(String[] args) throws Exception { 
        
        //Leitura  da base da arvore 
        System.out.println("Insira um número : ");
        int baseArv = EntradaTeclado.leInt();

        //Print da arvore
        int qntLinhas = baseArv;
        for(int i = 0; i < qntLinhas; i++){

            for(int j = baseArv; j > 0; j--){
                System.out.printf("*");
                
            }
            baseArv--;
            System.out.println();
        }
    }
}
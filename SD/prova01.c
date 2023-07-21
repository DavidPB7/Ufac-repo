#include <stdio.h>
#include <mpi.h>

/*Definir o grafo da aplicação antes de executar*/
int numeroDeTarefas = 6;
int matrizVizinhanca[6][6] = {{0,1,1,0,0,0},
                              {1,0,1,1,1,0},
                              {1,1,0,0,0,1},
                              {0,1,0,0,0,0},
                              {0,1,0,0,0,0},
                              {0,0,1,0,0,0}};
/*retorna o número de vizinhos da tarefa myRank*/
int contaNumeroDeVizinhos(int myRank)
{
   int i;
   int contador = 0;
   
   for (i = 0; i < numeroDeTarefas; i++)
      if (matrizVizinhanca[myRank][i] == 1)
         contador++;
         
   return contador;
}
/*programa principal*/
int main(int argc, char** argv)
{
   int i;
   int numeroDeVizinhos;
   int myRank;
   int source;
   int tag = 50;
   int pai;
   int contador;
   char message[100] = "Oi!";

   MPI_Status status;
   //inicialização do MPI
   MPI_Init(&argc, &argv);
   MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
   numeroDeVizinhos = contaNumeroDeVizinhos(myRank);


   if (myRank == 0)
	{
           /*enviando para todos os vizinhos de myRank*/
           for (i = 0; i < numeroDeTarefas; i++)	
               if (matrizVizinhanca[myRank][i] == 1)
               {
            	   printf("Enviando a informação para %d\n", i);
		   MPI_Send(message, 100, MPI_CHAR, i, tag, MPI_COMM_WORLD);
		   contador = contador + 1
               }
            
           /*recebendo de todos os vizinhos de myRank*/      
           for (i = 0; i < numeroDeTarefas; i++)
               if (matrizVizinhanca[myRank][i] == 1)
               {
                   printf("Recebendo a informação de %d\n", i);
                   MPI_Recv(message, 100, MPI_CHAR, i, tag,
                     MPI_COMM_WORLD, &status);
               }
   }
   else {

      /*recebendo msg de uma tarefa vizinha qualquer*/
      MPI_Recv(message, 100, MPI_CHAR, MPI_ANY_SOURCE, tag,MPI_COMM_WORLD, &status);
      pai = status.MPI_SOURCE;

      /*enviando para todos os vizinhos de myRank menos seu pai*/
      for (i = 0; i < numeroDeTarefas; i++)	
         if ( (matrizVizinhanca[myRank][i] == 1) && (i != pai) ){
            MPI_Send(message, 100, MPI_CHAR, i, tag, MPI_COMM_WORLD);
         }
      /*recebendo de todos os vizinhos de myRank menos 1*/      
      for(i = 0; i < (numeroDeVizinhos - 1); i++) {	
         MPI_Recv(message, 100, MPI_CHAR, MPI_ANY_SOURCE, tag,MPI_COMM_WORLD, &status);
       }
       MPI_Send(message, 100, MPI_CHAR, pai, tag,MPI_COMM_WORLD);
       if(numeroDeVizinhos == 1) {
	printf("A distancia do nó %d até o fim é de: %d", MyRank,contador);


}
   }
   //Finalização do MPI
   MPI_Finalize();
}

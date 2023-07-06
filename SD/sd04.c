#include <stdio.h>
#include <string.h>
#include <mpi.h>


// 4 - Faça um programa em MPI
// que some duas matrizes 2x2.

int main(int argc, char** argv) {
    int meu_rank, np, origem, destino, tag = 0;
    int valor, velocidade, distancia, tempo;


    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &meu_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &np);
    printf("----------Q4----------");


    if (meu_rank != 0) {
        if(meu_rank == 1) {
            destino = 0;
            printf("Informe uma distancia para o processo %d: ", meu_rank);
            scanf("%d", &valor);
            MPI_Send(&valor, 1, MPI_INT, destino, tag, MPI_COMM_WORLD);
    } else {
            destino = 0;
            printf("Informe um tempo para o processo %d: ", meu_rank);
            scanf("%d", &valor);
            MPI_Send(&valor, 1, MPI_INT, destino, tag, MPI_COMM_WORLD);
        }
    } else {
        for (origem = 1; origem < np; origem++) {
            MPI_Recv(&valor, 1, MPI_INT, origem, tag, MPI_COMM_WORLD, &status);
            lista[origem - 1] = valor;
        }
        distancia = lista[0];
        tempo = lista[1];


        velocidade = distancia/tempo


        printf("Velocidade de  %d\n", velocidade);
    }
   
    MPI_Finalize();
    return 0;
}





#include <stdio.h>
#include <string.h>
#include <mpi.h>

// 1 - Fazer um programa em MPI que
// utilize 3 processos, os processos 1 e 2 devem enviar um valor inteiro para o
// processo 0. O processo 0 deve efetuar as 4 operações básicas com os inteiros
// recebidos (+,-.*,/), após isso deve imprimir os resultados.

void main(int argc, char** argv){
    int meu_rank, np, origem, destino, tag=0;
    int valor, sum, div, sub, mult, v1, v2;
    int lista[2];

    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_COMM_rank(MPI_COMM_WORLD, &meu_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &np);


    if (meu_rank != 0){
        destino = 0;
        printf("Informe um valor inteiro para o processo %d: ", meu_rank);
        scanf("%d", &valor);
        MPI_Send(valor, 1, MPI_INT, destino, tag, MPI_COMM_WORLD);
    }
    else{
        for (origem=1; origem<np; origem++){
            MPI_Recv(&valor, 1, MPI_INT, origem, tag, MPI_COMM_WORLD, &status);
            lista[origem - 1] = valor;
        }
        v1 = lista[0];
        v2 = lista[1];

        sum = v1+v2;
        mult = v1*v2;
        div = v1/v2;
        sub = v1-v2;

        printf("Adição: %d\n", sum);
        printf("Multiplicação: %d\n", mult);
        printf("Subtração: %d\n", sub);
        printf("Divisão: %d\n", div);
    }
    MPI_Finalize();
    return 0;
}

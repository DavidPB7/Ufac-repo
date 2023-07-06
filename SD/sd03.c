#include <stdio.h>
#include <string.h>
#include <mpi.h>
#include <math.h>

// 3 - Faça um programa que
// calcule o quadrado da soma (a + b)2 , em 4 processos: o processo
// ZERO envia “a” para o processo 1, “a” e “b” para o processo 2 e “b” para o
// processo 3. No final cada processo responde com a operação equivalente.

int main(int argc, char** argv) {
    int meu_rank, np, origem, tag = 0;
    int a, b;

    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &meu_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &np);
    printf("----------Q3----------");

   if (meu_rank == 0) {
        printf("Informe o valor do 'a' para o processo: %d\n", meu_rank);
        scanf("%d", &a);

        printf("Informe o valor do 'b' para o processo: %d\n", meu_rank);
        scanf("%d", &b);

        MPI_Send(&a, 1, MPI_INT, 1, tag, MPI_COMM_WORLD);
        MPI_Send(&b, 1, MPI_INT, 2, tag, MPI_COMM_WORLD);

        MPI_Send(&a, 1, MPI_INT, 3, tag, MPI_COMM_WORLD);
        MPI_Send(&b, 1, MPI_INT, 3, tag, MPI_COMM_WORLD);

    } else {
        if(meu_rank == 1) {
            MPI_Recv(&a, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
            printf("O valor do processo %d correspondente a expressão 'a^2' é: %d\n", meu_rank, a*a);

        }
        if(meu_rank == 2) {
            MPI_Recv(&b, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
            printf("O valor do processo %d correspondente a expressão 'b^2' é: %d\n", meu_rank, b*b);

        }
        if(meu_rank == 3) {
            MPI_Recv(&a, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
            MPI_Recv(&b, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
            printf("O valor do processo %d correspondente a expressão '(a+b)^2' é: %d\n", meu_rank, pow(a+b, 2));
        }
    }
    MPI_Finalize();
    return 0;
}

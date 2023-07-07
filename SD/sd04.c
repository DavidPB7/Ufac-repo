#include <stdio.h>
#include <string.h>
#include <mpi.h>

// 4 - Faça um programa em MPI
// que some duas matrizes 2x2.

int main(int argc, char** argv) {
    int meu_rank, np, origem, tag = 0;
    int mat1[2][2] = {{2, 2}, {2, 2}};
    int mat2[2][2] = {{3, 3}, {3, 3}};
    int matS[2][2];

    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &meu_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &np);
    printf("----------Q4----------");

    printf("\n");
    printf("Matriz 01:\n");
    for (int i = 0; i < 2; i++) {
       for (int j = 0; j < 2; j++) {
           printf("(%d) ", mat1[i][j]);
       }
    }

    printf("\n");
    printf("Matriz 02:\n");
    for (int i = 0; i < 2; i++) {
       for (int j = 0; j < 2; j++) {
           printf("(%d) ", mat2[i][j]);
       }
    }

    printf("\n");
    if (meu_rank == 0) {
        MPI_Send(&mat1, 2*2, MPI_INT, 1, tag, MPI_COMM_WORLD);
        MPI_Send(&mat2, 2*2, MPI_INT, 2, tag, MPI_COMM_WORLD);

    } else {
        MPI_Recv(&mat1, 2*2, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
        MPI_Recv(&mat2, 2*2, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
        
        printf("Matriz Soma: \n")
        for(i = 0; i < 3; i++) {
            for(j = 0; j < 3; j++) {
                matS[i][j] = mat1[i][j] + mat2[i][j];   
                printf("(%d)\n", matS[i][j]);
            }
	}
    }
    MPI_Finalize();
    return 0;
}

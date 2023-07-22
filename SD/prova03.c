#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "mpi.h"

int main(int argc, char** argv) {
    int meu_rank, tag = 0;
    int a[1], b[1], matMult[3][3], i, j, r1;

    MPI_Status status;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &meu_rank);

    if (meu_rank == 0) {
        int mata[3][3] = {{1, 2, 3}, 
                          {1, 0, 1}, 
                          {6, 6, 6}};

        int matb[3][3] = {{3, 4, 5}, 
                          {2, 1, 2}, 
                          {3, 3, 3}};
	    
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                a[0] = mata[i][j];
                b[0] = matb[j][i];
                MPI_Send(a, 1, MPI_INT, 1, tag, MPI_COMM_WORLD);
                MPI_Send(b, 1, MPI_INT, 1, tag, MPI_COMM_WORLD);
            }
        }

        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                MPI_Recv(&r1, 1, MPI_INT, 1, tag, MPI_COMM_WORLD, &status);
                matMult[i][j] = r1;
            }
        }

        printf("Resultado:\n");
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                printf("%d\t", matMult[i][j]);
            }
            printf("\n");
        }
    } else {
        for (i = 0; i < 3; i++) {
            for (j = 0; j < 3; j++) {
                MPI_Recv(a, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
                MPI_Recv(b, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
                r1 = a[0] * b[0];
                MPI_Send(&r1, 1, MPI_INT, 0, tag, MPI_COMM_WORLD);
            }
        }
    }

    MPI_Finalize();
}

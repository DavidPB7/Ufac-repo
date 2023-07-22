#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "mpi.h"
int main(int argc, char** argv)
{
        int meu_rank, tag=0;
	int a[3], b[3], matc[3][3], i, j, r1;

        MPI_Status status;
        MPI_Init(&argc, &argv);
        MPI_Comm_rank(MPI_COMM_WORLD, &meu_rank);

	if (meu_rank == 0) {
		int mata[3][3]={{1,2,3,4,5},{1,0,1,8,7},{6,6,6,6,6}};
        	int matb[3][3]={{3,4,5,6,7},{2,1,2,1,2},{3,3,3,3,3}};
          	int matMult[3][3];

    		for(int i=0; i<3;i++){
      			for(int j=0; j<3;i++){
        			a = mata[i][j];
				b = matb[j][i];
        			MPI_Send(a, 1, MPI_INT, 1, tag, MPI_COMM_WORLD);
        			MPI_Send(b, 1, MPI_INT, 1, tag, MPI_COMM_WORLD);
      		}
    	}
		for(int i=0;i<3;i++) { 
			for(int j=0;j<3;j++){
        			MPI_Recv(r1, 1, MPI_INT, 1, tag, MPI_COMM_WORLD, &status);
        			matMult[i][j]=r1;
      		}
    	}
		for(int i=0;i<3;i++) { 
			for(int j=0;j<3;j++)
				printf("%d\t",matc[i][j]);
				printf("\n");
		}
	}
	else {
    		for(int i=0;i<3;i++) { 
			for(int j=0;j<3;j++){

        			MPI_Recv(a, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
				MPI_Recv(b, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);

        			r1 = a*b;
				MPI_Send(r1, 1, MPI_INT, 0, tag, MPI_COMM_WORLD);
      			}
    		}
	}
  MPI_Finalize( );
}

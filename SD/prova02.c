#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "mpi.h"
int main(int argc, char** argv)
{
        int meu_rank, tag=0;
	int a[5], b[5], matc[5][5], i, j, r1[5], r2[5], r3[5], r4[5], r5[5];

        MPI_Status status;
        MPI_Init(&argc, &argv);
        MPI_Comm_rank(MPI_COMM_WORLD, &meu_rank);

	if (meu_rank == 0) {
                int mata[5][5]={{1,2,3,4,5},{1,0,1,8,7},{6,6,6,6,6},{1,4,7,8,7},{9,6,3,9,2}};
        	int matb[5][5]={{3,4,5,6,7},{2,1,2,1,2},{3,3,3,3,3},{8,9,6,2,3},{7,6,3,7,9}};

		for (i=0;i<5;i++) {
			a[i]=mata[0][i];
			b[i]=matb[0][i];
		}

		MPI_Send(a, 5, MPI_INT, 1, tag, MPI_COMM_WORLD);
		MPI_Send(b, 5, MPI_INT, 1, tag, MPI_COMM_WORLD);

		for (i=0;i<5;i++) {
                        a[i]=mata[1][i];
                        b[i]=matb[1][i];
                }

                MPI_Send(a, 5, MPI_INT, 2, tag, MPI_COMM_WORLD);
                MPI_Send(b, 5, MPI_INT, 2, tag, MPI_COMM_WORLD);

		for (i=0;i<5;i++) {
                        a[i]=mata[2][i];
                        b[i]=matb[2][i];
                }

                MPI_Send(a, 5, MPI_INT, 3, tag, MPI_COMM_WORLD);
                MPI_Send(b, 5, MPI_INT, 3, tag, MPI_COMM_WORLD);

		for (i=0;i<5;i++) {
			a[i]=mata[3][i];
			b[i]=matb[3][i];
		}

		MPI_Send(a, 5, MPI_INT, 4, tag, MPI_COMM_WORLD);
		MPI_Send(b, 5, MPI_INT, 4, tag, MPI_COMM_WORLD);

		for (i=0;i<5;i++) {
			a[i]=mata[4][i];
			b[i]=matb[4][i];
		}

		MPI_Send(a, 5, MPI_INT, 5, tag, MPI_COMM_WORLD);
		MPI_Send(b, 5, MPI_INT, 5, tag, MPI_COMM_WORLD);



		MPI_Recv(r1, 5, MPI_INT, 1, tag, MPI_COMM_WORLD, &status);
		MPI_Recv(r2, 5, MPI_INT, 2, tag, MPI_COMM_WORLD, &status);
		MPI_Recv(r3, 5, MPI_INT, 3, tag, MPI_COMM_WORLD, &status);
		MPI_Recv(r4, 5, MPI_INT, 4, tag, MPI_COMM_WORLD, &status);
		MPI_Recv(r5, 5, MPI_INT, 5, tag, MPI_COMM_WORLD, &status);
		

		for(i=0;i<5;i++)
			matc[0][i]=r1[i];

		for(i=0;i<5;i++)
                        matc[1][i]=r2[i];

		for(i=0;i<5;i++)
                        matc[2][i]=r3[i];

		for(i=0;i<5;i++)
			matc[3][i]=r4[i];
		
		for(i=0;i<5;i++)
			matc[4][i]=r5[i];



		for(i=0;i<5;i++) { 
			for(j=0;j<5;j++)
				printf("%d\t",matc[i][j]);
			printf("\n");
		}
	}

        else if(meu_rank == 1) {

		MPI_Recv(a, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
		MPI_Recv(b, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);

        	for (i=0;i<5;i++)
			r1[i] = a[i]+b[i];
		MPI_Send(r1, 5, MPI_INT, 0, tag, MPI_COMM_WORLD);
	}
        else if(meu_rank == 2) {
                MPI_Recv(a, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
                MPI_Recv(b, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);

                for (i=0;i<5;i++)
                        r2[i] = a[i]+b[i];
                MPI_Send(r2, 5, MPI_INT, 0, tag, MPI_COMM_WORLD);
        }	
	else if(meu_rank == 3) {
                MPI_Recv(a, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
                MPI_Recv(b, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);

                for (i=0;i<5;i++)
                        r3[i] = a[i]+b[i];
                MPI_Send(r3, 5, MPI_INT, 0, tag, MPI_COMM_WORLD);
	}
	else if(meu_rank == 4) {
                MPI_Recv(a, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
                MPI_Recv(b, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);

                for (i=0;i<5;i++)
                        r4[i] = a[i]+b[i];
                MPI_Send(r4, 5, MPI_INT, 0, tag, MPI_COMM_WORLD);
	}
	else {
		MPI_Recv(a, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
                MPI_Recv(b, 5, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);

                for (i=0;i<5;i++)
                        r5[i] = a[i]+b[i];
                MPI_Send(r5, 3, MPI_INT, 0, tag, MPI_COMM_WORLD);
	}
        MPI_Finalize( );
}

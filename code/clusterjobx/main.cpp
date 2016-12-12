#include <iostream>
#include <random>
#include <mpi.h>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    int nagents = 512;
    int N = pow(10,7);
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> randint(0, nagents);
    uniform_real_distribution<double> epsilon(0.0,1.0);
    double ** agent;
    int n = atoi(argv[1]);
    double a = atof(argv[2]);
    agent = new double*[n];
    for (int i = 0; i < n; i++) {
        agent[i] = new double[nagents];
        for (int j = 0; j < nagents; j++) {
            agent[i][j] = 1;
        }
    }
    MPI_Init (&argc, &argv);
    int rank, nthds;
    MPI_Comm_rank (MPI_COMM_WORLD, &rank);
    MPI_Comm_size (MPI_COMM_WORLD, &nthds);
    for (int j = 0; j < n; j++) {
        for (int i = 0; i<N; i++) {
            int u = randint(gen);
            int v = randint(gen);
            float e = epsilon(gen);
            if (u == v)
                continue;
            double upp = agent[j][u];
            double vpp = agent[j][v];
	    if ( (upp != vpp) && pow(fabs(upp-vpp),-a ) < epsilon(gen)  )
	      continue;
            agent[j][u] = e*(upp + vpp);
            agent[j][v] = (1-e)*(upp + vpp);
        }
    }

    if (rank == 0) {
        ofstream outfile;
        outfile.open("../../resources/data_" + to_string(a) + "_" + to_string(randint(gen)) + ".txt");
        for (int k = 1; k<nthds; k++) {
            MPI_Recv(&(agent[0][0]), nagents*n, MPI_DOUBLE, k, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            for (int j = 0; j<n; j++) {
                for (int i = 0; i<nagents; i++) {
                    outfile << agent[j][i] << ' ';
                }
                outfile << endl;
            }
        }
    }
    else if (rank > 0) {
        MPI_Send(&(agent[0][0]), nagents*n, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD);
    }

    MPI_Finalize();
    return 0;
}

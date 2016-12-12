#include <iostream>
#include <random>
#include <mpi.h>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    int nagents = 1024;
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
            double upp = agent[j][u];
            double vpp = agent[j][v];
            
            if (vpp == upp){
              p = 1.;
            }
            else{
              p = 2*pow(fabs(upp - vpp ),-a);
            }
            if (e < p && (u != v)){
              agent[j][u] = e*(upp + vpp);
              agent[j][v] = (1-e)*(upp + vpp);
            }
        }
    }

    if (rank == 0) {
        ofstream outfile;
        outfile.open("../resources/data_" + to_string(a) + "_" + to_string(randint(gen)) + ".txt");
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




/*

for (int i = 0; i < MCSteps; i++){
  players.fill(m0);
  for (int j = 0; j < transactions; j++){
    int index_i = distribution(gen);
    int index_j = distribution(gen);
    
    double epsFac = eps(gen);
    
    
    if (players(index_i) - players(index_j) == 0){
      p = 1.;
    }
    else{
      p = 2*pow(fabs((players(index_i) - players(index_j))/double(m0)),-alpha)*(pow((c(index_i,index_j)+1)/(maxTransactions+1),gamma));
    }
    
    if (eps(gen) < p && (index_i != index_j)){
      double m1 = lambda*players(index_i) + (1-lambda)*epsFac*    (players(index_i) + players(index_j));
      double m2 = lambda*players(index_j) + (1-lambda)*(1-epsFac)*(players(index_i) + players(index_j));
      
      //cout << "hei" << endl;
      
      players(index_i) = m1;
      players(index_j) = m2;
      
      c(index_j,index_i) += 1;
      c(index_i,index_j) += 1;
      
      if (c(index_j,index_i) > maxTransactions){
        maxTransactions = c(index_j,index_i);
      }
      else if (c(index_i,index_j) > maxTransactions){
        maxTransactions = c(index_i,index_j);
      }
    }
    if (MCSteps == 1){
      if (j%writingFreq == 0){
        double mean = 0;
        for (int i = 0; i < N; i++){
          mean += players(i)/m0;
        }
        mean /= (N); 
        outFile << (j+1) << " " << findVariance(players,j+1,N,m0) << " " << mean << "\n";
      }
    }
  }
}
*/
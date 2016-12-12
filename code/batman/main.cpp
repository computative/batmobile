#include <iostream>
#include <random>
#include <mpi.h>
#include <fstream>
#include <string>

using namespace std;

void P(double **agent, int u, int v, int j, double e);

int main(int argc, char *argv[])
{
    int nagents = 1024;
    int N = pow(10,5);
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> randint(0, nagents-1);
    uniform_real_distribution<double> epsilon(0.0,1.0);
    int n = 1000;
    double a = 2;
    double l = 0.5;
    double ** agent;
    agent = new double*[n];
    for (int i = 0; i < n; i++) {
        agent[i] = new double[nagents];
        for (int j = 0; j < nagents; j++) {
            agent[i][j] = 1;
        }
    }
    for (int j = 0; j < n; j++) {
        for (int i = 0; i<N; i++) {
            int u = randint(gen);
            int v = randint(gen);
            double e = epsilon(gen);
            if (u == v)
                continue;
            double upp = agent[j][u];
            double vpp = agent[j][v];
            if ( (upp != vpp) && pow(fabs(upp-vpp),-a ) < epsilon(gen)  )
                continue;
            agent[j][u] = l*upp + e*(1-l)*(upp + vpp);
            agent[j][v] = l*vpp + (1-e)*(1-l)*(upp + vpp);
        }
    }
    ofstream outfile;
    string filename = "/home/marius/Dokumenter/fys4150/batmobile/resources/datal" + to_string(l) + "a" + to_string(a) + "n"+ to_string(nagents) +".txt";
    outfile.open(filename);
    for (int j = 0; j<n; j++) {
        for (int i = 0; i<nagents; i++) {
            outfile << agent[j][i] << ' ';
        }
        outfile << endl;
    }
    return 0;
}

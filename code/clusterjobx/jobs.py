from numpy import *
import os

for a in [0.5, 1, 1.5, 2]:
    outfile = open("job%f.sh" % a, 'w')
    outfile.write("#!/bin/bash\n")
    outfile.write("#SBATCH --partition=normal \n")
    outfile.write("#SBATCH --nodes=12 \n")
    outfile.write("#SBATCH --ntasks-per-node=8 \n")
    outfile.write("#SBATCH --time=12:00:00 \n")
    outfile.write("#SBATCH --job-name=batmobile \n")
    outfile.write("mpirun ./batman 100 %f \n" % a)
    outfile.close()
    print "sbatch job%f.sh" % a
    os.popen("sbatch job%f.sh" % a)

from numpy import *
import os

outfile = open("job.sh", 'w')
outfile.write("#!/bin/bash\n")
outfile.write("#SBATCH --partition=normal \n")
outfile.write("#SBATCH --nodes=18 \n")
outfile.write("#SBATCH --ntasks-per-node=8 \n")
outfile.write("#SBATCH --time=1:00:00 \n")
outfile.write("#SBATCH --job-name=batmobile \n")

outfile.write("mpirun ./batman 72 \n")
outfile.close()
print "sbatch job.sh"
os.popen("sbatch job.sh")

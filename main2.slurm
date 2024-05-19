#!/bin/bash
#SBATCH -A GOV113006 -p betatest
#SBATCH -J main -t 24:00:00                                    
#SBATCH --nodes=30 --ntasks-per-node=1 --cpus-per-task=112
#SBATCH --mem-bind=no
#SBATCH -o /home/u9071297/job_results/%j.out         
#SBATCH -e /home/u9071297/job_results/%j.err          

##export OMP_PROC_BIND=true
##export OMP_PLACES=cores
##export OMP_DYNAMIC=false

VARS="SLURM_JOB_ID SLURM_NTASKS SLURM_NNODES SLURM_NTASKS_PER_NODE SLURM_CPUS_PER_TASK SLURM_TASK_PID SLURM_NODELIST SLURM_SUBMIT_DIR SLURM_MEM_BIND SLURM_MPI_TYPE OMP_PROC_BIND OMP_PLACES OMP_DYNAMIC"
for v in ${VARS}; do echo " $v = ${!v}"; done

ml purge

module use /home/qusim/modulefiles
module use /home/qusim/openmpi/modulefiles
module use /home/qusim/intel-qs/modulefiles
module use /home/qusim/modulefiles-example-openmpi-intelqs/
module load intel-qs/oneAPI23/20240201

ml python

source /pkg/x86/apps/intel_oneapi/2024/setvars.sh

#export I_MPI_DEBUG=30
#export FI_LOG_LEVEL=debug

echo "Number of nodes: 30"

mpiexec python3 /home/u9071297/VQC/vqc_p.py

echo "---- Walltime: ${SECONDS} sec."

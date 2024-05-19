# nchc-hpc_qc-bechmark
## Hardware
![alt text](figure/orm67ua2.png)
```
cat /proc/cpuinfo
srun lsblk
```

## Software
- OS：RHEL8.7
- Toolchain
  1. GCC 8.5.0(default)
  2. Intel oneAPI
  3. NVHPC

## Quantum Computing Tools
1. **qiskit**
2. Intel-QS
3. XACC

## Buildup Qiskit Env
- install miniconda and create env for qiskit
```
# install miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
# set path /opt/nfsdir/miniconda3
conda config --set auto_activate_base false
# create env
conda create --name qiskit python=3.11
# env activate
conda activate qiskit_aer
```
- add PATH
```
sudo nano ~/.bashrc
module use /home/qusim/modulefiles
export MPIROOT=/home/qusim/gcc8/openmpi-4.1.6
export PATH=$MPIROOT/bin:$PATH
export LD_LIBRARY_PATH=$MPIROOT/lib:$LD_LIBRARY_PATH
export MANPATH=$MPIROOT/share/man:$MANPATH
export LD_LIBRARY_PATH=/home/qusim/gcc8/OpenBLAS-0.3.26/lib:$LD_LIBRARY_PATH
export BLAS=/home/qusim/gcc8/OpenBLAS-0.3.26/lib/libopenblas.so
export ATLAS=/home/qusim/gcc8/OpenBLAS-0.3.26/lib/libopenblas.so
source ~/.bashrc
```
```
mpiexec --version
which mpicc mpiexec mpirun
ompi_info
```
- install qiskit-aer from source
```
git clone https://github.com/Qiskit/qiskit-aer
cd qiskit-aer
pip install -r requirements-dev.txt
pip install pybind11 auditwheel
python ./setup.py bdist_wheel -- -DAER_MPI=True -DAER_DISABLE_GDR=True
pip install -U dist/qiskit_aer*.whl
```
- install qiskit
```
pip install qiskit==0.45.3
pip install qiskit-aer==0.13.2
pip install qiskit-machine-learning==0.7.1
pip install qiskit-experiments==0.5.4
```
- others
```
pip install -U memory_profiler
```

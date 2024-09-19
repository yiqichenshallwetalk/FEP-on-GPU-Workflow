FEP-on-GPU-Workflow: A GPU-resident GROMACS FEP Workflow Suite
(Currently only supports CUDA and MACA platforms)

# 1. Install workflow management tool: MetaMol
We recommend installing MetaMol via conda(>=3.23)
```bash
cd metamol
conda env create -f environment.yml
conda activate metamol
pip3 install .
``` 

To test the installation of MetaMol, run the following:
```bash
cd ${metamol_source_dir}/metamol; pytest -vv;
```

# 2. Install the FEP-on-GPU GROMACS Simulation Engine
```bash
conda activate metamol
cd gromacs-fep-gpu/
mkdir -p build
cd build && cmake -DGMX_GPU=CUDA -DGMX_DOUBLE=off -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX -DGMX_MPI=off ../
cmake --build . -j 16
make install
``` 

Build & run unit tests

```bash
make tests -j 16 && make test -j 16
``` 

# 3. End-to-End FEP Workflow Examples
Four benchmark systems are provided as examples. All input files and scripts are included inside the `examples` folder. The following tutorial uses 4MR3 ligand solvent system as an example. Note that the metamol environment should be active.
```bash
conda activate metamol
cd examples/4MR3/ligand/
python3 fep_ligand.py
``` 
When finished successfully, the output data will be saved to the `data` folder.


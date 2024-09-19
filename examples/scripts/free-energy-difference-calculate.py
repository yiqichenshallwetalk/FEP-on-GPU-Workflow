import numpy as np
import os
import matplotlib.pyplot as plt

from metamol.workflows.fep_analysis import compute_free_energy_differences, readXvgData, uncorrelate
# filepath: The directory of xvg folder
filepath = 'data/out_xvg/PROD/xvg_files'
# temperature: The temperature this FEP simulations are at
temperature = 298.15
# equiltime: equilibration time, in ps, is the discarded time due to equilibration
equiltime = 1000.0
# n_bootstraps: the number of resamplings for bootstrapping
n_bootstraps = 1000

# Use the compute_free_energy_differences function in MetaMol to read xvg files and compute delta G
fe_diff = compute_free_energy_differences(filepath=filepath, equiltime=equiltime, temperature=temperature, n_bootstraps=n_bootstraps)
# The default backend is pymbar. To run mbar computations on GPU, please first install the fastmbar package: pip3 install fastmbar, then run the following
# fe_diff = compute_free_energy_differences(filepath=filepath, equiltime=equiltime, temperature=temperature, n_bootstraps=n_bootstraps, backend='fastmbar', gpu=True)

# num of states: 31 for ligand and 42 for complex systems
num_states = 31
dhdl_all = [fe_diff['Delta_f'][i, i+1] for i in range(num_states-1)]
dhdl_std_all = [fe_diff['dDelta_f'][i, i+1] for i in range(num_states-1)]
# convert from KT to kcal/mol
dhdl_all = np.array(dhdl_all) * 0.593
dhdl_std_all = np.array(dhdl_std_all) * 0.593

# Bar plot of delta G values between intermediate states
plt.figure()
plt.bar(range(num_states-1), dhdl_all, yerr=dhdl_std_all)
plt.xlabel('State', fontsize=15)
plt.ylabel(r'$\Delta G (kcal/mol)$', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# Outpur the free nenergy difference between end states
print("The free energy diffrence between end states is {0} +- {1} kcal/mol", fe_diff['Delta_f'][0, num_states-1], fe_diff['dDelta_f'][0, num_states-1])


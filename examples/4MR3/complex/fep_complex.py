import os
from metamol.workflows.gromacs_fep import FEP_workflow
from metamol.workflows.utils import download_local
from dflow import config
# Debug mode , indepedent of k8s
config["mode"] = "debug"

wf_complex, step_list = FEP_workflow(config_file="input_complex.json")
wf_complex.submit()

print(wf_complex.query_status())

local_dir = "data"
download_local(wf_complex, step_list[-1], local_path=local_dir)

# Arrange xvg files into one folder
num_states = 42
prefix_dir = 'data/out_xvg/PROD/'
dst = os.path.join(prefix_dir, 'xvg_files')
os.makedirs(dst, exist_ok=True)
for i in range(num_states):
    src = os.path.join(prefix_dir, 'No_'+str(i), 'prod_No'+str(i)+'.xvg')
    dst = os.path.join(prefix_dir, 'xvg_files')
    cmd = f'cp "{src}" "{dst}"'
    os.system(cmd)


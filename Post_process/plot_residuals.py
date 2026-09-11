import csv
import numpy as np
from matplotlib import pyplot as plt
import os


cwd = os.path.dirname(os.path.abspath(__file__))
init_data_file = ""
data_file = os.path.join(cwd, "..", "MRF_quad_rotor_with_body", "log.simpleFoam")

Ux_res = np.array([])
Uy_res = np.array([])
Uz_res = np.array([])
p_res = np.array([])
cont_res = np.array([])
nu_tilda_res = np.array([])

if len(init_data_file) > 0:
    with open(init_data_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            strRow = str(row)
            if "Solving for Ux" in strRow:
                residual = row[2]  # only get final residual
                split_idx = row[2].index("=")
                res_number = float(row[2][split_idx + 2:])
                Ux_res = np.append(Ux_res, res_number)
            if "Solving for Uy" in strRow:
                residual = row[2]  # only get final residual
                split_idx = row[2].index("=")
                res_number = float(row[2][split_idx + 2:])
                Uy_res = np.append(Uy_res, res_number)
            if "Solving for Uz" in strRow:
                residual = row[2]  # only get final residual
                split_idx = row[2].index("=")
                res_number = float(row[2][split_idx + 2:])
                Uz_res = np.append(Uz_res, res_number)
            if "Solving for p" in strRow:
                residual = row[2]  # only get final residual
                split_idx = row[2].index("=")
                res_number = float(row[2][split_idx + 2:])
                p_res = np.append(p_res, res_number)

with open(data_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        strRow = str(row)
        if "Solving for Ux" in strRow:
            residual = row[2]  # only get final residual
            split_idx = row[2].index("=")
            res_number = float(row[2][split_idx + 2:])
            Ux_res = np.append(Ux_res, res_number)
        if "Solving for Uy" in strRow:
            residual = row[2]  # only get final residual
            split_idx = row[2].index("=")
            res_number = float(row[2][split_idx + 2:])
            Uy_res = np.append(Uy_res, res_number)
        if "Solving for Uz" in strRow:
            residual = row[2]  # only get final residual
            split_idx = row[2].index("=")
            res_number = float(row[2][split_idx + 2:])
            Uz_res = np.append(Uz_res, res_number)
        if "Solving for p" in strRow:
            residual = row[2]  # only get final residual
            split_idx = row[2].index("=")
            res_number = float(row[2][split_idx + 2:])
            p_res = np.append(p_res, res_number)
        if "Solving for nuTilda" in strRow:
            residual = row[2]  # only get final residual
            split_idx = row[2].index("=")
            res_number = float(row[2][split_idx + 2:])
            nu_tilda_res = np.append(nu_tilda_res, res_number)

num_epoch_all = Ux_res.shape[0]
epoch_all = np.arange(num_epoch_all) + 1
num_epoch_turb = nu_tilda_res.shape[0]
epoch_turb = np.arange(num_epoch_turb) + (num_epoch_all - num_epoch_turb) + 1

plt.semilogy(epoch_all, Ux_res, label="Ux")
plt.semilogy(epoch_all, Uy_res, label="Uy")
plt.semilogy(epoch_all, Uz_res, label="Uz")
plt.semilogy(epoch_all, p_res, label="p")
plt.semilogy(epoch_turb, nu_tilda_res, label="nuTilda")
plt.legend()
plt.xlabel("Iteration step")
plt.ylabel("Residual")
plt.grid()
plt.show()

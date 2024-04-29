import csv
from matplotlib import pyplot as plt

data_file = "log.simpleFoam"

Ux_res = []
Uy_res = []
Uz_res = []
p_res = []
cont_res = []

with open(data_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        strRow = str(row)
        if "Solving for Ux" in strRow:
            residual = row[2]  # only get final residual
            split_idx = row[2].index("=")
            res_number = float(row[2][split_idx+2:])
            Ux_res.append(res_number)
        if "Solving for Uy" in strRow:
            residual = row[2]  # only get final residual
            split_idx = row[2].index("=")
            res_number = float(row[2][split_idx + 2:])
            Uy_res.append(res_number)
        if "Solving for Uz" in strRow:
            residual = row[2]  # only get final residual
            split_idx = row[2].index("=")
            res_number = float(row[2][split_idx + 2:])
            Uz_res.append(res_number)
        if "Solving for p" in strRow:
            residual = row[2]  # only get final residual
            split_idx = row[2].index("=")
            res_number = float(row[2][split_idx + 2:])
            p_res.append(res_number)


plt.semilogy(Ux_res, label="Ux")
plt.semilogy(Uy_res, label="Uy")
plt.semilogy(Uz_res, label="Uz")
plt.semilogy(p_res, label="p")
plt.legend()
plt.xlabel("Iteration step")
plt.ylabel("Residual")
plt.grid()
plt.show()

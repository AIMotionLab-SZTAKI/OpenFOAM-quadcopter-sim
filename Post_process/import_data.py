import csv
import numpy as np
import pandas as pd
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

data_name = "raw_cw"
output_name = "single_rotor_cw"

df = pd.read_csv("raw_data/" + data_name + ".csv", header=0)

df = df.drop(columns=['nuTilda', 'nut'])
df = df.rename(columns={"Points:0": "x", "Points:1": "y", "Points:2": "z",
                        "U:0": "vx", "U:1": "vy", "U:2": "vz"})

# correcting the pressure with the density
df["vz"] += 5  # correct with the inflow velocity
df["v"] = np.sqrt(df["vx"]**2 + df["vy"]**2 + df["vz"]**2)
df["p"] *= 1.293
df["p"] += 0.5*1.293*df["v"]**2
del df["v"]

# drop outside domains
#idxDrop = df[(np.abs(df.x) > 0.35) | (np.abs(df.y) > 0.35)].index
#df = df.drop(idxDrop)

# interpolation
xi = np.linspace(-0.4, 0.4, 81)
yi = xi
zi = np.linspace(-0.8, 0, 81)

X, Y, Z = np.meshgrid(xi, yi, zi)
X = X.reshape(81*81*81, 1)
Y = Y.reshape(81*81*81, 1)
Z = Z.reshape(81*81*81, 1)

dfi = pd.DataFrame()
dfi["x"] = np.squeeze(X, axis=1)
dfi["y"] = np.squeeze(Y, axis=1)
dfi["z"] = np.squeeze(Z, axis=1)

dfi["p"] = griddata((df["x"], df["y"], df["z"]), df["p"], (dfi["x"], dfi["y"], dfi["z"]), method='nearest')
dfi["vx"] = griddata((df["x"], df["y"], df["z"]), df["vx"], (dfi["x"], dfi["y"], dfi["z"]), method='nearest')
dfi["vy"] = griddata((df["x"], df["y"], df["z"]), df["vy"], (dfi["x"], dfi["y"], dfi["z"]), method='nearest')
dfi["vz"] = griddata((df["x"], df["y"], df["z"]), df["vz"], (dfi["x"], dfi["y"], dfi["z"]), method='nearest')

dfi = dfi.sort_values(by=['x', 'y', 'z'])
dfi = dfi.round(decimals=3)

df_pressure = dfi.copy()
df_vel = dfi.copy()
del df_pressure["vx"], df_pressure["vy"], df_pressure["vz"]
del df_vel["p"]
df_pressure.to_csv("processed_data/" + output_name + "_pressure.csv", index=False)
df_vel.to_csv("processed_data/" + output_name + "_velocity.csv", index=False)


# create z heatmap
z_level = -0.5
df_zmesh = dfi
idxDrop = df_zmesh[df_zmesh.z != z_level].index
df_zmesh = df_zmesh.drop(idxDrop)

x = df_zmesh["x"].to_numpy()
y = df_zmesh["y"].to_numpy()
p = df_zmesh["p"].to_numpy()

# create x-y points to be used in heatmap
xi = np.linspace(x.min(), x.max(), 81)
yi = np.linspace(y.min(), y.max(), 81)

# Interpolate for plotting
zi = griddata((x, y), p, (xi[None, :], yi[:, None]), method='linear')

# Create the contour plot
plt.figure()
plt.contourf(xi, yi, zi, 50, cmap='jet')
plt.colorbar()
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title(f"Pressure contour at z={z_level} m")
plt.show(block=False)


# create x heatmap
x_level = -0.1
df_xmesh = dfi
idxDrop = df_xmesh[df_xmesh.x != x_level].index
df_xmesh = df_xmesh.drop(idxDrop)

y = df_xmesh["y"].to_numpy()
z = df_xmesh["z"].to_numpy()
p = df_xmesh["p"].to_numpy()

# create x-y points to be used in heatmap
yi = np.linspace(y.min(), y.max(), 81)
zi = np.linspace(z.min(), z.max(), 81)

# Interpolate for plotting
pi = griddata((y, z), p, (yi[None, :], zi[:, None]), method='linear')

# Create the contour plot
plt.figure()
plt.contourf(yi, zi, pi, 50, cmap='jet')
plt.colorbar()
plt.xlabel("y [m]")
plt.ylabel("z [m]")
plt.title(f"Pressure contour at x={x_level} m")
plt.show()


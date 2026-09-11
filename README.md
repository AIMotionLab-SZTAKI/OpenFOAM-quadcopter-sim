# OpenFOAM Quadcopter Simulation
 
OpenFOAM case files for the CFD simulation of quadcopter aerodynamics. The rotating propellers are modelled with the *multiple reference frame* (MRF) approach, and the steady-state flow is solved with `simpleFoam`, and turbulence is modelled with the Spalart–Allmaras model.
 
> A preliminary version of the simulation (modeling only a single rotor) is available on the [`single-rotor`](https://github.com/AIMotionLab-SZTAKI/OpenFOAM-quadcopter-sim/tree/single-rotor) branch.

## Repository structure
 
```
.
├── 0/                       # Initial and boundary conditions (U, p, nut, nuTilda)
├── 0.orig/                  # Original copy of the initial and boundary conditions
├── constant/
│   ├── MRFProperties        # MRF zones and propeller angular velocities
│   ├── momentumTransport    # Turbulence model settings
│   ├── transportProperties  # Fluid properties
│   └── g                    # Gravitational field setting
├── system/                  # Solver, discretization and decomposition settings
├── mesh/                    # Meshing case
│   ├── constant/triSurface/ # Geometry: propellers (blade_M1–M4) and domain boundaries (inlet, outlet, side)
│   ├── system/              # blockMesh, snappyHexMesh, surfaceFeatures and decomposition settings
│   ├── runMesh.sh           # Mesh generation script
│   └── open.foam            # ParaView file for inspecting the mesh
├── utils/                   # Dictionaries for the initialization and final stages of the run
├── copyMesh.sh              # Copies the mesh into the simulation case and pre-processes it
├── runSim.sh                # Runs a single simulation
├── run_multiple_sim.sh      # Runs simulations for multiple propeller speeds
└── open.foam                # ParaView file for inspecting the results
```

## Requirements
 
- [OpenFOAM 10](https://openfoam.org/download/10-ubuntu/) (openfoam.org release). The case has not been tested with other versions, and the ESI releases (openfoam.com, e.g., `v2312`) use partly different dictionary syntax.
- [ParaView](https://www.paraview.org/) for visualization.
- A multi-core machine. The default configuration runs on 22 parallel processes (see [Parallel settings](#parallel-settings)).

## Installation
 
Clone the repository:
 
```bash
git clone https://github.com/AIMotionLab-SZTAKI/OpenFOAM-quadcopter-sim.git
cd OpenFOAM-quadcopter-sim
```
 
Install OpenFOAM 10 by following the [official instructions](https://openfoam.org/download/10-ubuntu/), then make sure its environment is loaded in the terminal:
 
```bash
source /opt/openfoam10/etc/bashrc
echo $WM_PROJECT_VERSION   # should print 10
```

## Usage
 
Start from the simulation root folder:
```bash
cd OpenFOAM-quadcopter-sim/MRF_quad_rotor
```
 
### 1. Generate the mesh
 
Create the finite volume discretization of the computational domain:
 
```bash
cd mesh
source runMesh.sh
```

### 2. Copy the mesh to the simulation case
 
Once meshing has finished, copy the mesh to the simulation case. This step also performs some minor pre-processing:
 
```bash
cd ..
source copyMesh.sh
```

### 3. Run the simulation
 
Set the propeller angular velocity in `constant/MRFProperties` (the `omega` entry of each MRF zone). Then start the simulation in the background and follow its progress in the log file:
 
```bash
source runSim.sh > log.simpleFoam &
tail -f log.simpleFoam
```
 
Pressing `Ctrl+C` stops `tail`; the simulation keeps running in the background.
 
The simulation runs in two stages: an initialization run with the turbulence model disabled, followed by the final run with turbulence enabled. The `controlDict` and `momentumTransport` dictionaries for both stages are stored in `utils/`.
 
To run simulations for multiple propeller angular velocities, use:
 
```bash
source run_multiple_sim.sh
```

### Parallel settings
 
Both the meshing and the simulation run on 22 parallel processes by default. To change this, update:
 
- `numberOfSubdomains`, `simpleCoeffs`, and `hierarchicalCoeffs` in `mesh/system/decomposeParDict` and `system/decomposeParDict`,
- the number of processes in the shell scripts (`mesh/runMesh.sh`, `runSim.sh`, `run_multiple_sim.sh`), e.g. the `-np` argument of `mpirun`.
The two values must match.

## Visualization and post-processing
 
Results can be visualized and post-processed in [ParaView](https://www.paraview.org/) by opening the `open.foam` file in the repository root (or `mesh/open.foam` to inspect the mesh):
 
```bash
paraview open.foam
```
 
Alternatively, run OpenFOAM's `paraFoam` wrapper from the case directory.
 

## Simulation user guide

### Creating the numerical mesh
Before running the CFD simulations, the finite volume discretization of the computational domain is required. To do that, first go the the `mesh/` dictionary and run the following command:
```bash
cd OpenFOAM-quadcopter-sim/MRF_quad_rotor/mesh/
source runMesh.sh
```

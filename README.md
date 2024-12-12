# OpenFOAM-quadcopter-sim
This repository contains the OpenFOAM files for numerical simulation of quadcopter aerodynamics (CFD).

## Installation
To get the project files, clone the repository as
```
$ git clone https://github.com/AIMotionLab-SZTAKI/OpenFOAM-quadcopter-sim
```

### OpenFOAM
OpenFOAM v10 is required for the CFD simulation, which can be installed by following the instructions here: <https://openfoam.org/download/10-ubuntu/>.

### Python scripts
To be able to run the Python scripts, first open the folder containing the post-processing codes
```
$ cd OpenFOAM-quadcopter-sim/Post_process/
```

It is recommended to use a virtual environment. On Linux/Bash run
```
$ python3 -m venv venv
$ source venv/bin/activate
```

On Windows, run
```
$ python -m venv venv
$ ./venv/Scripts/activate
```

Then, install the required packages as
```
$ pip install -r requirements.txt
```

## Simulation user guide
The mesh has to be made first, to run the CFD simulations. Download the `.stl` files from [here](https://nextcloud.sztaki.hu/apps/files/files/1578197?dir=/AIMotionLab/Projects/CFD/OpenFOAM%20stl%20files), and copy them into `OpenFOAM-quadcopter-sim/MRF_single_rotor/mesh/constant/triSurface/` folder. Finally, the meshing process can be started with
```
$ cd OpenFOAM-quadcopter-sim/MRF_single_rotor/mesh/
$ source runMesh.sh
```
After the meshing process has finished, the mesh has to be copied to the main simulation folder, and some minor modifications also have to be applied with
```
$ cd ..
$ source copyMesh.sh
```
Finally, the simulation is ready to run. It is advised to log the output into a separate file, then if necessary the log file can be viewed during the simulation:
```
$ source runSim.sh > log.simpleFoam &
$ tail -f log.simpleFoam
```

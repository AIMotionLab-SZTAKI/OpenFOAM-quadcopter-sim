# OpenFOAM-quadcopter-sim
This repository contains the OpenFOAM files for numerical simulation of quadcopter aerodynamics (CFD).

## Installation
To get the project files, clone the repository as
```
$ git clone https://github.com/AIMotionLab-SZTAKI/OpenFOAM-quadcopter-sim
```

### OpenFOAM
For the CFD simulation, OpenFOAM v10 is required, which can be installed by following the instructions here: <https://openfoam.org/download/10-ubuntu/>.

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

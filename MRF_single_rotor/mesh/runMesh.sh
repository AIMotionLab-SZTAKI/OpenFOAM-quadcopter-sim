#!/bin/bash

blockMesh

surfaceFeatures

decomposePar

mpirun -np 30 snappyHexMesh -parallel -overwrite

reconstructParMesh -constant

rm -r processor*
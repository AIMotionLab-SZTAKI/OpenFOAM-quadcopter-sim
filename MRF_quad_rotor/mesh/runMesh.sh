#!/bin/bash

blockMesh

surfaceFeatures

decomposePar

mpirun --use-hwthread-cpus -np 22 snappyHexMesh -parallel -overwrite

reconstructParMesh -constant

rm -r processor*

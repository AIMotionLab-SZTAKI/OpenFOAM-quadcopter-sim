#!/bin/sh
cd ${0%/*} || exit 1    # Run from this directory

# Mesh stator part
cd mesh_stator/
fluentMeshToFoam MRF_stator.msh

# Mesh rotor part
cd ../mesh_rotor/
fluentMeshToFoam MRF_rotor.msh

mkdir constant/polyMesh/sets
topoSet

# Merge meshes
cd ../
mergeMeshes -overwrite mesh_stator mesh_rotor
cp -r mesh_stator/constant/polyMesh/ constant/

checkMesh

createPatch -overwrite

topoSet

decomposePar

mpirun -np 4 simpleFoam -parallel | tee log.simple
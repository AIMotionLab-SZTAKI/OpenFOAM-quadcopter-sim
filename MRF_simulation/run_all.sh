#!/bin/sh
cd ${0%/*} || exit 1    # Run from this directory

# Mesh stator part
cd mesh_stator/
fluentMeshToFoam MRF_stator.msh

# Mesh rotor part
cd ../mesh_rotor/
fluentMeshToFoam MRF_rotor.msh

# Merge meshes
cd ../
mergeMeshes -overwrite mesh_stator mesh_rotor

# copy mesh_stator/constant/polyMesh to /constant/polyMesh
checkMesh

createPatch -overwrite
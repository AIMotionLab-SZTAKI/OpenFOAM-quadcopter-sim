#!/bin/sh
cd "$(dirname "$0")" || exit 1  # Run from this directory
# define paths
DIR=$(pwd)  # current directory
STATOR_MESH="$DIR/mesh_stator/MRF_stator.msh"
ROTOR_MESH="$DIR/mesh_rotor/MRF_rotor.msh"
#
# Mesh stator part
cd "$DIR/mesh_stator" || exit 1
fluentMeshToFoam -case "$DIR/mesh_stator" "$STATOR_MESH"
#
# Mesh rotor part
cd "$DIR/mesh_rotor" || exit 1
fluentMeshToFoam -case "$DIR/mesh_rotor" "$ROTOR_MESH"
#
mkdir "$DIR/mesh_rotor/constant/polyMesh/sets"
topoSet
#
# Merge meshes
cd $DIR || exit 1
#mergeMeshes -overwrite mesh_stator mesh_rotor
#
#rm -r $(DIR)/constant/polyMesh/
#cp -r $(DIR)/mesh_stator/constant/polyMesh/ constant/
#
#checkMesh
#
#createPatch -overwrite
#
#topoSet
#
#decomposePar
#
#mpirun -np 4 simpleFoam -parallel | tee log.simple
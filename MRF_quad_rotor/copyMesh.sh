#!/bin/bash

rm -rf constant/polyMesh

cp -r mesh/constant/polyMesh constant/

createPatch -overwrite

#!/bin/bash

cp utils/momentumTransport_init constant/momentumTransport
cp utils/controlDict_init system/controlDict

decomposePar

mpirun -np 30 simpleFoam -parallel

cp utils/momentumTransport_final constant/momentumTransport
cp utils/controlDict_final system/controlDict

mpirun -np 30 simpleFoam -parallel

reconstructPar
rm -r processor*

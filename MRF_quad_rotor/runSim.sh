#!/bin/bash

cp utils/momentumTransport_init constant/momentumTransport
cp utils/controlDict_init system/controlDict

decomposePar

mpirun --use-hwthread-cpus -np 22 simpleFoam -parallel

cp utils/momentumTransport_final constant/momentumTransport
cp utils/controlDict_final system/controlDict

mpirun --use-hwthread-cpus -np 22 simpleFoam -parallel

reconstructPar
#rm -r processor*

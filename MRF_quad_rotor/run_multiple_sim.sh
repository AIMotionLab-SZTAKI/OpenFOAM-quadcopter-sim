#!/bin/bash
#set -e

OMEGAS="1150 1200 1300 1400 1500 1600 1700 1800"
for omega in $OMEGAS; do
  echo "=== omega = $omega rad/s ==="
  rm -rf processor* 0 results_$omega
  cp -r 0.orig 0

  cp utils/momentumTransport_init constant/momentumTransport
  cp utils/controlDict_init system/controlDict

  # set the rotation speed (rad/s), adjust the entry path to your MRF zone name
  cp utils/MRFProperties.orig constant/MRFProperties
  foamDictionary constant/MRFProperties -entry MRF1/omega -set "$omega"
  foamDictionary constant/MRFProperties -entry MRF2/omega -set "-$omega"
  foamDictionary constant/MRFProperties -entry MRF3/omega -set "$omega"
  foamDictionary constant/MRFProperties -entry MRF4/omega -set "-$omega"

  decomposePar -force > log.decomposePar_$omega 2>&1
  mpirun --use-hwthread-cpus -np 22 simpleFoam -parallel > log.simple1_$omega 2>&1

  cp utils/momentumTransport_final constant/momentumTransport
  cp utils/controlDict_final system/controlDict
  mpirun --use-hwthread-cpus -np 22 simpleFoam -parallel > log.simple2_$omega 2>&1

  reconstructPar > log.reconstructPar_$omega 2>&1
  rm -rf processor*

  mkdir results_$omega
  for d in $(foamListTimes); do mv "$d" results_$omega/; done
  mv log.*_$omega results_$omega/
done

#!/bin/bash
# BASH
# 
#Sets up the higher accuracy relaxation INCAR files for the TMDC T or Hc structures.
#
#Matt Evans
#University of Exeter
#me367@exeter.ac.uk
#19/06/20
#v1.1 
# 
###################################################################################################

#Run from your own DStruc_T or DStruc_Hc directory

Phase=$(echo $PWD | sed 's/\/home\/links\/me367\/DWork\/DTMDC\/DMX2\/DStruc_//')
echo $Phase

if [ "$Phase" == "Hc" ]
then
    Metal="Co Cr Cu Fe Hf Ir Mn Mo Ni Os Pb Pd Pt Re Rh Ru Sc Sn Ti V W Y Zr"
    Chalc="S Se Te"
elif [ "$Phase" == "T" ]
then
    Metal="Co Cr Cu Fe Ge Hf Ir Mn Mo Nb Ni Os Pb Pd Pt Re Rh Ru Sc Sn Ta Ti V W Y Zr"
    Chalc="Se Te"
fi

for i in $Metal
do
    for j in $Chalc
    do
	cp -r /scratch/DMX2/DStruc_$Phase/D$i/D$j/DBulk1x1/DRelax ~/DWork/DTMDC/DMX2/DStruc_$Phase/D$i/D$j/DBulk1x1
	mkdir -p D$i/D$j/DBulk1x1/DPhonon 
	# mkdir -p ~/DWork/DTMDC/DMX2/DStruc_$Phase/D$i/D$j/DBulk1x1/DPhonon/ #To run from anywhere in your home (~) directory
	if [ "$Phase" == "Hc" ]
	then
	    cp D$i/D$j/DBulk1x1/DRelax/{CHGCAR,POSCAR,KPOINTS,POTCAR} D$i/D$j/DBulk1x1/DPhonon/
	elif [ "$Phase" == "T" ]
	then
	    cp D$i/D$j/DBulk1x1/DRelax/{CHGCAR,CONTCAR,KPOINTS,POTCAR} D$i/D$j/DBulk1x1/DPhonon/ #for Hc alter CONTCAR to POSCAR
	    mv D$i/D$j/DBulk1x1/DPhonon/CONTCAR D$i/D$j/DBulk1x1/DPhonon/POSCAR #for Hc comment out this line
	fi
	sed 's\ EDIFF = 1d-7\ EDIFF = 1d-8\; s\ EDIFFG = -0.01\ EDIFFG = -0.0001\' <D$i/D$j/DBulk1x1/DRelax/INCAR >D$i/D$j/DBulk1x1/DPhonon/INCAR 
    done
done



###################################################################################################
#
# v1.0 (12/06/20):
# Copies down the T structure Se2 files from the sratch into my home directory for relaxation.
# Also changes the EDIFF and EDIFFG to finer convergence for higher accuracy relaxations in VASP.
# 
# 
# v1.1 (19/06/20) 
# Modified so this can be either used from the DStruc_T or DStruc_Hc directory. 
# 
# 
# 

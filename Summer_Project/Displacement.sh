#!/bin/bash
# BASH
# 
#Changes the k sampling points for all DStruc_T Se structures ready for EDisp run.
#DOES NOT find number of electrons/NBANDS --> do this manually after running this script.
# 
#Matt Evans
#University of Exeter
#me367@exeter.ac.uk
#30/06/20
#v1.3 
# 
###################################################################################################

Phase=$(echo $PWD | sed 's/\/home\/links\/me367\/DWork\/DTMDC\/DMX2\/DStruc_//')

#Run from your own DStruct_T directory
echo "$Phase"

if [ "$Phase" == "Hc" ]
then 
    Metal="Co Cr Cu Fe Hf Ir Mn Mo Ni Os Pb Pd Pt Re Rh Ru Sc Sn Ti V W Y Zr"
    #Metal="Fe Co"
    Chalc="S Se Te"
    basis=2 # atomic basis variable
    elec=0 # valence electrons of MX2 species
    bands=0
elif [ "$Phase" == "T" ]
then    
    Metal="Co Cr Cu Fe Ge Hf Ir Mn Mo Mo Nb Ni Os Pb Pd Pt Re Rh Ru Sc Sn Ta Ti V W Y Zr"
    #Metal="Fe Co"
    Chalc="Se Te"
    basis=1 # atomic basis variable
    elec=0 # valence electrons of MX2 species
    bands=0
fi


for i in $Metal
do
echo first loop
    for j in $Chalc
    do
echo second loop
	check=$(grep 'reached required accuracy - stopping structural energy minimisation' D$i/D$j/DBulk1x1/DPhonon/out.out)
	if [ ! -z "$check" ] # if string is NOT (!) zero, i.e. if the above string exists in out.out, perform the following...
	then
	    #if [ ! -e D$i/D$j/DBulk1x1/DPhonopy/INCAR ] # if the DPhonopy INCAR doesn't exit, make one
	    #then 
		a=$(grep 'ZVAL' D$i/D$j/DBulk1x1/DPhonon/POTCAR | sed 's\.* = \\; s\mass.*\\')
		for k in $a
		do
		    if [ "$Phase" == "Hc" ]
		    then
			elec=$(echo "$elec+($k*$basis)" | bc -l)
			basis=$(echo "$basis+2" | bc -l) # obtaining 4 chalcogen atoms for Hc strucs
		    elif [ "$Phase" == "T" ]
		    then
			elec=$(echo "$elec+($k*$basis)" | bc -l)
                        basis=$(echo "$basis+1" | bc -l) # obtaining 2 chalcogen atoms for T strucs
		    fi
		done

		mag=$(grep 'mag' D$i/D$j/DBulk1x1/DPhonon/out.out |tail -1|  sed 's\.* mag= \\; s\ *\\')
		Mag=$(echo $mag | awk 'function abs(v) {return v < 0 ? -v :v}; BEGIN {Mag=abs('$mag')} END {printf Mag}')
	       	echo $mag
	 
		if (( $(echo "$Mag > 0.01" | bc -l) )) 
		then
		    echo $i$j
		else
		    
		    mkdir -p D$i/D$j/DBulk1x1/DPhonopy
		    cp D$i/D$j/DBulk1x1/DPhonon/{INCAR,CONTCAR,KPOINTS,POTCAR} D$i/D$j/DBulk1x1/DPhonopy
		    if [ "$Phase" == "Hc" ]
		    then    
			bands=$(echo "($elec*6*6*1)/2+20" | bc) # calculating the number of bands
			
			sed "s/ NSW/# NSW/;
                             s/ ICHARG = 1/ ICHARG = 2/; 
                             s/ IBRION/# IBRION/; 
                             s/ NFREE/# NFREE/; 
                             s/ NELMIN/# NELMIN/; 
                             s/ NELMDL/# NELMDL/; 
                             s/ EDIFFG/# EDIFFG/;
                             s/ ISIF/# ISIF/;
                             s/ ISPIN/# ISPIN/;
                             s/# NCORE = [0-9]*/ NCORE = 24/;
                             s/ NBANDS = [0-9]*/ NBANDS = $bands/" <D$i/D$j/DBulk1x1/DPhonon/INCAR >D$i/D$j/DBulk1x1/DPhonopy/INCAR
			
			sed 's\ 12 12 6\ 2 2 6\' <D$i/D$j/DBulk1x1/DPhonon/KPOINTS >D$i/D$j/DBulk1x1/DPhonopy/KPOINTS	    
			mv D$i/D$j/DBulk1x1/DPhonopy/CONTCAR D$i/D$j/DBulk1x1/DPhonopy/POSCAR
		    elif [ "$Phase" == "T" ]
		    then
			bands=$(echo "($elec*6*6*2)/2+20" | bc) # calculating the number of bands                  
	
			sed "s/ NSW/# NSW/;
                             s/ ICHARG = 1/ ICHARG = 2/; 
                             s/ IBRION/# IBRION/;
                             s/ NFREE/# NFREE/;
                             s/ NELMIN/# NELMIN/;
                             s/ NELMDL/# NELMDL/;
                             s/ EDIFFG/# EDIFFG/;
                             s/ ISIF/# ISIF/;
                             s/ ISPIN/# ISPIN/;
                             s/# NCORE = [0-9]*/ NCORE = 24/;
                             s/ NBANDS = [0-9]*/ NBANDS = $bands/" <D$i/D$j/DBulk1x1/DPhonon/INCAR >D$i/D$j/DBulk1x1/DPhonopy/INCAR
			
			sed 's\ 12 12 12\ 2 2 6\' <D$i/D$j/DBulk1x1/DPhonon/KPOINTS >D$i/D$j/DBulk1x1/DPhonopy/KPOINTS
			mv D$i/D$j/DBulk1x1/DPhonopy/CONTCAR D$i/D$j/DBulk1x1/DPhonopy/POSCAR
		    fi
		fi
	    #fi
	else
	    echo $i$j
	fi
    done
    if [ "$Phase" == "Hc" ]
    then
	basis=2 # atomic basis variable
	elec=0 # valence electrons of MX2 species
	bands=0

    elif [ "$Phase" == "T" ]
    then
	basis=1 # atomic basis variable
	elec=0 # valence electrons of MX2 species
	bands=0
    fi
done

echo "FINISHED KPOINTS AMMENDMANTS, BAND CALCULATIONS & RELAXATION COMMENTED-OUT"


###################################################################################################
## Thanks and partial credit to Conor Price (and Joe Pitfield for input on L22 v1.0).
# v1.0 (16/06/20):
# Modifies KPOINTS and INCAR files to have correct band number for phonon displacement calculations.  
# 
# v1.1 (18/06/20);
# Included if statements to see check if the out.out file is completed and hence the calculations are finished.
# Modified sed statement for IBRION, NFREE etc to look for any numbers in INCAR --> [0-9]*. 
#
# v1.2 (19/06/20);
# Modified file so it can run from either the DStruc_T or DStruc_Hc directory.
#
# v1.3 (30/06/20);
# Included new commands into sed statements so that NCORE = 24.
# awk statement included to determine whether the TMDC is magnetic or not
# --> if magnetic, TMDC is printed to screen and the displacement set-up does not occur. 
# Thanks and credit to Conor Price for awk statement on line 65.

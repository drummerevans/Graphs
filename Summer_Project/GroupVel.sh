#!/bin/bash
# BASH
#
#Calculates the phonon group velocity for the acoustic modes.
#
#Matt Evans
#University of Exeter
#me367@exeter.ac.uk
#20/07/20
#v1.0
#
###################################################################################################

#Generating the ZA, TA and LA branch velocities

ZA=$(grep -n -m10 'group_velocity' band.yaml | tail -n1 | sed 's/[0-9]*:    group_velocity: \[ *//; s/,  */ /; s/,    -/ /; s/,  */ /;s/ \]//')
TA=$(grep -n -m11 'group_velocity' band.yaml | tail -n1 | sed 's/[0-9]*:    group_velocity: \[ *//; s/,  */ /; s/,    -/ /; s/,  */ /;s/ \]//')
LA=$(grep -n -m12 'group_velocity' band.yaml | tail -n1 | sed 's/[0-9]*:    group_velocity: \[ *//; s/,  */ /; s/,    -/ /; s/,  */ /;s/ \]//')

#echo "$ZA"
#echo "$TA"
#echo "$LA"

ZA_squared=0
TA_squared=0
LA_squared=0

# now computing the modulus of the group velocities
square() {
    my_var=$(echo "$1")
    my_var=0
    branch=$(echo "$2")
    
    for i in $branch
    do
	 number=$(echo "$i^2" | bc -l)
	 my_var=$(echo "$my_var+$number" | bc -l)
    done

    a=$(awk -v x=$my_var 'BEGIN {print sqrt(x)}')
    a=$(echo "$a*100" | bc -l) # converting group vel to m/s
    echo "$a"
}

vg1=$(square "$ZA_squared" "$ZA") 
echo "Group Velocity of the ZA branch is: $vg1 m/s"    
echo "-----------------------------------------------"
	
vg2=$(square "TA_squared" "$TA")
echo "Group Velocity of the TA branch is: $vg2 m/s"
echo "-----------------------------------------------"

vg3=$(square "TA_squared" "$LA")
echo "Group Velocity of the LA branch is: $vg3 m/s"
echo "-----------------------------------------------"


###################################################################################################
#
# v1.0 (20/07/20):
# Calculates the phonon group velcities for the three acoustic modes: ZA, TA and LA.
# Needs to be run in the DPhonopy directory for the specific TMDC.
#
#
#
#
#
#
#

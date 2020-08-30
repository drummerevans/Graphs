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

#Generating the ZA, TA and LA branch velocities for the bottom six heterostructure branches

ZA1=$(grep -n -m19 'group_velocity' band.yaml | tail -n1 | sed 's/[0-9]*:    group_velocity: \[  *//; s/,    / /; s/,    -/ /; s/,  */ /;s/ \]//')
TA1=$(grep -n -m20 'group_velocity' band.yaml | tail -n1 | sed 's/[0-9]*:    group_velocity: \[  *//; s/,    / /; s/,    -/ /; s/,  */ /;s/ \]//')
LA1=$(grep -n -m21 'group_velocity' band.yaml | tail -n1 | sed 's/[0-9]*:    group_velocity: \[  *//; s/,    / /; s/,    -/ /; s/,  */ /;s/ \]//')
ZA2=$(grep -n -m22 'group_velocity' band.yaml | tail -n1 | sed 's/[0-9]*:    group_velocity: \[  *//; s/,    / /; s/,    -/ /; s/,  */ /;s/ \]//')
TA2=$(grep -n -m23 'group_velocity' band.yaml | tail -n1 | sed 's/[0-9]*:    group_velocity: \[  *//; s/,    / /; s/,    -/ /; s/,  */ /;s/ \]//')
LA2=$(grep -n -m24 'group_velocity' band.yaml | tail -n1 | sed 's/[0-9]*:    group_velocity: \[  *//; s/,    / /; s/,    -/ /; s/,  */ /;s/ \]//')

#echo "$ZA1"
#echo "$TA1"
#echo "$LA1"

ZA1_squared=0
TA1_squared=0
LA1_squared=0
ZA2_squared=0
TA2_squared=0
LA2_squared=0

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

vg1=$(square "$ZA1_squared" "$ZA1") 
echo "Group Velocity of the 1st ZA branch is: $vg1 m/s"    
echo "-----------------------------------------------"
	
vg2=$(square "TA1_squared" "$TA1")
echo "Group Velocity of the 1st TA branch is: $vg2 m/s"
echo "-----------------------------------------------"

vg3=$(square "TA1_squared" "$LA1")
echo "Group Velocity of the 1st LA branch is: $vg3 m/s"
echo "-----------------------------------------------"

vg4=$(square "$ZA2_squared" "$ZA2")
echo "Group Velocity of the 2nd ZA branch is: $vg4 m/s"
echo "-----------------------------------------------"

vg5=$(square "TA2_squared" "$TA2")
echo "Group Velocity of the 2nd TA branch is: $vg5 m/s"
echo "-----------------------------------------------"

vg6=$(square "LA2_squared" "$LA2")
echo "Group Velocity of the 2nd LA branch is: $vg6 m/s"
echo "-----------------------------------------------"


###################################################################################################
#
# v1.0 (20/07/20):
# Calculates the phonon group velcities for the six acoustic modes: ZA, TA and LA in the heterostructure.
# Needs to be run in the DPhonopy directory for the specific TMDC heterostructure.
#
#
#
#
#
#
#

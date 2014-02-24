#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hongo-e_5
#
# Created:     06/02/2014
# Copyright:   (c) hongo-e_5 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def switchcase(x):
    z = " "
    for i in x:
        if i.upper() == i:
            z += i.lower()
        elif i.lower() == i:
            z += i.upper()
        else:
            z += i
    return z
file = open("caseinverterdata.txt", "r")
for line in file:
    print switchcase(line)
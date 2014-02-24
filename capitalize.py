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

file = open("capitalizedata.txt", "r")

for line in file:
    x = line.split(" ")
    w = " "
    for i in x:
        p = x.index(i)
        y = x[p]
        z = y[0]
        newline = z.upper() + y[1:]
        w += newline + " "
    print w

file.close()
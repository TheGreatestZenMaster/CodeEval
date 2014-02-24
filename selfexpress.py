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

file = open("selfexpressdata.txt", "r")

for line in file:
    x = line
    for i in x:
        if i == x.count(i):
            print "Yes"
        else:
            print "no"

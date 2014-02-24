#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ooshima-e_alt
#
# Created:     05/02/2014
# Copyright:   (c) ooshima-e_alt 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

file = open("newtest.txt", "w")

file.write("Hello, I am a new file!\n")
file.write("This is the second line\n")

file.close()

z = open("newtest.txt", "r")
for line in f:
    x = line.split()
    print x[-2]
z.close()
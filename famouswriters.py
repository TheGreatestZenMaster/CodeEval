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

file = open("famouswritersdata.txt", "r")

for line in file:
    for i in line:
        if i == "|":
            x = line.index(i)
            data = line[:x+1]
            code = line[x:]
            code = code.split(" ")
            z = " "
            for i in code:
                if i == " " or i == "|":
                    z += " "
                else:
                    z += data[int(i)-1]
            print z


file.close
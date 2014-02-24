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

file = open("compressedsequencedata.txt", "r")
file1 = open("compressedsequencedata.txt", "r")
def file_len(fname):
    for i, l in enumerate(fname):
            pass
    return i + 1

if file_len(file1) in range(20, 50):
    output = ""
    for line in file:
        z = line.split(" ")
        for i in z:
            y = z.count(i)
            if y in range(1, 400) and (i not in output):
                if int(i) in range(1, 99):
                    output += str(y) + " " + str(i) + " "
                else:
                    output += ""
        print output
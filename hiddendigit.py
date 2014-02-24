#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hongo-e_5
#
# Created:     07/02/2014
# Copyright:   (c) hongo-e_5 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

file = open("hiddendigitdata.txt", "r")

def decode(x):
    if x.isdigit() == True:
        y = x
    elif x == "a":
        y = 0
    elif x == "b":
        y = 1
    elif x == "c":
        y = 2
    elif x == "d":
        y = 3
    elif x == "e":
        y = 4
    elif x == "f":
        y = 5
    elif x == "g":
        y = 6
    elif x == "h":
        y = 7
    elif x == "i":
        y = 8
    elif x == "j":
        y = 9
    else:
        y = ""
    return y


for line in file:
    y = ""
    for i in line:
        y += str(decode(i))
    if y == "":
        y = "NONE"
    print y

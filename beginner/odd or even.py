#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rgcet
#
# Created:     10/03/2018
# Copyright:   (c) rgcet 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main(ch):
 ch = input("Enter a character: ")
if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")
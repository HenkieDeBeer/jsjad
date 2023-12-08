# parts of code used fromhttps://www.murky.org/blog/2020-8/vigkeylength
from Keylength import determineOffset
from Split import shiftLetters
from Decoder import decode

# grab the ciphertext
filetimetable = open("vigciphertext.txt","r")
lines=filetimetable.readlines()
filetimetable.close()

# let's make it all one string
working=""
for line in lines:
    for char in line:
        asc=ord(char)
        if (64 < asc < 91) or ( 96 < asc < 123):
            char=char.upper()
            working+=char


TASK = "KEYLENGTH"
SPLITCONSTANT = 1
SHOWSUBSET = 1
SHIFT = -1
KEY=""

if TASK == "KEYLENGTH":
  determineOffset(working)
elif TASK == "SPLITANDSHIFT":
  shiftLetters(working, SPLITCONSTANT, SHOWSUBSET, SHIFT)
elif TASK == "DECODE":
  decode(working, KEY)
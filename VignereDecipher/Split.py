
import string

def shiftLetters(working, SPLITCONSTANT, SHOWSUBSET, SHIFT):
  if SPLITCONSTANT < 1 or SHOWSUBSET < 1 or SHOWSUBSET > SPLITCONSTANT:
    print("Verander de constanten")
  else:
    splited = []
    for i in range(SPLITCONSTANT):
      splited.append(dict.fromkeys(string.ascii_uppercase, 0))
    
    for i in range(len(working)):
      putInto = i % SPLITCONSTANT
      letter = working[i]
      splited[putInto][letter] += 1


    if SHIFT >= 0 and SHIFT < 26:
      print("keyletter", chr(ord("A")+SHIFT), "for subset", SHOWSUBSET)
      subset = splited[SHOWSUBSET-1]
      for key in subset.keys():
        newLetter = chr((ord(key) - 65 + SHIFT)%26 + 65)
        print(newLetter,"-->", key, ":", subset[newLetter])
    else:
      print (splited[SHOWSUBSET-1])



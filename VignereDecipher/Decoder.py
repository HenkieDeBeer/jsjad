def decode(working, KEY):
  keyShift = []
  for i in range(len(KEY)):
    shift = ord(KEY[i]) - ord("A")
    keyShift.append(shift)

  for i in range(len(working)):
    shift = keyShift[i%len(KEY)]
    newLetter = chr((ord(working[i])-shift+26-ord("A"))%26+ord("A"))
    print(newLetter, end="")
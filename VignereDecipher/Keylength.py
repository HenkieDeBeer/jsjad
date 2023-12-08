# https://www.murky.org/blog/2020-8/vigkeylength

def determineOffset(working):
  # shift  the ciphertext against itself.
  # count up number of matches between
  # ciphertext and shifted ciphertext
  offsets=[]
  data=[]

  # this is for lebelling the peaks
  threshold=0
  offset = 1

  # let's only do a small number of shifts, more text, longer keys tested.
  # you might want to fiddle with the top value in the range
  for offset in range(1,int(len(working)/10)):
      matches=0
      for j in range(len(working)-offset):
          if working[j]==working[j+offset]:
              matches+=1
      threshold+=matches
      data.append(matches)
      offsets.append(offset)
      
  # this sets a threshold above which a point is labelled
  threshold=int(1.2*threshold/offset)
  for i in range(len(offsets)):
    if data[i] > threshold :
      print(offsets[i],": ", data[i])

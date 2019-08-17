def insertions(seq):
  for end in range(len(seq)):
    pos= end
    while pos>0 and seq[pos]<seq[pos-1]:
      (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
      pos=pos-1
  print(seq)
insertions([9,5,10,2,6])


def selection_sort(li):
  for start in range(len(li)):
    minpostion=start
    for i in range(start,len(li)):
      if li[i] < li[minpostion]:
        minpostion=i
    (li[start],li[minpostion])=(li[minpostion],li[start])
  print(li)
selection_sort([5,4,1,9,3,6,8])

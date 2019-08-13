def bSearch(ls,v,l,h):
   if h-l==0:
     print(False)
   mid=(l+h)//2
   if ls[mid]==v:
     print(True)
   if v<ls[mid]:
     print(bSearch(ls,v,l,mid))
   else:
     print(bSearch(ls,v,mid+1,h))
ls=[0,1,2,3,4,5,6,7,8,9]
bSearch(ls,12,0,10)

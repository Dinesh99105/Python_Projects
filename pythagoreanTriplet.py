def pythatrio(n):
  ls=[(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x*x+y*y==z*z ]
  return(ls)
print(pythatrio(100))

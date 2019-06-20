# program for finding prime number in given range

def isprime(n) :
    if n==1 :
       print("1 is a special case")
       return False
    for x in range(2,n) :
        if n%x==0 :
           print("{} is equal to {}x{}".format(n,x,n//x))
           return False
    else :
           print("{} is a prime number".format(n))
           return True
for n in range(1,1000) :
    isprime(n)

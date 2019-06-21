# shows how to handel exception in python
try:
   fh = open("xline.txt")
   for line in fh.readlines():
       print(line)
except IOError as e:
      print("error({})".format(e))
print("msg after error")

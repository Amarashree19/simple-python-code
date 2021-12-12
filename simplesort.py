from functools import reduce
l=[45,20,37,11]
a=[]
i=len(l)
while i!=0:
  min1=reduce(min,l)
  #print(min)
  a.append(min1)
  l.remove(min1)
  i=len(l)
  if i==0:
   break
print("the soeted list is\n")
print(a)

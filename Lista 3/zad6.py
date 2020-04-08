import math
def promien(x,y,a=0,b=0):
  r2=(x-a)*(x-a)+(y-b)*(y-b)
  r=math.sqrt(r2)
  return r

print(promien(2,4))
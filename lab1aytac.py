import math
p=0
eps=0.001
x=0.5
a=math.sin(x)

p=0
n=2
while(a/(math.factorial(n)))>eps:
    a=(-1)*math.sin(x)*n
    p+=a
    n+=1
print("p=",p)

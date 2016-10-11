
import matplotlib.pyplot as plt
import random

b=3
a=-3
N=1000
g=0.0
Integral=0.0
fx=0.0
fx1=0.0
xi=[]
yi=[]

random.seed(0)

a=-3
b=3
N=1000


k=b-a

for i in range (N):

  g=random.random()

  x= a + g*(b-a)

  if x>=-2.0 or x<= 2.0:
            fx1=-x**2+4
  else:
    fx1=0

  yi.append(fx1)
  xi.append(x)


  fx=fx+fx1


Integral=(1/N)*k*fx
print('Интеграл=',Integral)

plt.scatter(xi, yi)


plt.show()


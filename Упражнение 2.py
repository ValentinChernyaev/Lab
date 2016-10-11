# http://www.cyberforum.ru/turbo-pascal/thread1294897.html
import matplotlib.pyplot as plt
import random

g=0.0
Integral=0.0
fx=0.0
fx1=0.0
xi=[]
yi=[]

random.seed(0)

a=-2 # реальный интервал от -2 до 2..
b=2  # в задаче зачем-то от -3 до 3
N=1000000


k=b-a # Переменной"k"присвоим значение длины промежутка интегрирования}

for i in range (N):
    #проведем N испытаний
  g=random.random() # g - случайная величина из промежутка [0;1]}

  x= a + g*(b-a) # произвольная величина из [a; b] }
 # print(g,x)

  if x>=-2.0 or x<= 2.0:  # Вычисляем функцию
            fx1=-x**2+4
  else:
    fx1=0

  yi.append(fx1)
  xi.append(x)
  #print (fx1, x)

  fx=fx+fx1


Integral=(1/N)*k*fx
print ("Количество случайных значений u=", N)
print('Интеграл=',Integral)
# Построить точки
#plt.scatter(xi, yi)

#plt.plot(xi, yi)
#plt.show()


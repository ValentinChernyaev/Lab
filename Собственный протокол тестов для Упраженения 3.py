import numpy, random
import matplotlib.pyplot as plt
sum=0


def get_percentile(values, bucket_number):
 step=0
 step=100/bucket_number # шаг для вычисления

 percentiles = [0.0 for x in range(bucket_number)] #соорудили список
 for i in range(1,bucket_number,1):
    # вычислили i-ый персентель с округлением до 2х знаков
     percentiles[i]=round(numpy.percentile(values, i*step), 2)

 return percentiles

def get_percentile_number(value, percentiles):
 number=0
 uspeh=False
 length=len(percentiles)
 for i in range(0,length):
     if percentiles[i]>value: # Больше текущего
          number=i-1 # взять предыдущее значение
          uspeh=True
          break
 if number<0: # это был первый элемент
   i=0 # взять нормальный индекс
   uspeh=True # нашли
# Не нашли => Больше всех
 if not uspeh: number=length-1

 return number

def value_equalization(value, percentiles, add_random=False):
 step=0.0
 random_noise=0.0

 idx = get_percentile_number(value, percentiles)
 step = 1/len(percentiles)

 # Добавить шум
 if add_random:
    random_noise=random.random()*step
 else:
    random_noise=0

 new_value = float(idx)*step+random_noise

 return new_value



def values_equalization(val, percentiles, add_random=False):
 # Нужно скопировать спискок и работать с копией...
 # иначе менялся ВХОДНОЙ СПИСОК из-за
 # передача параметра val по ССЫЛКЕ И ЭТО ЖЕСТЬ!!!
 val_temp = val[:]
 for i in range(len(val_temp)):
       temp=val_temp[i]
       val_temp[i]=value_equalization(temp, percentiles, add_random)
 return val_temp



values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

percentiles = get_percentile(values, 5)
print(percentiles)

print(get_percentile_number(2.5, percentiles))
print(get_percentile_number(5.5, percentiles))
print(get_percentile_number(100, percentiles))

print(value_equalization(5.5, percentiles))
print(value_equalization(5.5, percentiles, add_random=True))

percentiles = get_percentile(values, 4)
print(percentiles)
print(values_equalization(values, percentiles, add_random=True))

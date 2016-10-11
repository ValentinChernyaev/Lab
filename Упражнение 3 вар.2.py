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


data=numpy.ones((200,267))
file_in = open('c:\img.txt', 'r')
i=0
for stroka in file_in.readlines():

    lst = stroka.split()
    for j in range(len(lst)):
         data[i][j]=lst[j]
    i+=1

plt.subplot(221) # 2 строки 2 столбца для построения Область 1
plt.title('Picture before')
plt.imshow(data, cmap = plt.get_cmap('gray'))

plt.subplot(222) # 1 строки 2 столбца для построения Область 2
plt.title('Histogram before..')
vector=data.flatten()
plt.hist(vector, bins=10, color='red')









vector_ekv = vector[:] #Переписать вектор в новый
bucket_number=int(input("Введите bucket_number (стандартное значение-4)"))

percentil_ekv=get_percentile(vector_ekv,bucket_number) # Получить персентели

final_vector=values_equalization(vector_ekv,percentil_ekv,True) # эквализация

#------Новый орёл-----------------------
new_data = final_vector.reshape((200, 267)) # Пересобрать массив

plt.subplot(223) # 2 строки 2 столбца для построения Область 3
plt.title('Picture after..')
plt.imshow(new_data, cmap = plt.get_cmap('gray'))
#------Новая гистограмма-----------------------
plt.subplot(224) # 1 строки 2 столбца для построения Область 2
plt.title('Histogram after (bucket_number '+str(bucket_number)+')')
plt.hist(final_vector, bins=10, color='orange')

plt.show()


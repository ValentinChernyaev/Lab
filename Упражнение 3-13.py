<<<<<<< HEAD
﻿import numpy, random
import matplotlib.pyplot as plt
sum=0

ind=[]
index=[]


data=numpy.ones((200,267))
file_in = open('c:\img.txt', 'r')
i=0
for stroka in file_in.readlines():

    lst = stroka.split()
    for j in range(len(lst)):
         data[i][j]=lst[j]
    i+=1

for i in range(200):
    ind.append(i)

for i in range (100):
   index.append(random.sample(range(200),1))

print(index)
data1=numpy.ones((100,267))

for i in range(100):
    ind=index[i]

    for j in range(267):
        data1[i][j]=data[ind[0]][j]




plt.title('Picture 100 random.sample()')
plt.imshow(data1, cmap = plt.get_cmap('gray'))

plt.show()

=======
﻿import numpy, random
import matplotlib.pyplot as plt
sum=0

ind=[]
index=[]


data=numpy.ones((200,267))
file_in = open('c:\img.txt', 'r')
i=0
for stroka in file_in.readlines():

    lst = stroka.split()
    for j in range(len(lst)):
         data[i][j]=lst[j]
    i+=1

for i in range(200):
    ind.append(i)

for i in range (100):
   index.append(random.sample(range(200),1))

print(index)
data1=numpy.ones((100,267))

for i in range(100):
    ind=index[i]

    for j in range(267):
        data1[i][j]=data[ind[0]][j]




plt.title('Picture 100 random.sample()')
plt.imshow(data1, cmap = plt.get_cmap('gray'))

plt.show()

>>>>>>> dd87a4c235bdcc202d73d85476b002e3582c8553

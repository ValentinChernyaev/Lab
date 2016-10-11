import numpy, random
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
   index.append(random.choice(ind))

data1=numpy.ones((100,267))

for i in range(100):

    for j in range(267):
     data1[i][j]=data[index[i]][j]




plt.title('Picture 100 random.choice()')
plt.imshow(data1, cmap = plt.get_cmap('gray'))

plt.show()


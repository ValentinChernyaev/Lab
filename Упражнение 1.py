import matplotlib.pyplot as plt
import random

random.seed(0)
N = 1000
values = [random.normalvariate(0, 1) for i in range(N)]
plt.hist(values, bins=100)


     #subplot 1
plt.subplot(221)
random.seed(0)
N = 100
values = [random.normalvariate(0, 1) for i in range(N)]
plt.title(r'$N=100$')
plt.hist(values, bins=100, color='green')
plt.grid(True)

     #subplot 2
plt.subplot(222)
random.seed(0)
N = 1000
plt.title(r'$N=1000$')
values = [random.normalvariate(0, 1) for i in range(N)]
plt.hist(values, bins=100, color='red')
plt.grid(True)

     #subplot 3
plt.subplot(223)
random.seed(0)
N = 10000
plt.title(r'$N=10000$')
values = [random.normalvariate(0, 1) for i in range(N)]
plt.hist(values, bins=100)
plt.grid(True)

     #subplot 4
plt.subplot(224)
random.seed(0)
N = 100000
plt.title(r'$N=100000$')
values = [random.normalvariate(0, 1) for i in range(N)]
plt.hist(values, bins=100, color='orange')
plt.grid(True)

plt.show()
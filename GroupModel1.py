import numpy as np
import matplotlib.pyplot as plt

import random

#x = random.random()

#print(x)

for i in range(100):
  x = 100.0*random.random()
#  print i
  print x


x3 = np.random.rand(100)
print x3

plt.hist(np.random.rand(1000))

x1 = np.arange(-3, 3, 0.1)
y = np.sin(x1)
#plt.plot(x1,y)

plt.show()
#plt.savefig("image.png")



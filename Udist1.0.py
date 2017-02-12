import numpy as np
import matplotlib.pyplot as plt



#nx = [0]*10

#nx.append([1,2])
#print nx[:]

#nxx = [0]
#nxx.append([1,2])
#print nxx[:]
nindex = []
#ny = [0]*10
#ny = []

n = 0
nxxx = 0
nyyy = 0
x = np.random.rand(1000)*100
y = np.random.rand(1000)*100
#print x[0],y[0]

while n < 1000:
 if x[n] < 10:
  nxxx = 1
 elif x[n] < 20:
  nxxx = 2
 elif x[n] < 30:
  nxxx = 3
 elif x[n] < 40:
  nxxx = 4
 elif x[n] < 50:
  nxxx = 5
 elif x[n] < 60:
  nxxx = 6
 elif x[n] < 70:
  nxxx = 7
 elif x[n] < 80:
  nxxx = 8
 elif x[n] < 90:
  nxxx = 9
 elif x[n] <= 100:
  nxxx = 10

 if y[n] < 10:
  nyyy = 1
 elif y[n] < 20:
  nyyy = 2
 elif y[n] < 30:
  nyyy = 3
 elif y[n] < 40:
  nyyy = 4
 elif y[n] < 50:
  nyyy = 5
 elif y[n] < 60:
  nyyy = 6
 elif y[n] < 70:
  nyyy = 7
 elif y[n] < 80:
  nyyy = 8
 elif y[n] < 90:
  nyyy = 9
 elif y[n] <= 100:
  nyyy = 10

 nindex.append([nxxx, nyyy])
 n = n + 1
 nxxx = 0
 nyyy = 0
#print nindex

#print nindex.count([1,1])
#print nindex.index([1,1])
ite = 0
chk = 0
while ite < 1e4:

 chk1 = 0
 while chk1 == 0:
  x_strt = np.random.randint(1,11)
  y_strt = np.random.randint(1,11)
# print nindex
  chk1 = nindex.count([x_strt,y_strt])
# if chk == 0:
#  ite = ite +1
#  print 'Zero sample for start was detected'
 strt = nindex.index([x_strt,y_strt])
 print 'index of start: ',strt
 print 'index of start: ',nindex[strt]
 print 'x_strt, y_strt: ',x_strt, y_strt

 chk2 = 0
 while chk2 == 0:
  x_dest = np.random.randint(1,11)
  y_dest = np.random.randint(1,11)
  chk2 = nindex.count([x_dest,y_dest])
  print chk2

# if chk2 == 0:
#  ite = ite +1
#  print 'Zero sample for destination was detected'
 dest = nindex.index([x_dest,y_dest])

 x[strt] = float(x_dest*10)-np.random.uniform(0.00001,10)
 y[strt] = float(y_dest*10)-np.random.uniform(0.00001,10)
 print 'dest x,y index:  ', x_dest,' ', y_dest
 print 'dest crd: ',x[strt],y[strt]
 print

# Update for nindex
 nindex[strt] = nindex[dest]
 ite = ite + 1


fig = plt.figure()

ax = fig.add_subplot(1,1,1)

ax.scatter(x,y,s=1)
ax.set_title('random plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

ax.grid(True)

plt.savefig('testfig')
plt.show()



import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)

plt.plot(x,y)
plt.show()

a = np.arange(0,4*np.pi,0.1)
b = np.sin(a)
c = np.arange(0,4*np.pi,0.1)
d = np.cos(c)

plt.plot(a,b,c,d)
plt.title(" GRAPH of SIN and COS from 0 to 4π")
plt.legend(["sin(x)","cos(x)"])
plt.xlabel("cosx from x to 4π")
plt.ylabel("sinx from x to 4π")
plt.show()

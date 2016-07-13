import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)

b = np.log(x)

plt.plot(x, y) 
plt.plot(x, b)

#plt.show() 

plt.xlabel("cheese")
plt.ylabel("crackers")

# plt.show() 


x.plot.box()
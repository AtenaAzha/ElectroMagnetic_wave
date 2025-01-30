import numpy as np
import matplotlib.pyplot as plt
import time

c = 3
lambda1 = 1
lambda2 = 0.5
K = 2*np.pi/lambda1
k_av = 2*np.pi/lambda2
Omega = np.array([c*K])
omega_av = np.array([c*k_av])
A = 0.2
t = 6
x = np.arange(0, 2*np.pi, 0.1)
# print(type(K*x), type(Omega*t))
# print((K*x).shape, (Omega*t).shape)

# quit()
object1 = np.array([float(K*x)[0] , float(Omega*t)])
object2 = np.array([float(k_av*x)[0] , float(omega_av*t)])

y1 = np.cos(object1)
y2 = np.cos(object2)
Y = (2*A) * (y1*y2)

# Plotting Sine Graph
plt.plot(x, Y, color='green')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

c = 3e8
landa1 = 2
landa2 = 2
wave_num1 = 2*np.pi / landa1
wave_num2 = 2*np.pi / landa2
omega1 = c * wave_num1
omega2 = c * wave_num2
domain = 0.5

x_space = np.linspace(0 , 10 , 500)
t_space = np.linspace(0 , 10 , 100)


fig , ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)

wave1, = ax.plot([], [], color='r', label="Wave 1")
wave2, = ax.plot([], [], color='b', label="Wave 2")
super_wave, = ax.plot([], [], color='g', label="Superposition")
ax.legend()


def moving(t):
    y1 = domain * np.cos(wave_num1 * x_space - omega1 * t)
    y2 = domain * np.cos(wave_num2 * x_space - omega2 * t + np.pi / 3)
    y_sum = y1 + y2

    wave1.set_data(x_space , y1)
    wave2.set_data(x_space , y2)
    super_wave.set_data(x_space, y_sum)
    return wave1, wave2, super_wave

ani = animation.FuncAnimation(fig, moving, frames=t_space, interval=50, blit=True)
plt.show()


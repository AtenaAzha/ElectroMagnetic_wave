import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class SuperPosition:
    def __init__(self):
        self.c = 3e8
        self.landa1 = 2
        self.landa2 = 2
        self.wave_num1 = 2*np.pi / self.landa1
        self.wave_num2 = 2*np.pi / self.landa2
        self.omega1 = self.c * self.wave_num1
        self.omega2 = self.c * self.wave_num2
        self.domain = 0.5

    def info(self):
        self.x_space = np.linspace(0 , 10 , 500)
        self.t_space = np.linspace(0 , 10 , 100)


        self.fig , self.ax = plt.subplots()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(-2, 2)

        self.wave1, = self.ax.plot([], [], color='r', label="Wave 1")
        self.wave2, = self.ax.plot([], [], color='b', label="Wave 2")
        self.super_wave, = self.ax.plot([], [], color='g', label="Superposition")
        self.ax.legend()


        def moving(t):
            y1 = self.domain * np.cos(self.wave_num1 * self.x_space - self.omega1 * t)
            y2 = self.domain * np.cos(self.wave_num2 * self.x_space - self.omega2 * t + np.pi / 3)
            y_sum = y1 + y2

            self.wave1.set_data(self.x_space , y1)
            self.wave2.set_data(self.x_space , y2)
            self.super_wave.set_data(self.x_space, y_sum)
            return self.wave1, self.wave2, self.super_wave

        self.ani = animation.FuncAnimation(self.fig, moving, frames=self.t_space, interval=50, blit=True)
        return plt.show()


ins = SuperPosition()
print(ins.info())
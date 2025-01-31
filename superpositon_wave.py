import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class SuperPosition:
    def __init__(self):
        self.c = 3e8
        self.landa1 = 5
        self.landa2 = 5.5
        self.wave_num1 = 2*np.pi / self.landa1
        self.wave_num2 = 2*np.pi / self.landa2
        self.omega1 = self.c * self.wave_num1
        self.omega2 = self.c * self.wave_num2
        self.domain = 0.5
        self.vg = (self.omega2 - self.omega1) / (self.wave_num2 - self.wave_num1)
        self.Wave_Num = 2 * np.pi / (self.landa1 + self.landa2)
        self.Omega = self.vg * self.Wave_Num

    def info(self):
        self.x_space = np.linspace(-50 , 50 , 500)
        self.t_space = np.linspace(0 , 1e-8 , 100)


        self.fig , self.ax = plt.subplots(figsize = (10,5))
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-3, 3)

        self.wave1, = self.ax.plot([], [], color='r', label="Wave 1")
        self.wave2, = self.ax.plot([], [], color='b', label="Wave 2")
        self.pac_wave, = self.ax.plot([], [], color='g', label="wave_packet")
        self.ax.legend()


        def moving(t):
            y1 = self.domain * np.cos(self.wave_num1 * self.x_space - self.omega1 * t)
            y2 = self.domain * np.cos(self.wave_num2 * self.x_space - self.omega2 * t + np.pi / 3)
            y_pac = 2*self.domain*(np.cos(self.Wave_Num * self.x_space - self.Omega * t))

            self.wave1.set_data(self.x_space , y1)
            self.wave2.set_data(self.x_space , y2)
            self.pac_wave.set_data(self.x_space, y_pac)
            return self.wave1, self.wave2, self.pac_wave

        self.ani = animation.FuncAnimation(self.fig, moving, frames=self.t_space, interval=50, blit=True)
        return plt.show()


ins = SuperPosition()
print(ins.info())
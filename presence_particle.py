import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class ObjectPosition:
    def __init__(self):
        self.c = 3e8
        self.landa = 2   
        self.wave_num = 2 * np.pi / self.landa
        self.omega = self.c * self.wave_num

    def data(self):
        self.x_space = np.linspace(-10, 10, 500)
        self.t_space = np.linspace(0, 10, 100)

        self.object_position = 2 
        self.reflection_coefficient = 0.5

        self.figur, self.axes = plt.subplots(figsize=(8, 4))
        self.axes.set_xlim(-10, 10)
        self.axes.set_ylim(-1.5, 1.5)

        self.wave, = self.axes.plot([], [], 'b', label="EM_wave")
        self.axes.axvline(self.object_position, color='r', linestyle='--', label="object_place")
        self.axes.legend()
       
        def moving(t):
            wave_ = np.cos(self.wave_num * self.x_space - self.omega * t)
            wave_[self.x_space > self.object_position] *= self.reflection_coefficient 
    
            self.wave.set_data(self.x_space, wave_)
            return self.wave,
        self.ani = animation.FuncAnimation(self.figur, moving, frames=self.t_space, interval=50, blit=True)
        return plt.show()


ins = ObjectPosition()
print(ins.data())